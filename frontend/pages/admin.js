import { useEffect, useState } from "react";
import { getToken } from "../lib/auth";

export default function Admin() {
  const [cases, setCases] = useState([]);

  useEffect(() => {
    fetch(`${process.env.NEXT_PUBLIC_API}/admin/risk`, {
      headers: { Authorization: `Bearer ${getToken()}` }
    })
      .then(res => res.json())
      .then(setCases);
  }, []);

  return (
    <div>
      <h1>Admin Risk Dashboard</h1>
      {cases.map(c => (
        <div key={c.id}>Escrow #{c.id} – ₦{c.amount}</div>
      ))}
    </div>
  );
}

