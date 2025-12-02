# PyAoC - Advent of Code Solver

Python-based Advent of Code solver with automatic input handling and timing.

## Requirements

- Python 3.14+
- [uv](https://docs.astral.sh/uv/) package manager

## Running Solutions

```bash
# Run a specific day and part
uv run main.py <day> <part>

# Examples
uv run main.py 1 1      # Day 1, Part 1
uv run main.py 1 2      # Day 1, Part 2

# Specify a different year (default: 2025)
uv run main.py --year 2024 1 1
```

## Project Structure

```
aoc/
  2025/
    inputs/          # Puzzle inputs
    metadata/        # Solution results and timing
    solutions/       # Solution files (day01_part1.py, day01_part2.py, etc.)
  2024/
    ...
```

## Creating Solutions

Solutions go in `aoc/<year>/solutions/day<DD>_part<N>.py` and must implement a `solve(data: list[str]) -> int` function.