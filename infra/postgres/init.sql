CREATE TABLE IF NOT EXISTS agent_runs (
  id TEXT PRIMARY KEY,
  agent TEXT NOT NULL,
  repository TEXT NOT NULL,
  status TEXT NOT NULL,
  tokens BIGINT NOT NULL DEFAULT 0,
  created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE IF NOT EXISTS token_usage_daily (
  id SERIAL PRIMARY KEY,
  usage_date DATE NOT NULL,
  workload TEXT NOT NULL,
  tokens BIGINT NOT NULL,
  spend_usd NUMERIC(12, 2) NOT NULL
);

INSERT INTO token_usage_daily (usage_date, workload, tokens, spend_usd)
VALUES
  (CURRENT_DATE, 'code_generation', 15200000000, 6536.00),
  (CURRENT_DATE, 'repository_indexing', 11600000000, 4988.00),
  (CURRENT_DATE, 'review_and_security', 8900000000, 3827.00)
ON CONFLICT DO NOTHING;
