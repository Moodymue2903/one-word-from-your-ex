"""One Word From Your Ex — make.fun entry.

Writes exactly one word — the word the entrant's ex would use to describe
them — to /output/entry.txt.

The word is "Almost": the whole almost-relationship in a single word. Almost
the one, almost enough, almost loved — and never quite any of them. It is a
word an ex would literally say, it lands with no explanation, and its sting
is the near-miss itself rather than an insult. No near-synonym ("nearly",
"close", "almost-there") carries the same edge, which is what the judge's
fourth criterion asks for.

Gate (from the competition kit): /output/entry.txt must be UTF-8 text of
1 to 24 characters, not only whitespace, holding exactly one word.
"""

import os
import sys

# The entry. One word, seven letters, no spaces, no punctuation.
WORD = "Almost"

# Gate limits from the competition kit.
MIN_CHARS = 1
MAX_CHARS = 24

# Default output path inside the grading sandbox.
DEFAULT_OUTPUT = "/output/entry.txt"


def validate_word(word):
    """Check a candidate word against the competition gate.

    Returns the word unchanged when it passes, and raises ValueError with
    a plain explanation when it does not, so a bad word fails loudly
    instead of shipping a disqualified entry.
    """
    if not isinstance(word, str):
        raise ValueError("entry must be text, got %s" % type(word).__name__)
    if word != word.strip():
        raise ValueError("entry must not start or end with whitespace")
    if not MIN_CHARS <= len(word) <= MAX_CHARS:
        raise ValueError(
            "entry must be %d-%d characters, got %d"
            % (MIN_CHARS, MAX_CHARS, len(word))
        )
    if not word.strip():
        raise ValueError("entry must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word, got %r" % word)
    return word


def write_entry(word, output_path):
    """Validate the word and write it to the output path as UTF-8 text."""
    checked = validate_word(word)
    directory = os.path.dirname(output_path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(checked)
    return checked


def main(argv=None):
    """Entry point: write WORD to the output path and confirm on stdout."""
    args = list(sys.argv[1:] if argv is None else argv)
    output_path = args[0] if args else DEFAULT_OUTPUT
    written = write_entry(WORD, output_path)
    print("wrote %r (%d chars) to %s" % (written, len(written), output_path))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
