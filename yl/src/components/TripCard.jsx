import React from "react";
import { Link } from "react-router-dom";

export default function TripCard({ trip }) {
  return (
    <div style={{ border: "1px solid #ccc", margin: 10, padding: 10, width: 300 }}>
      <img src={trip.image_url} alt={trip.name} style={{ width: "100%", height: 150, objectFit: "cover" }} />
      <h3>{trip.name}</h3>
      <p><strong>Location:</strong> {trip.location}</p>
      <p><strong>Cost:</strong> ${trip.cost}</p>
      <p>{trip.description}</p>
      <Link to={`/trip/${trip.id}`}>View Details</Link>
    </div>
  );
}
