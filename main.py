import hashlib
import os
from pathlib import Path

LINE = "One star. His lap closes without warning, has no warranty, and evicted me mid-nap for a snack run."

CHAR_LIMIT = 200


def validate() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    path = out_dir / "entry.txt"
    data = path.read_bytes()
    text = data.decode("utf-8")
    assert text == LINE, "entry.txt content does not match LINE"
    assert 1 <= len(text) <= CHAR_LIMIT, "entry.txt must be 1-200 characters"
    assert "\n" not in text, "entry.txt must be a single line"
    assert "\r" not in text, "entry.txt must not contain a carriage return"
    assert not data.endswith(b"\n"), "entry.txt must not end with a newline"
    assert text == text.strip(), "entry.txt must not have leading/trailing whitespace"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "out"))
    out_dir.mkdir(parents=True, exist_ok=True)
    data = LINE.encode("utf-8")
    (out_dir / "entry.txt").write_bytes(data)
    validate()
    print(hashlib.sha256(data).hexdigest())


if __name__ == "__main__":
    main()
