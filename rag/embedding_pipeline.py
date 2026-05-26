import hashlib
import math


class EmbeddingPipeline:
    """Deterministic demo embeddings; replace with provider embeddings in production."""

    def __init__(self, dimensions: int = 384) -> None:
        self.dimensions = dimensions

    def embed(self, text: str) -> list[float]:
        digest = hashlib.sha256(text.encode("utf-8")).digest()
        values = []
        for index in range(self.dimensions):
            byte = digest[index % len(digest)]
            values.append((byte / 255.0) * 2 - 1)
        norm = math.sqrt(sum(value * value for value in values)) or 1
        return [value / norm for value in values]

    def embed_documents(self, chunks: list[dict]) -> list[dict]:
        return [{**chunk, "embedding": self.embed(chunk["content"])} for chunk in chunks]
