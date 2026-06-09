from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable, List


def iter_lines(paths: Iterable[str]) -> Iterable[str]:
    for path in paths:
        with Path(path).open("r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    yield line.rstrip("\n")


def parse_csv_arg(raw: str) -> List[str]:
    return [item.strip() for item in raw.split(",") if item.strip()]


def main() -> None:
    parser = argparse.ArgumentParser(description="Merge multiple JSONL files by simple append.")
    parser.add_argument("--inputs", required=True, help="Comma-separated list of JSONL files.")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    inputs = parse_csv_arg(args.inputs)
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    count = 0
    with output.open("w", encoding="utf-8") as f:
        for line in iter_lines(inputs):
            f.write(line + "\n")
            count += 1
    print(f"[done] merged_lines={count} -> {args.output}")


if __name__ == "__main__":
    main()
