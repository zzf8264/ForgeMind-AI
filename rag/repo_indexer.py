from pathlib import Path


class RepositoryIndexer:
    def __init__(self, root: str, include_suffixes: tuple[str, ...] = (".py", ".ts", ".tsx", ".go", ".java", ".md")) -> None:
        self.root = Path(root)
        self.include_suffixes = include_suffixes

    def discover_files(self) -> list[Path]:
        ignored = {".git", "node_modules", ".next", "__pycache__", "dist", "build"}
        files: list[Path] = []
        for path in self.root.rglob("*"):
            if any(part in ignored for part in path.parts):
                continue
            if path.is_file() and path.suffix in self.include_suffixes:
                files.append(path)
        return files

    def chunk_file(self, path: Path, chunk_size: int = 1800, overlap: int = 180) -> list[dict]:
        text = path.read_text(encoding="utf-8", errors="ignore")
        chunks = []
        cursor = 0
        while cursor < len(text):
            content = text[cursor : cursor + chunk_size]
            chunks.append({"path": str(path), "offset": cursor, "content": content})
            cursor += max(1, chunk_size - overlap)
        return chunks
