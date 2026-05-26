def usage_snapshot() -> dict:
    return {
        "monthly_tokens": 42_800_000_000,
        "daily_agent_runs": 186_000,
        "active_repositories": 128,
        "monthly_spend_usd": 18_420,
        "concurrent_tasks": 3_200,
        "p95_latency_ms": 1280,
        "regions": ["us-east-1", "eu-west-1", "ap-southeast-1"],
        "token_breakdown": [
            {"label": "code_generation", "tokens": 15_200_000_000},
            {"label": "repository_indexing", "tokens": 11_600_000_000},
            {"label": "review_and_security", "tokens": 8_900_000_000},
            {"label": "documentation", "tokens": 7_100_000_000},
        ],
    }
