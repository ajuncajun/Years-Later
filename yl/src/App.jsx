import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Navbar from "./components/Navbar";
import Home from "./pages/Home";
import FindTrips from "./pages/FindTrips";
import TripDetail from "./pages/TripDetail";
import PlanTrip from "./pages/PlanTrip";
import Favorites from "./pages/Favorites";
import Login from "./pages/Login";

function App() {
  return (
    <Router>
      <Navbar />
      <div style={{ padding: 20 }}>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/find-trips" element={<FindTrips />} />
          <Route path="/trip/:id" element={<TripDetail />} />
          <Route path="/plan-trip/:planId" element={<PlanTrip />} />
          <Route path="/favorites" element={<Favorites />} />
          <Route path="/login" element={<Login />} />
          <Route path="*" element={<div>Page Not Found</div>} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
