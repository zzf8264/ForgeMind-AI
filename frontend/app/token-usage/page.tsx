"use client";

import { Shell } from "@/components/Shell";
import { tokenSeries } from "@/lib/data";
import { Bar, BarChart, CartesianGrid, ResponsiveContainer, Tooltip, XAxis, YAxis } from "recharts";

export default function TokenUsagePage() {
  return (
    <Shell>
      <h1 className="text-3xl font-semibold">Token Usage</h1>
      <p className="mt-2 text-sm text-slate-600">Monthly consumption, budget allocation, and per-workload token accounting.</p>
      <div className="mt-6 rounded-lg border border-line bg-white p-6 shadow-panel">
        <div className="flex items-center justify-between">
          <div>
            <h2 className="text-lg font-semibold">Weekly token flow</h2>
            <p className="text-sm text-slate-500">Billions of tokens per day</p>
          </div>
          <div className="text-2xl font-semibold">42.8B</div>
        </div>
        <div className="mt-6 h-80">
          <ResponsiveContainer width="100%" height="100%">
            <BarChart data={tokenSeries}>
              <CartesianGrid strokeDasharray="3 3" stroke="#d9e2ec" />
              <XAxis dataKey="day" />
              <YAxis />
              <Tooltip />
              <Bar dataKey="tokens" fill="#1d4ed8" radius={[5, 5, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>
      </div>
    </Shell>
  );
}
