import React, { useState } from "react";
import "../styles/LoginPage.css";
import {useNavigate} from "react-router-dom"; // Подключаем стили

const LoginPage = () => {
  const [identifier, setIdentifier] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const handleGoHome = () => {
    navigate("/");
  };

  const handleLogin = (event) => {
    event.preventDefault();

    if (!identifier || !password) {
      alert("Please fill in both fields.");
      return;
    }

    const loginData = { identifier, password };

    // Пример отправки данных на сервер
    fetch("/api/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(loginData),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          alert("Login successful!");
          // Перенаправление на другую страницу
          window.location.href = "/dashboard";
        } else {
          alert(data.message || "Login failed. Please try again.");
        }
      })
      .catch((error) => {
        console.error("Error:", error);
        alert("Something went wrong. Please try again later.");
      });
  };


  return (
      <div className="login-container">
        <button className="btn-home" onClick={handleGoHome}>
          Go to Home
        </button>
        <form className="login-form" onSubmit={handleLogin}>
          <input
              type="text"
              className="input-field"
              placeholder="Email, Phone, or Username"
              value={identifier}
              onChange={(e) => setIdentifier(e.target.value)}
              required
          />
          <input
              type="password"
              className="input-field"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
          />
          <button type="submit" className="btn-login">Login</button>
        </form>
      </div>
  );
};

export default LoginPage;
