from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, PointStruct, VectorParams


class VectorStore:
    def __init__(self, url: str = "http://localhost:6333", collection: str = "forgemind_repository_context") -> None:
        self.client = QdrantClient(url=url)
        self.collection = collection

    def ensure_collection(self, dimensions: int = 384) -> None:
        collections = [item.name for item in self.client.get_collections().collections]
        if self.collection not in collections:
            self.client.create_collection(
                collection_name=self.collection,
                vectors_config=VectorParams(size=dimensions, distance=Distance.COSINE),
            )

    def upsert(self, documents: list[dict]) -> None:
        points = [
            PointStruct(
                id=index,
                vector=document["embedding"],
                payload={"path": document["path"], "offset": document["offset"], "content": document["content"][:2000]},
            )
            for index, document in enumerate(documents)
        ]
        self.client.upsert(collection_name=self.collection, points=points)
