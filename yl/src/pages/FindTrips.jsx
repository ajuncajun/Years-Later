import React, { useEffect, useState } from "react";
import axios from "axios";
import TripCard from "../components/TripCard";

export default function FindTrips() {
  const [trips, setTrips] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    axios.get("http://127.0.0.1:5000/api/trips")
      .then(res => {
        setTrips(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading trips...</p>;

  return (
    <div>
      <h2>Find Trips</h2>
      <div style={{ display: "flex", flexWrap: "wrap" }}>
        {trips.length ? trips.map(trip => <TripCard key={trip.id} trip={trip} />) : <p>No trips found</p>}
      </div>
    </div>
  );
}
