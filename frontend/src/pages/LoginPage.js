import React, { useState, useEffect } from "react";
import "../styles/LoginPage.css";
import { useNavigate } from "react-router-dom";

const LoginPage = () => {
  const [identifier, setIdentifier] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleGoHome = () => {
    navigate("/");
  };

  const handleKeyPress = (event) => {
    if (event.key === "Escape") {
      handleGoHome();
    }
  };

  // Эффект для добавления обработчика клавиш при монтировании компонента
  useEffect(() => {
    window.addEventListener("keydown", handleKeyPress);
    return () => {
      window.removeEventListener("keydown", handleKeyPress);
    };
  }, []);

  // Функция обработки входа
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
