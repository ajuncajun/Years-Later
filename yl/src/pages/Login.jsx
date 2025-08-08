import React, { useState, useContext } from "react";
import { AuthContext } from "../contexts/AuthContext";
import { useNavigate } from "react-router-dom";

export default function Login() {
  const { user, login } = useContext(AuthContext);
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const result = await login(email, password);
    if (result.success) {
      navigate("/"); // redirect after login
    } else {
      setError(result.message);
    }
  };

  if (user) return <p>You are already logged in.</p>;

  return (
    <div style={{ maxWidth: 400, margin: "auto" }}>
      <h2>Login</h2>
      <form onSubmit={handleSubmit}>
        <label>Email</label><br />
        <input type="email" required value={email} onChange={(e) => setEmail(e.target.value)} /><br />
        <label>Password</label><br />
        <input type="password" required value={password} onChange={(e) => setPassword(e.target.value)} /><br />
        <button type="submit" style={{ marginTop: 10 }}>Login</button>
      </form>
      {error && <p style={{color: "red"}}>{error}</p>}
    </div>
  );
}
