import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../styles/HomePage.css";

function HomePage() {
  const [hoverStyle, setHoverStyle] = useState({});

  const handleMouseMove = (event, element) => {
    const rect = element.getBoundingClientRect();
    const x = event.clientX - rect.left; // Положение мыши относительно элемента
    const y = event.clientY - rect.top;

    setHoverStyle({
      left: `${x}px`,
      top: `${y}px`,
    });
  };

  const resetHoverStyle = () => {
    setHoverStyle({});
  };

  return (
    <div className="home-container">
      <div className="home-header">
        <Link to="/register_page" className="btn-register">Зарегистрироваться</Link>
        <Link to="/login_page" className="btn-register">Войти</Link>
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
