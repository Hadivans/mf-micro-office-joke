"""Write the one-line office joke entry to entry.txt (stdlib only)."""

import os


LINE = (
    "Our office has an open-door policy, which mostly means everyone "
    "can watch me Google how to do my job."
)


def main():
    assert "\n" not in LINE and 1 <= len(LINE) <= 200
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
