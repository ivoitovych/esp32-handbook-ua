#!/bin/sh
# Спільна бібліотека перевірок авторства. Підключається з commit-msg і pre-push.
#
# Політика (незмінна умова проєкту):
#   1. У повідомленні коміту немає жодних записів співавторства
#      і жодних згадок про інструменти-асистенти.
#   2. Поля author і committer кожного коміту дорівнюють ідентичності
#      з .githooks/identity.conf — обидва, точно, без винятків.
#   3. У тексті довідника немає згадок про інструменти-асистенти.

hook_dir=$(dirname "$0")
[ -f "$hook_dir/identity.conf" ] && . "$hook_dir/identity.conf"
: "${EXPECTED_NAME:?identity.conf: EXPECTED_NAME не задано}"
: "${EXPECTED_EMAIL:?identity.conf: EXPECTED_EMAIL не задано}"

# Заборонені рядки у повідомленнях комітів.
# Кожен РЯДОК — окремий ERE-патерн; порівняння без урахування регістру.
# Патерни містять пробіли, тому обхід — через for_each_pattern, а не
# через $(...) з розбиттям на слова.
FORBIDDEN_MSG_PATTERNS='
co-authored
assisted-by:
generated with
claude
anthropic
chatgpt
openai
copilot
gpt-[0-9]
llm-generated
ai-generated
згенеровано (ші|ai)
🤖
'

# Заборонені рядки у вмісті тексту, що йде в друк.
FORBIDDEN_CONTENT_PATTERNS='
claude
anthropic
chatgpt
copilot
ai-generated
llm-generated
згенеровано (ші|ai)
🤖
'

# for_each_pattern <список> <команда…> — викликає команду для кожного
# непорожнього рядка списку, передаючи патерн першим аргументом.
for_each_pattern() {
	_list=$1
	shift
	printf '%s\n' "$_list" | while IFS= read -r _p; do
		[ -z "$_p" ] && continue
		"$@" "$_p"
	done
}

# check_message <файл-або-->  : 0 якщо чисто, 1 якщо знайдено заборонене
check_message() {
	_msg=$(cat "$1")
	_found=$(printf '%s\n' "$FORBIDDEN_MSG_PATTERNS" | while IFS= read -r _p; do
		[ -z "$_p" ] && continue
		if printf '%s\n' "$_msg" | grep -qiE -- "$_p"; then
			echo "  ✗ повідомлення коміту містить заборонений патерн: $_p"
		fi
	done)
	if [ -n "$_found" ]; then
		printf '%s\n' "$_found" >&2
		return 1
	fi
	return 0
}

# check_identity <sha> : 0 якщо author і committer збігаються з очікуваними
check_identity() {
	_sha=$1
	_hit=0
	_an=$(git log -1 --format='%an' "$_sha")
	_ae=$(git log -1 --format='%ae' "$_sha")
	_cn=$(git log -1 --format='%cn' "$_sha")
	_ce=$(git log -1 --format='%ce' "$_sha")
	[ "$_an" = "$EXPECTED_NAME" ]  || { echo "  ✗ author.name:    «$_an» ≠ «$EXPECTED_NAME»" >&2; _hit=1; }
	[ "$_ae" = "$EXPECTED_EMAIL" ] || { echo "  ✗ author.email:   «$_ae» ≠ «$EXPECTED_EMAIL»" >&2; _hit=1; }
	[ "$_cn" = "$EXPECTED_NAME" ]  || { echo "  ✗ committer.name: «$_cn» ≠ «$EXPECTED_NAME»" >&2; _hit=1; }
	[ "$_ce" = "$EXPECTED_EMAIL" ] || { echo "  ✗ committer.email:«$_ce» ≠ «$EXPECTED_EMAIL»" >&2; _hit=1; }
	return $_hit
}

# check_commit_message <sha>
check_commit_message() {
	_sha=$1
	_body=$(git log -1 --format='%B' "$_sha")
	_found=$(printf '%s\n' "$FORBIDDEN_MSG_PATTERNS" | while IFS= read -r _p; do
		[ -z "$_p" ] && continue
		if printf '%s\n' "$_body" | grep -qiE -- "$_p"; then
			echo "  ✗ повідомлення містить заборонений патерн: $_p"
		fi
	done)
	if [ -n "$_found" ]; then
		printf '%s\n' "$_found" >&2
		return 1
	fi
	return 0
}
