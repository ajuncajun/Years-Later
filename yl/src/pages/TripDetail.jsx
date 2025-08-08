import React, { useEffect, useState } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";

export default function TripDetail() {
  const { id } = useParams();
  const [trip, setTrip] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get(`http://127.0.0.1:5000/api/trips/${id}`)
      .then(res => {
        setTrip(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <p>Loading trip details...</p>;
  if (!trip) return <p>Trip not found</p>;

  return (
    <div style={{ padding: 20 }}>
      <h2>{trip.name}</h2>
      <img src={trip.image_url} alt={trip.name} style={{ width: "100%", maxHeight: 400, objectFit: "cover" }} />
      <p><strong>Location:</strong> {trip.location}</p>
      <p><strong>Cost:</strong> ${trip.cost}</p>
      <p>{trip.description}</p>
      {/* Add buttons for 'Add to Plan' or 'Book' here */}
    </div>
  );
}
