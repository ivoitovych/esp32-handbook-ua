#!/usr/bin/env python3
"""One randomised wave: N helpers × M tickets, drawn from the checkable pool.

## What this measures

Everything built on 2026-08-28 at once — the versioned task spec, the
self-contained card, the English verdict vocabulary — against the only
judge that cannot be argued with: layer 3, which searches for the quote
as a substring of the document the helper named.

## Why the pool is restricted, and why that is not cheating

A helper cannot verify a claim whose document is unreachable. Egress is
an organisation-level `403` on every manufacturer domain, so a ticket
without a local document can only ever come back "unreachable" — which
measures the network, not the technology.

So the pool is the units for which a candidate document **is present in
this container's cache**: 469 of 5715 unverified units. The sample is
random within that pool and therefore proportional across classes, not
picked for winnability.

    factcheck/tools/wave.py --plan DIR --agents 10 --tickets 20 --seed 20260829
    factcheck/tools/wave.py --judge DIR

## The serial rule, and why it is in the order

Each helper takes **one ticket at a time**: read it, answer it, write the
answer, and only then open the next. Not for tidiness — a helper that
reads twenty tickets before answering any of them carries twenty claims
in its head at once, and the cheapest way to discharge that load is to
answer from memory of the batch rather than from the document. The rule
is stated in the order because a rule the worker cannot see is not a
rule.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import pathlib
import random
import re
import sys

import config
from repo import ROOT  # noqa: E402  (root is found, not counted)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

KESH = ROOT / "factcheck" / "source-cache"
NEZVIRENI = "CEFGL"

BLOKY = ["ORIENTATION", "VERBATIM", "HONEST-MISS", "NETWORK", "STUB",
         "NO-SELF-REFERENCE", "VERDICTS-EXTERNAL", "ABSENCE", "FORMAT"]

RAMKA = """# Wave {wave} — ticket batch {n} of {vsyoho}: {k} claims

Random sample, seed **{nasinnya}**, drawn from the {pool} unverified
claims whose candidate document is present in this container's cache.

**The document is named on every ticket and it is on disk.** Read it
with your file tools; do not fetch anything from the network — nothing
is reachable from here.

## One ticket at a time

Answer ticket 1 completely and append its entry to your answer file
**before you read ticket 2**. Then ticket 2, and so on.

