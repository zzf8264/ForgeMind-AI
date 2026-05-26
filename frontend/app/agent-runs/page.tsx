import { Shell } from "@/components/Shell";
import { StatusPill } from "@/components/StatusPill";
import { runs } from "@/lib/data";

export default function AgentRunsPage() {
  return (
    <Shell>
      <h1 className="text-3xl font-semibold">Agent Runs</h1>
      <p className="mt-2 text-sm text-slate-600">Streaming execution traces from distributed coding, review, repository analysis, documentation, and DevOps agents.</p>
      <div className="mt-6 grid gap-4">
        {runs.map((run) => (
          <div key={run.id} className="rounded-lg border border-line bg-white p-5 shadow-panel">
            <div className="flex flex-wrap items-center justify-between gap-3">
              <div>
                <div className="font-mono text-xs text-slate-500">{run.id}</div>
                <div className="mt-1 text-lg font-semibold">{run.agent}</div>
              </div>
              <StatusPill value={run.status} />
            </div>
            <div className="mt-4 grid gap-3 text-sm text-slate-600 sm:grid-cols-3">
              <div>Repository: {run.repo}</div>
              <div>Region: {run.region}</div>
              <div>Tokens: {run.tokens}</div>
            </div>
          </div>
        ))}
      </div>
    </Shell>
  );
}
