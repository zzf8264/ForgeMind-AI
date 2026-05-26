import { Shell } from "@/components/Shell";

const benchmarks = [
  ["Repository indexing", "72.4M chunks/month", "1.8s retrieval p95", "11.6B tokens"],
  ["Autonomous coding", "186K runs/day", "18.4s first plan", "15.2B tokens"],
  ["Review and security", "92K reviews/day", "9.2s first finding", "8.9B tokens"],
  ["Distributed sandbox", "3,200 concurrent tasks", "420ms queue admission", "99.95% SLO"]
];

export default function BenchmarksPage() {
  return (
    <Shell>
      <h1 className="text-3xl font-semibold">Benchmarks</h1>
      <p className="mt-2 text-sm text-slate-600">Capacity planning metrics for multi-agent coding workloads, repository RAG, and distributed sandbox execution.</p>
      <div className="mt-6 grid gap-4">
        {benchmarks.map(([name, throughput, latency, tokens]) => (
          <div key={name} className="grid gap-4 rounded-lg border border-line bg-white p-5 shadow-panel md:grid-cols-4">
            <div className="font-semibold">{name}</div>
            <div className="text-sm text-slate-600">{throughput}</div>
            <div className="text-sm text-slate-600">{latency}</div>
            <div className="text-sm font-medium text-brand">{tokens}</div>
          </div>
        ))}
      </div>
    </Shell>
  );
}
