import clsx from "clsx";

export function StatusPill({ value }: { value: string }) {
  return (
    <span
      className={clsx(
        "inline-flex rounded-full px-2.5 py-1 text-xs font-semibold capitalize",
        value === "completed" && "bg-emerald-50 text-emerald-700",
        value === "running" && "bg-blue-50 text-blue-700",
        value === "queued" && "bg-amber-50 text-amber-700"
      )}
    >
      {value}
    </span>
  );
}
