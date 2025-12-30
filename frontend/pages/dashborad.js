import { useEffect, useState } from "react";
import { fetchAPI } from "../lib/api";
import TrustBadge from "../components/TrustBadge";

export default function Dashboard() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchAPI("/users/1/fraud-risk").then(setData);
  }, []);

  if (!data) return <p>Loading...</p>;

  return (
    <div>
      <h1>User Dashboard</h1>
      <TrustBadge risk={data.fraud_probability} />
      <p>Fraud Risk: {(data.fraud_probability * 100).toFixed(1)}%</p>
    </div>
  );
}
