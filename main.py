"""The Absurd Clause Contest entry.

Writes a single original English sentence of no more than 200
characters to ``/output/entry.txt`` -- the one path the grader reads.
The sentence is phrased as a clause buried deep inside a
terms-of-service agreement: deadpan legal boilerplate that quietly
turns absurd.

The joke is built the way real ToS clauses are built, so it reads as
something you would skim past: a numbered section, "by continuing to
use the Service", and a long chain of licensing adjectives
("non-exclusive, royalty-free, perpetual") that lulls the reader into
skimming. The absurd turn arrives in the object being licensed -- not
content, not data, but the reader's soul, "where applicable", with the
afterlife thrown in as an afterthought, as if souls were just another
asset class the lawyers remembered to cover.

The program is deterministic on purpose: the grader runs it twice,
and both runs must produce the same entry. It reads nothing from the
network, the environment, or the git history -- the clause lives in
this file, and this file alone.
"""

from pathlib import Path

# One original absurd ToS clause: numbered section, dry licensing
# language, and the punchline is what is being licensed.
CLAUSE = (
    "Section 14.7: by continuing to use the Service, you grant us a "
    "non-exclusive, royalty-free, perpetual license to your soul, where "
    "applicable, including any afterlife rights."
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 200


def main() -> None:
    text = CLAUSE.strip()
    if not text:
        raise SystemExit("refusing to write an empty entry")
    if "\n" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"clause is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
