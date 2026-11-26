"""Cloudgap forecast: write the competition entry line to /output/entry.txt.

The entry is a single weather-forecast line (at most 120 characters) for
Cloudgap, a city that does not exist. This program validates the line,
writes it to the scorer's output path, and reads it back to prove the
round trip is exact.
"""

from pathlib import Path

ENTRY = "Cloudgap: sunny intervals today, except directly overhead, where the sky has gone missing since Tuesday."

MAX_CHARS = 120
CANDIDATE_PATHS = (Path("/output/entry.txt"), Path("output/entry.txt"))


def validate(line: str) -> str:
    """Reject anything the gate would refuse, before writing a byte."""
    if not line.strip():
        raise ValueError("entry must not be only whitespace")
    if len(line) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    if "\n" in line:
        raise ValueError("entry must be a single line")
    return line


def write_entry(line: str) -> Path:
    """Write the line to the first usable output path and confirm it."""
    checked = validate(line)
    for target in CANDIDATE_PATHS:
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(checked, encoding="utf-8")
        except OSError:
            continue
        if target.read_text(encoding="utf-8") != checked:
            raise RuntimeError(f"round-trip mismatch at {target}")
        return target
    raise RuntimeError("no output path was writable")


def main() -> None:
    path = write_entry(ENTRY)
    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"wrote: {path}")


if __name__ == "__main__":
    main()
