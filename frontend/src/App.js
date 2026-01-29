import React, { useState } from "react";
import axios from "axios";

function App() {
  const [junction, setJunction] = useState("");
  const [id, setId] = useState("");
  const [hour, setHour] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const res = await axios.post("/predict", {
        Junction: Number(junction),
        ID: Number(id),
        hour: Number(hour),
      });

      setResult(res.data.predicted_vehicles);
    } catch (err) {
      console.error(err);
      alert("API Error. Is Flask running?");
    }
  };

  return (
    <div style={styles.container}>
      <h1>🚦 Smart City Traffic Predictor</h1>

      <form onSubmit={handleSubmit} style={styles.form}>
        <input
          type="number"
          placeholder="Junction"
          value={junction}
          onChange={(e) => setJunction(e.target.value)}
          required
        />

        <input
          type="number"
          placeholder="ID"
          value={id}
          onChange={(e) => setId(e.target.value)}
          required
        />

        <input
          type="number"
          placeholder="Hour (0-23)"
          value={hour}
          onChange={(e) => setHour(e.target.value)}
          required
        />

        <button type="submit">Predict</button>
      </form>

      {result !== null && (
        <h2>🚗 Predicted Vehicles: {result}</h2>
      )}
    </div>
  );
}

const styles = {
  container: {
    textAlign: "center",
    marginTop: "80px",
    fontFamily: "Arial",
  },

  form: {
    display: "inline-flex",
    flexDirection: "column",
    gap: "12px",
    width: "250px",
  },
};

export default App;
