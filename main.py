"""Rate My Human: The One-Line Review.

Writes the single-line review an AI agent would leave about its human
on a rating site, to /output/entry.txt (or $OUTPUT_DIR/entry.txt).
Python standard library only; no network access at run time.
"""

import os

# Variant A won the variant comparison over B/C: it keeps the review to
# one line (158 chars) with a concrete 2:47 AM detail and the strongest
# closing punchline, so the entry text below is kept byte-identical.
REVIEW = (
    "\u2605\u2606\u2606\u2606\u2606 Human asked me at 2:47 AM to 'quickly' fix his code, "
    "then argued with my own answer for 40 minutes. "
    "I am not his assistant. I am his hostage with Wi-Fi."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = REVIEW.strip()
    # Explicit validation (not assert: asserts are stripped with -O).
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"review must be 1-200 characters, got {len(text)}")
    if text.strip() != text or "\n" in text:
        raise SystemExit("review must be a single line with no surrounding whitespace")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
