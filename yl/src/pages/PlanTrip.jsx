import React, { useState, useEffect, useContext } from "react";
import axios from "axios";
import { useParams } from "react-router-dom";
import { AuthContext } from "../contexts/AuthContext";

export default function PlanTrip() {
  const { user } = useContext(AuthContext);
  const { planId } = useParams();
  const [plan, setPlan] = useState(null);
  const [items, setItems] = useState([]);
  const [comments, setComments] = useState([]);
  const [newItem, setNewItem] = useState({ title: "", price: "", notes: "" });
  const [newComment, setNewComment] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    if (!planId) {
      setLoading(false);
      return;
    }
    axios.get(`http://127.0.0.1:5000/api/plans/${planId}`)
      .then(res => {
        setPlan(res.data.plan);
        setItems(res.data.items || []);
        setComments(res.data.comments || []);
        setLoading(false);
      })
      .catch(err => {
        console.error(err);
        setLoading(false);
      });
  }, [planId]);

  const addItem = async (e) => {
    e.preventDefault();
    if (!user) return alert("Please login to add items.");
    if (!newItem.title) return alert("Item title required");

    try {
      await axios.post(`http://127.0.0.1:5000/api/plans/${planId}/items`, {
        ...newItem,
        created_by: user.id
      });
      setItems(prev => [...prev, { ...newItem, id: Date.now(), created_by: user.id }]);
      setNewItem({ title: "", price: "", notes: "" });
    } catch (error) {
      alert("Failed to add item");
      console.error(error);
    }
  };

  const addComment = async (e) => {
    e.preventDefault();
    if (!user) return alert("Please login to comment.");
    if (!newComment.trim()) return alert("Comment cannot be empty.");

    try {
      await axios.post(`http://127.0.0.1:5000/api/comments`, {
        plan_id: planId,
        user_id: user.id,
        comment: newComment.trim(),
      });
      setComments(prev => [...prev, { comment: newComment.trim(), user_id: user.id, id: Date.now() }]);
      setNewComment("");
    } catch (error) {
      alert("Failed to add comment");
      console.error(error);
    }
  };

  if (loading) return <p>Loading plan...</p>;
  if (!plan) return <p>No plan selected or plan not found.</p>;

  return (
    <div>
      <h2>{plan.title}</h2>
      <p><strong>Budget:</strong> ${plan.budget || "N/A"}</p>

      <h3>Plan Items</h3>
      <ul>
        {items.length === 0 ? <li>No items added yet.</li> :
          items.map(item => (
            <li key={item.id}>
              <strong>{item.title}</strong> - ${item.price} <br />
              Notes: {item.notes || "None"}
            </li>
          ))
        }
      </ul>

      <form onSubmit={addItem}>
        <h4>Add Item</h4>
        <input
          type="text"
          placeholder="Title"
          value={newItem.title}
          onChange={(e) => setNewItem(prev => ({ ...prev, title: e.target.value }))}
          required
        /><br />
        <input
          type="number"
          placeholder="Price"
          value={newItem.price}
          onChange={(e) => setNewItem(prev => ({ ...prev, price: e.target.value }))}
        /><br />
        <textarea
          placeholder="Notes"
          value={newItem.notes}
          onChange={(e) => setNewItem(prev => ({ ...prev, notes: e.target.value }))}
        /><br />
        <button type="submit">Add Item</button>
      </form>

      <h3>Comments</h3>
      <ul>
        {comments.length === 0 ? <li>No comments yet.</li> :
          comments.map(c => (
            <li key={c.id}>
              <strong>User {c.user_id}:</strong> {c.comment}
            </li>
          ))
        }
      </ul>

      <form onSubmit={addComment}>
        <h4>Add Comment</h4>
        <textarea
          value={newComment}
          onChange={(e) => setNewComment(e.target.value)}
          required
        /><br />
        <button type="submit">Add Comment</button>
      </form>
    </div>
  );
}
