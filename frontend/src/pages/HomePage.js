import React from "react";
import { Link } from "react-router-dom";
import '../styles/HomePage.css';

function HomePage() {
  return (
    <div className="home-container">
      <div className="home-header">
        <Link to="/register_page" className="btn-register">Go to Register</Link>
        <Link to="/users_list" className="btn-users">User List</Link>
      </div>

      <div className="home-content">
        <h1 className="welcome-text">Welcome to <span className="app-name">SomeApp</span></h1>
        <p className="description">
          We are creating something for you
        </p>
      </div>

      <div className="animation">
        <div className="ball"></div>
        <div className="ball"></div>
        <div className="ball"></div>
      </div>
    </div>
  );
}

export default HomePage;
