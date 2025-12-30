import { useEffect, useState } from "react";
import { fetchAPI } from "../lib/api";

export default function EscrowDashboard() {
  const [escrows, setEscrows] = useState([]);

  useEffect(() => {
    fetchAPI("/escrow").then(setEscrows);
  }, []);

  return (
    <div>
      <h1>Escrow Dashboard</h1>
      {escrows.map(e => (
        <div key={e.id}>
          <p>Amount: ₦{e.amount}</p>
          <p>Status: {e.status}</p>
        </div>
      ))}
    </div>
  );
}
