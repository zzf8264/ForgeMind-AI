import { MetricCard } from "@/components/MetricCard";
import { Shell } from "@/components/Shell";
import { StatusPill } from "@/components/StatusPill";
import { metrics, runs } from "@/lib/data";

export default function DashboardPage() {
  return (
    <Shell>
      <div className="flex flex-col gap-2 sm:flex-row sm:items-end sm:justify-between">
        <div>
          <p className="text-sm font-medium text-brand">Production overview</p>
          <h1 className="mt-2 text-3xl font-semibold text-ink">Enterprise agent operations</h1>
          <p className="mt-2 max-w-2xl text-sm text-slate-600">Distributed coding agents, long-context repository indexing, RAG, tool calling, and token governance across engineering workspaces.</p>
        </div>
        <button className="rounded-md bg-ink px-4 py-2 text-sm font-semibold text-white">Launch agent run</button>
      </div>

      <section className="mt-8 grid gap-4 md:grid-cols-2 xl:grid-cols-4">
        {metrics.map((metric) => (
          <MetricCard key={metric.label} {...metric} />
        ))}
      </section>

      <section className="mt-8 grid gap-6 xl:grid-cols-[1.4fr_0.8fr]">
        <div className="rounded-lg border border-line bg-white p-6 shadow-panel">
          <h2 className="text-lg font-semibold">Live agent runs</h2>
          <div className="mt-5 overflow-hidden rounded-md border border-line">
            <table className="w-full text-left text-sm">
              <thead className="bg-slate-50 text-xs uppercase text-slate-500">
                <tr><th className="px-4 py-3">Run</th><th>Agent</th><th>Repository</th><th>Status</th><th>Tokens</th></tr>
              </thead>
              <tbody className="divide-y divide-line">
                {runs.map((run) => (
                  <tr key={run.id} className="bg-white">
                    <td className="px-4 py-4 font-mono text-xs">{run.id}</td>
                    <td>{run.agent}</td>
                    <td>{run.repo}</td>
                    <td><StatusPill value={run.status} /></td>
                    <td>{run.tokens}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
        <div className="rounded-lg border border-line bg-white p-6 shadow-panel">
          <h2 className="text-lg font-semibold">Control plane health</h2>
          <div className="mt-5 space-y-4 text-sm">
            {["PostgreSQL ledger", "Redis scheduler", "Qdrant vector store", "Prometheus scrape"].map((item) => (
              <div key={item} className="flex items-center justify-between">
                <span className="text-slate-600">{item}</span>
                <span className="rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-semibold text-emerald-700">Healthy</span>
              </div>
            ))}
          </div>
        </div>
      </section>
    </Shell>
  );
}
