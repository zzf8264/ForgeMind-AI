from datetime import date

RUNS = [
    ("run_8b11", "CodingAgent", "acme/platform", "running", 840210),
    ("run_7f92", "RepoAnalyzerAgent", "acme/payments", "completed", 1284300),
    ("run_4aa0", "ReviewAgent", "acme/mobile", "queued", 0),
]


def main() -> None:
    print("ForgeMind AI demo seed preview")
    print(f"usage_date={date.today().isoformat()}")
    for run in RUNS:
        print({"id": run[0], "agent": run[1], "repository": run[2], "status": run[3], "tokens": run[4]})


if __name__ == "__main__":
    main()
