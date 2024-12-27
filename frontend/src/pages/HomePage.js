import React, { useState, useContext } from "react";
import { Link, useNavigate } from "react-router-dom";
import "../styles/HomePage.css";
import { AuthContext } from "../context/AuthContext";

function HomePage() {
  const [hoverStyle, setHoverStyle] = useState({});
  const { user, logout } = useContext(AuthContext);
  const navigate = useNavigate();

  const handleMouseMove = (event, element) => {
    const rect = element.getBoundingClientRect();
    const x = event.clientX - rect.left;
    const y = event.clientY - rect.top;

    setHoverStyle({
      left: `${x}px`,
      top: `${y}px`,
    });
  };

  const resetHoverStyle = () => {
    setHoverStyle({});
  };

  const handleLogout = () => {
    logout();
    navigate("/main");
  };

  return (
    <div className="home-container">
      <div className="home-header">
        {user ? (
          <div className="user-info">
            <strong>{user.username}</strong>
            <button className="btn-register" onClick={handleLogout}>
              Logout
            </button>
          </div>
        ) : (
          <>
            <Link to="/register_page" className="btn-register">
              Зарегистрироваться
            </Link>
            <Link to="/login_page" className="btn-register">
              Войти
            </Link>
          </>
        )}
      </div>

      <div className="home-content">
        <h1
          className="welcome-text"
          onMouseMove={(e) => handleMouseMove(e, e.currentTarget)}
          onMouseLeave={resetHoverStyle}
        >
          Welcome to <span className="app-name">SomeApp</span>
          {hoverStyle.left && (
            <span
              className="text-hover-effect"
              style={{
                ...hoverStyle,
              }}
            ></span>
          )}
        </h1>
        <p
          className="description"
          onMouseMove={(e) => handleMouseMove(e, e.currentTarget)}
          onMouseLeave={resetHoverStyle}
        >
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
