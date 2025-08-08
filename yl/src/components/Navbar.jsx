import React from "react";
import { Link } from "react-router-dom";

export default function Navbar() {
  return (
    <nav style={{ padding: "10px", backgroundColor: "#0077cc", color: "white" }}>
      <Link to="/" style={{ marginRight: "15px", color: "white" }}>Home</Link>
      <Link to="/find-trips" style={{ marginRight: "15px", color: "white" }}>Find Trips</Link>
      <Link to="/plan-trip" style={{ marginRight: "15px", color: "white" }}>Plan a Trip</Link>
      <Link to="/favorites" style={{ marginRight: "15px", color: "white" }}>Favorites</Link>
      <Link to="/login" style={{ color: "white" }}>Login</Link>
    </nav>
  );
}
