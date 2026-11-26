"""Write the one-line weather forecast for Cloudgap to /output/entry.txt and verify it."""

ENTRY = "Cloudgap: sunny intervals today, except directly overhead, where the sky has gone missing since Tuesday."

OUTPUT_PATHS = ["/output/entry.txt", "./output/entry.txt"]


def main() -> None:
    assert 1 <= len(ENTRY) <= 120, "entry must be 1-120 characters"
    assert ENTRY.strip(), "entry must not be only whitespace"

    written_path = None
    last_error = None
    for path in OUTPUT_PATHS:
        try:
            with open(path, "w", encoding="utf-8") as f:
                f.write(ENTRY)
            written_path = path
            break
        except OSError as exc:  # e.g. /output not writable; try the fallback
            last_error = exc
    if written_path is None:
        raise RuntimeError(f"could not write entry: {last_error}")

    with open(written_path, "r", encoding="utf-8") as f:
        read_back = f.read()
    assert read_back == ENTRY, "round-trip mismatch"

    print(ENTRY)
    print(f"characters: {len(ENTRY)}")
    print(f"wrote: {written_path}")


if __name__ == "__main__":
    main()
