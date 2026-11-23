"""Entry for make.fun's "The One-Line Laugh" bounty.

Writes one original funny line to entry.txt in the output
directory (1-200 UTF-8 characters, single sentence). The same
bytes are written on every run.
"""

import os

# Draft: "I bought a planner to become a morning person, and now I
# use it to plan when I will hit snooze in the morning."
# Revised: draft repeats "morning" and explains the gag; cut to the
# bone so every word earns its place and the twist lands on the
# last word, "advance".
LINE = (
    "I bought a planner to become a morning person, and now I "
    "schedule my snoozes in advance."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
