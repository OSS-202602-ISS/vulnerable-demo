# vulnerable-demo

> **This repository is deliberately out of date.** It is teaching material for
> the Open Source Software course (Chapter 10, "Is My Open Source Safe?").
> Every version in `requirements.txt` has known security problems. That is the point.

## Do not install it

**Do not run `pip install -r requirements.txt` here.** You would put known-vulnerable
code into your environment.

You only **check** this list. The check plans an install in a temporary place and
throws it away; nothing is installed into your environment.

## What is inside

| File | What it is |
|---|---|
| `requirements.txt` | Three old, pinned versions: `requests==2.19.1`, `PyYAML==5.3`, `urllib3==1.23` |
| `app.py` | Ten lines: read `config.yaml`, download one page with `requests` |
| `config.yaml` | The settings `app.py` reads |
| `.gitignore` | Keeps `.env` (secrets) and `.venv/` out of Git |
| `LICENSE` | MIT |

## Check it (the lab)

Inside your own virtual environment:

```bash
pip install pip-audit==2.10.1
pip-audit -r requirements.txt
```

It takes about a minute or more: it finds every library these three lines would bring in.

Read each row: package, version, advisory ID, and the version that fixes it.
One name in the output (`idna`) is not in `requirements.txt` - `requests` brings it in.
Then open one ID on <https://osv.dev> and compare.

## How it would be fixed

Move each line to a version that is newer than every "Fix Versions" value,
then run the program and the tests again. The course whitelist versions
(`requests==2.34.2`, `PyYAML==6.0.3`), with `urllib3==2.8.0`, already pass the same check.
