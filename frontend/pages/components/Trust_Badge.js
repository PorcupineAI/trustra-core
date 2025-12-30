export default function TrustBadge({ risk }) {
  if (risk < 0.3) return <span>🟢 Trusted</span>;
  if (risk < 0.6) return <span>🟠 Caution</span>;
  return <span>🔴 High Risk</span>;
}
