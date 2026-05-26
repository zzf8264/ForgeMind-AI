from pathlib import Path


def main() -> None:
    root = Path("demo-workspace")
    (root / "services" / "billing").mkdir(parents=True, exist_ok=True)
    (root / "services" / "billing" / "README.md").write_text(
        "# Billing Service\n\nDemo repository used by ForgeMind AI repository indexing examples.\n",
        encoding="utf-8",
    )
    (root / "services" / "billing" / "retry_policy.py").write_text(
        "def retry_delay(attempt: int) -> int:\n    return min(60, 2 ** attempt)\n",
        encoding="utf-8",
    )
    print(f"created {root.resolve()}")


if __name__ == "__main__":
    main()
