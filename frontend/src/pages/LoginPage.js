import React, { useState, useEffect, useContext } from "react";
import "../styles/LoginPage.css";
import { useNavigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

const LoginPage = () => {
  const [identifier, setIdentifier] = useState("");
  const [password, setPassword] = useState("");
  const [showPassword, setShowPassword] = useState(false);
  const navigate = useNavigate();
  const { login } = useContext(AuthContext);

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
      password,
    };

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/api/token/create/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(loginData),
        }
      );

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Login failed");
      }

      const data = await response.json();
      const { access, refresh } = data;

      login(access, refresh);

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
        <div className="password-input-container">
          <input
              type={showPassword ? "text" : "password"}
              className="password-input"
              placeholder="Password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
          />
          <button
              type="button"
              className="btn-show"
              onClick={() => setShowPassword((prev) => !prev)}
          >
            {showPassword ? (
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    className="icon-eye"
                >
                  <path d="M1 12s4-7 11-7 11 7 11 7-4 7-11 7-11-7-11-7z"></path>
                  <circle cx="12" cy="12" r="3"></circle>
                </svg>
            ) : (
                <svg
                    xmlns="http://www.w3.org/2000/svg"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    strokeWidth="2"
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    className="icon-eye-off"
                >
                  <path
                      d="M17.94 17.94A10.94 10.94 0 0 1 12 19C5 19 1 12 1 12a19.72 19.72 0 0 1 4.55-5.94"></path>
                  <path d="M1 1l22 22"></path>
                </svg>
            )}
          </button>
        </div>
        <button type="submit" className="btn-login">
          Login
        </button>
      </form>
    </div>
  );
};

export default LoginPage;
