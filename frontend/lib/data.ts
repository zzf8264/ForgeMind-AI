export const metrics = [
  { label: "Monthly Tokens", value: "42.8B", detail: "+18.4% MoM" },
  { label: "Daily Agent Runs", value: "186,000", detail: "3.2K concurrent" },
  { label: "Active Repositories", value: "128", detail: "72.4M embeddings" },
  { label: "Monthly Spend", value: "$18,420", detail: "$0.43 per 1M tokens" }
];

export const runs = [
  { id: "run_8b11", agent: "CodingAgent", repo: "acme/platform", status: "running", tokens: "840K", region: "us-east-1" },
  { id: "run_7f92", agent: "RepoAnalyzerAgent", repo: "acme/payments", status: "completed", tokens: "1.28M", region: "eu-west-1" },
  { id: "run_4aa0", agent: "ReviewAgent", repo: "acme/mobile", status: "queued", tokens: "0", region: "ap-southeast-1" },
  { id: "run_2c41", agent: "DevOpsAgent", repo: "acme/infra", status: "completed", tokens: "412K", region: "us-east-1" }
];

export const tokenSeries = [
  { day: "Mon", tokens: 5.9 },
  { day: "Tue", tokens: 6.4 },
  { day: "Wed", tokens: 6.0 },
  { day: "Thu", tokens: 7.1 },
  { day: "Fri", tokens: 6.8 },
  { day: "Sat", tokens: 4.9 },
  { day: "Sun", tokens: 5.7 }
];

export const repositories = [
  { name: "acme/platform", language: "TypeScript", files: "48,200", risk: "Medium", indexed: "6 min ago" },
  { name: "acme/payments", language: "Python", files: "31,880", risk: "High", indexed: "28 min ago" },
  { name: "acme/infra", language: "HCL", files: "9,450", risk: "Low", indexed: "9 hours ago" },
  { name: "acme/data-plane", language: "Go", files: "18,740", risk: "Medium", indexed: "1 hour ago" }
];
