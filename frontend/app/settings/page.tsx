import { Shell } from "@/components/Shell";

export default function SettingsPage() {
  return (
    <Shell>
      <h1 className="text-3xl font-semibold">Settings</h1>
      <p className="mt-2 text-sm text-slate-600">Enterprise controls for auth, regions, sandbox policy, model routing, and usage budgets.</p>
      <div className="mt-6 grid gap-5 lg:grid-cols-2">
        {[
          ["Authentication", "JWT sessions, SSO-ready identity boundaries, role based access control."],
          ["Model Routing", "Policy based model selection for coding, review, indexing, and documentation."],
          ["Sandbox Execution", "Terminal isolation, audit logs, resource limits, and network controls."],
          ["Multi-region", "Active-active deployment support for us-east-1, eu-west-1, and ap-southeast-1."]
        ].map(([title, body]) => (
          <div key={title} className="rounded-lg border border-line bg-white p-6 shadow-panel">
            <h2 className="text-lg font-semibold">{title}</h2>
            <p className="mt-2 text-sm text-slate-600">{body}</p>
          </div>
        ))}
      </div>
    </Shell>
  );
}
