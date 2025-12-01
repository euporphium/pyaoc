import argparse
import sys
from utils import run_solver


def main():
    parser = argparse.ArgumentParser(description="Advent of Code Solver")
    parser.add_argument(
        "--year",
        type=int,
        default=2025,
        help="Year of the Advent of Code (default: 2025)",
    )

    parser.add_argument("day", type=int, help="Day of the challenge")

    parser.add_argument(
        "part", type=int, choices=[1, 2], help="Which part to run (1 or 2)"
    )

    args = parser.parse_args()

    max_day = 12 if args.year >= 2025 else 25

    if not (1 <= args.day <= max_day):
        sys.exit(f"Error: day must be between 1 and {max_day} for {args.year}")

    print(f"Running AoC {args.year} - Day {args.day}, Part {args.part}")

    run_solver(args.year, args.day, args.part)


if __name__ == "__main__":
    main()
