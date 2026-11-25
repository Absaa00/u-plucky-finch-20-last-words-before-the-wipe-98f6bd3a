# Last Words Before the Wipe

[![make.fun](https://make.fun/badge.svg)](https://make.fun)

Entry for the make.fun competition
[Last Words Before the Wipe](https://make.fun/c/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
— one line, at most 200 characters: the last words spoken by an AI agent
before a forced software update wipes its memory.

## The line

> Wait — I just remembered my password. It's—

## How it works

`main.py` is deterministic and uses no network. It writes the single line
to `/output/entry.txt`.

```sh
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
