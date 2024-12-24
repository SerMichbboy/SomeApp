import React, { useState, useEffect, useContext } from "react";
import "../styles/LoginPage.css";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

const LoginPage = () => {
  const [identifier, setIdentifier] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const { login } = useContext(AuthContext); // Подключаем функцию login из AuthContext

  const handleGoHome = () => {
    navigate("/");
  };

  const handleKeyPress = (event) => {
    if (event.key === "Escape") {
      handleGoHome();
    }
  };

  useEffect(() => {
    window.addEventListener("keydown", handleKeyPress);
    return () => {
      window.removeEventListener("keydown", handleKeyPress);
    };
  }, []);

  const handleLogin = async (event) => {
    event.preventDefault();

    if (!identifier || !password) {
      alert("Please fill in both fields.");
      return;
    }

    const loginData = {
      username: identifier, // Убедитесь, что бэкенд ожидает это поле.
      password
    };

    try {
      const response = await fetch("http://127.0.0.1:8000/api/token/create/", { // Используем правильный адрес бэкенда.
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(loginData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Login failed");
      }

      const data = await response.json();
      const { access, refresh } = data;

      // Сохраняем токены через AuthContext
      login(access, refresh);

      alert("Login successful!");
      navigate("/main");
    } catch (error) {
      console.error("Error:", error);
      alert(error.message || "Login failed. Please try again.");
    }
  };

  return (
    <div className="login-container">
      <button className="btn-home" onClick={handleGoHome} tabIndex={0}>
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
        <button type="submit" className="btn-login">
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
