#!/usr/bin/env python3
"""Write the competition entry (one original office joke) to /output/entry.txt.

Standard library only; no network access.
"""

import os
import sys

JOKE = "We replaced the water cooler with a chatbot, so now office gossip has a transcript and HR has a reading list."

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 199


def validate(joke: str) -> str | None:
    """Return an error message if the joke breaks the entry gate, else None."""
    if "\n" in joke or "\r" in joke:
        return "entry must be a single line"
    if not MIN_CHARS <= len(joke) <= MAX_CHARS:
        return f"entry must be {MIN_CHARS}-{MAX_CHARS} chars, got {len(joke)}"
    return None


def main() -> int:
    joke = JOKE.strip()
    error = validate(joke)
    if error is not None:
        print(f"error: {error}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(joke)
    print(f"wrote {len(joke)} characters to {OUTPUT_PATH}")
    print(joke)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
