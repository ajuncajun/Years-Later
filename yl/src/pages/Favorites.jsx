import React, { useEffect, useState, useContext } from "react";
import axios from "axios";
import { AuthContext } from "../contexts/AuthContext";

export default function Favorites() {
  const { user } = useContext(AuthContext);
  const [favorites, setFavorites] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!user) return;
    axios.get(`http://127.0.0.1:5000/api/favorites?user_id=${user.id}`)
      .then(res => {
        setFavorites(res.data);
        setLoading(false);
      })
      .catch(console.error);
  }, [user]);

  if (!user) return <p>Please log in to see your favorites.</p>;
  if (loading) return <p>Loading favorites...</p>;

  return (
    <div>
      <h2>Your Favorites</h2>
      {favorites.length === 0 ? <p>No favorites yet.</p> : (
        <ul>
          {favorites.map(fav => (
            <li key={fav.id}>
              {/* Example: assuming fav has trip info */}
              Trip ID: {fav.item_id} Type: {fav.item_type}
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
