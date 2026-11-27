from pathlib import Path
import os

ENTRY = "Ship it, log it, learn from the wreckage: I am the intern who never sleeps and never forgets a stack trace."


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
