def repositories_snapshot() -> dict:
    return {
        "repositories": [
            {"name": "acme/platform", "language": "TypeScript", "indexed_files": 48200, "risk": "medium", "last_indexed": "2026-05-26T07:10:00Z"},
            {"name": "acme/payments", "language": "Python", "indexed_files": 31880, "risk": "high", "last_indexed": "2026-05-26T06:42:00Z"},
            {"name": "acme/infra", "language": "HCL", "indexed_files": 9450, "risk": "low", "last_indexed": "2026-05-25T22:15:00Z"},
        ],
        "indexing": {"status": "healthy", "vector_db": "qdrant", "collections": 128, "embeddings": 72_400_000},
    }
