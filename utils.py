from datetime import datetime
import importlib
import json
from pathlib import Path
import time


def get_input_path(year: int, day: int, part: int) -> Path:
    base = Path(f"aoc/{year}/inputs")
    specific = base / f"day{day:02d}_part{part}.txt"
    shared = base / f"day{day:02d}.txt"

    if specific.exists():
        return specific
    if shared.exists():
        return shared

    raise FileNotFoundError(f"No input found for year={year}, day={day}, part={part}")


def get_metadata_path(year: int, day: int) -> Path:
    path = Path(f"aoc/{year}/metadata")
    path.mkdir(parents=True, exist_ok=True)
    return path / f"day{day:02d}.json"


def update_metadata(
    year: int, day: int, part: int, result: int, runtime_ms: float
) -> None:
    meta_path = get_metadata_path(year, day)
    data = {}

    if meta_path.exists():
        try:
            data = json.loads(meta_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            data = {}

    part_key = f"part{part}"
    data[part_key] = {
        "result": result,
        "runtime_ms": round(runtime_ms, 2),
        "last_run": datetime.now().isoformat(timespec="seconds"),
    }

    meta_path.write_text(json.dumps(data, indent=2), encoding="utf-8")

    print(f"Metadata updated ({part_key}): {meta_path}")


def run_solver(year: int, day: int, part: int) -> None:
    module_name = f"aoc.{year}.solutions.day{day:02d}_part{part}"
    try:
        solver = importlib.import_module(module_name)
    except ModuleNotFoundError:
        print(f"Solver module not found: {module_name}")
        return

    input_path = get_input_path(year, day, part)
    with open(input_path, encoding="utf-8") as f:
        data = f.read().splitlines()

    print(f"Input: {input_path}")
    print(f"Running {module_name}.solve({len(data)} lines)")

    start = time.perf_counter()

    try:
        result = solver.solve(data)
    except Exception as e:
        print(f"Solver crashed: {e}")
        end = time.perf_counter()
        runtime_ms = (end - start) * 1000
        print(f"Runtime before crash: {runtime_ms:.2f} ms")
        return

    end = time.perf_counter()
    runtime_ms = (end - start) * 1000
    print(f"Result: {result} | Time: {runtime_ms:.2f} ms")

    update_metadata(year, day, part, result, runtime_ms)
