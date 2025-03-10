import React, { useEffect, useState } from "react";

function Dashboard() {
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchDashboard = async () => {
      const token = localStorage.getItem("token");
      const res = await fetch("http://localhost:5000/api/auth/dashboard", {
        headers: { Authorization: token },
      });

      const data = await res.json();
      setMessage(data.message);
    };

    fetchDashboard();
  }, []);

  return <h2>{message}</h2>;
}

export default Dashboard;
