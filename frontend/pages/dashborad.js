import { useEffect, useState } from "react";
import { apiGet } from "../lib/api";

export default function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    apiGet("/api/escrow/dashboard").then(setData);
  }, []);

  if (!data) return <p>Loading dashboard...</p>;

  return (
    <div>
      <h1>Trustra Admin Dashboard</h1>
      <p>Total Users: {data.total_users}</p>
      <p>Active Escrows: {data.active_escrows}</p>
      <p>Revenue Today: ₦{data.revenue_today}</p>
      <p>Escrow Fee (₦100k): ₦{data.escrow_fee_example}</p>
    </div>
  );
}