This is not tidiness. Holding twenty claims at once makes answering from
the batch cheaper than answering from the document — and layer 3 will
discard exactly that, so the work would be lost.
"""


def _nm2():
    spec = importlib.util.spec_from_file_location("nm2", ROOT / "factcheck" / "tools" / "order_m2.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def basein() -> list[dict]:
    """Незвірені одиниці, що мають кандидата в кеші."""
    import sample
    nm2 = _nm2()
    fayly = nm2.kesh_fayly()
    out = []
    for klas in NEZVIRENI:
        try:
            odyn = sample.odynyci(klas)
        except Exception:
            continue
        for u in odyn:
            kand = nm2.pidibraty(u["tekst"], fayly)
            if kand:
                out.append(dict(u, klas=klas, kandydat=kand))
    out.sort(key=lambda u: u["id"])
    return out


def konteksty() -> dict[str, str]:
    """`id` → оточення в книзі, з уже зрендерених карток."""
    import layer1
    out: dict[str, str] = {}
    for g in config.groups():
        d = config.cards_root() / g
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            for m in layer1.RE_KARTKA.finditer(f.read_text(encoding="utf-8")):
                k = (m.group("kontekst") or "").strip()
                if k:
                    out[m.group("id")] = k
    return out


def planuvaty(kudy: pathlib.Path, agentiv: int, kvytkiv: int,
              nasinnya: int, wave: str) -> int:
    import task_spec
    kudy.mkdir(parents=True, exist_ok=True)
    pool = basein()
    treba = agentiv * kvytkiv
    if len(pool) < treba:
        print(f"у басейні {len(pool)}, потрібно {treba} — беру всі")
        treba = len(pool)
    vzyato = random.Random(nasinnya).sample(pool, treba)
    kont = konteksty()

    versiya = task_spec.versiya(BLOKY, shablon=RAMKA)
    (kudy / "wave.json").write_text(json.dumps({
        "wave": wave, "seed": nasinnya, "order_version": versiya,
        "pool": len(pool), "agents": agentiv, "tickets_each": kvytkiv,
        "units": [u["id"] for u in vzyato],
        "by_class": {k: sum(1 for u in vzyato if u["status"] == k)
                     for k in NEZVIRENI},
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    for a in range(agentiv):
        chastka = vzyato[a * kvytkiv:(a + 1) * kvytkiv]
        if not chastka:
            break
        ramka = RAMKA
        for kk, vv in dict(wave=wave, n=a + 1, vsyoho=agentiv,
                           k=len(chastka), nasinnya=nasinnya,
                           pool=len(pool)).items():
            ramka = ramka.replace("{" + kk + "}", str(vv))
        r = [task_spec.sklasty(BLOKY, zaholovok=ramka, shablon=RAMKA),
             f"\n<!-- order_version:{versiya} wave:{wave} agent:{a+1} -->\n",
             "\n## Tickets\n"]
        for i, u in enumerate(chastka, 1):
            r.append(f"\n### Ticket {i} — `{u['id']}`  (current state `{u['status']}`)\n")
            r.append(f"**Claim:**\n\n> {u['tekst']}\n")
            k = kont.get(u["id"])
            if k:
                r.append("**Where it sits in the book:**\n\n```\n" + k + "\n```\n")
            fayly = u["kandydat"] if isinstance(u["kandydat"], list) else [u["kandydat"]]
            r.append("**Candidate document(s), already on disk:**\n")
            for f in fayly:
                r.append(f"- `source-cache/{f}`")
            r.append("")
        (kudy / f"agent-{a+1:02d}.md").write_text("\n".join(r) + "\n",
                                                  encoding="utf-8")
    print(f"хвиля {wave}: агентів {agentiv}, квитків {treba}, "
          f"насіння {nasinnya}, order_version {versiya} → {kudy}")
    print(f"  за класами: "
          f"{ {k: sum(1 for u in vzyato if u['status'] == k) for k in NEZVIRENI} }")
    return 0


def suddya(kudy: pathlib.Path) -> int:
    """Шар 3 як суддя: чи стоїть цитата в названому документі."""
    import layer3
    import yaml
    plan = json.loads((kudy / "wave.json").read_text(encoding="utf-8"))
    rody: dict[str, int] = {}
    doslivnykh = pereviryaly = 0
    bidy: list[str] = []
    for f in sorted(kudy.glob("answers-*.yaml")):
        try:
            dani = yaml.safe_load(f.read_text(encoding="utf-8")) or []
        except Exception as e:
            bidy.append(f"{f.name}: YAML не читається — {str(e)[:60]}")
            continue
        for z in dani:
            if not isinstance(z, dict):
                continue
            v = str(z.get("verdict") or z.get("verdykt") or "?")
            rody[v] = rody.get(v, 0) + 1
            if v not in ("confirmed", "disputes"):
                continue
            pereviryaly += 1
            cyt = str(z.get("quote") or "").strip()
            dzh = str(z.get("source") or "")
            imya = re.sub(r"^source-cache/", "", dzh).strip("`  ")
            p = KESH / imya
            if not cyt or not p.exists():
                bidy.append(f"{z.get('unit')}: джерело `{imya}` не знайдено")
                continue
            tekst = layer3.plaskyy(layer3.tekst_dzherela(p) or "")
            frah = layer3.uryvky(cyt)
            if frah and all(all(layer3.plaskyy(x) in tekst for x in g)
                            for g in frah):
                doslivnykh += 1
            else:
                bidy.append(f"{z.get('unit')}: цитати немає в `{imya}`")
    print(f"хвиля {plan['wave']} · насіння {plan['seed']} · "
          f"order_version {plan['order_version']}")
    print(f"  квитків роздано   {len(plan['units'])}")
    print(f"  відповідей        {sum(rody.values())}")
    print(f"  вердикти          {dict(sorted(rody.items()))}")
    print(f"  твердили доказ    {pereviryaly}")
    print(f"  пережили шар 3    {doslivnykh}"
          + (f"  ({100*doslivnykh/pereviryaly:.0f} %)" if pereviryaly else ""))
    for b in bidy[:12]:
        print(f"     ✗ {b}")
    if len(bidy) > 12:
        print(f"     … ще {len(bidy)-12}")
    return 0


def main() -> int:
    a = argparse.ArgumentParser()
    a.add_argument("--plan")
    a.add_argument("--judge")
    a.add_argument("--agents", type=int, default=10)
    a.add_argument("--tickets", type=int, default=20)
    a.add_argument("--seed", type=int, default=0)
    a.add_argument("--wave", default="w1")
    o = a.parse_args()
    if o.judge:
        return suddya(pathlib.Path(o.judge))
    if o.plan:
        if not o.seed:
            a.error("--plan без --seed: дослід буде невідтворний")
        return planuvaty(pathlib.Path(o.plan), o.agents, o.tickets,
                         o.seed, o.wave)
    a.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
