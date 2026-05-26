import Link from "next/link";
import { Activity, BarChart3, Bot, Database, Gauge, GitBranch, Settings } from "lucide-react";

const nav = [
  { href: "/", label: "Dashboard", icon: Gauge },
  { href: "/agent-runs", label: "Agent Runs", icon: Bot },
  { href: "/token-usage", label: "Token Usage", icon: Activity },
  { href: "/repositories", label: "Repositories", icon: GitBranch },
  { href: "/benchmarks", label: "Benchmarks", icon: BarChart3 },
  { href: "/settings", label: "Settings", icon: Settings }
];

export function Shell({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen">
      <aside className="fixed inset-y-0 left-0 hidden w-72 border-r border-line bg-white px-5 py-6 lg:block">
        <div className="flex items-center gap-3">
          <div className="grid h-10 w-10 place-items-center rounded-lg bg-ink text-white">
            <Database size={20} />
          </div>
          <div>
            <div className="text-lg font-semibold">ForgeMind AI</div>
            <div className="text-xs text-slate-500">Agent Infrastructure Cloud</div>
          </div>
        </div>
        <nav className="mt-10 space-y-1">
          {nav.map((item) => (
            <Link key={item.href} href={item.href} className="flex items-center gap-3 rounded-md px-3 py-2 text-sm font-medium text-slate-700 hover:bg-slate-100">
              <item.icon size={17} />
              {item.label}
            </Link>
          ))}
        </nav>
        <div className="absolute bottom-6 left-5 right-5 rounded-md border border-line bg-slate-50 p-4">
          <div className="text-sm font-semibold">Enterprise Cluster</div>
          <div className="mt-1 text-xs text-slate-500">3 regions, 3,200 concurrent tasks, 99.95% control-plane SLO</div>
        </div>
      </aside>
      <main className="lg:pl-72">
        <div className="mx-auto max-w-7xl px-5 py-6 sm:px-8">{children}</div>
      </main>
    </div>
  );
}
