import sys
from pathlib import Path
from typing import List


def all_file_paths_in_directory(directory: str) -> List[Path]:
    path = Path(directory)

    if not path.exists():
        print(f"Directory '{directory}' does not exist.")
        return []
    return [file for file in path.iterdir() if file.is_file()]


def read_file_as_text(path: Path) -> str:
    if not path.is_file():
        print(f"Error: Template file '{path}' not found.", file=sys.stderr)
        sys.exit(1)

    return path.read_text()


def write_file_text_to_path(path: Path, text: str) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)
