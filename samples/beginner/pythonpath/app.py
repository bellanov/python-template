"""Display the current PYTHONPATH and sys.path entries."""

import os
import sys


def display_pythonpath() -> None:
    pythonpath = os.environ.get("PYTHONPATH")

    if pythonpath:
        print(f"PYTHONPATH={pythonpath}")
    else:
        print("PYTHONPATH is not set")

    print("\nCurrent sys.path entries:")
    for index, path in enumerate(sys.path, start=1):
        print(f"{index}. {path}")


if __name__ == "__main__":
    display_pythonpath()
