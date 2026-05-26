import { Shell } from "@/components/Shell";
import { repositories } from "@/lib/data";

export default function RepositoriesPage() {
  return (
    <Shell>
      <h1 className="text-3xl font-semibold">Repositories</h1>
      <p className="mt-2 text-sm text-slate-600">Long-context indexing status, ownership mapping, and risk posture for connected GitHub repositories.</p>
      <div className="mt-6 overflow-hidden rounded-lg border border-line bg-white shadow-panel">
        <table className="w-full text-left text-sm">
          <thead className="bg-slate-50 text-xs uppercase text-slate-500">
            <tr><th className="px-5 py-3">Repository</th><th>Language</th><th>Indexed Files</th><th>Risk</th><th>Last Indexed</th></tr>
          </thead>
          <tbody className="divide-y divide-line">
            {repositories.map((repo) => (
              <tr key={repo.name}>
                <td className="px-5 py-4 font-semibold">{repo.name}</td>
                <td>{repo.language}</td>
                <td>{repo.files}</td>
                <td>{repo.risk}</td>
                <td>{repo.indexed}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </Shell>
  );
}
