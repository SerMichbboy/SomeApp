import React, { createContext, useState, useEffect } from "react";
import { jwtDecode } from "jwt-decode";

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [accessToken, setAccessToken] = useState(localStorage.getItem("access"));

  useEffect(() => {
    const token = localStorage.getItem("access");
    if (token) {
      try {
        const decodedToken = jwtDecode(token);
        if (decodedToken.exp * 1000 > Date.now()) {
          setUser(decodedToken);
        } else {
          localStorage.removeItem("access");
          localStorage.removeItem("refresh");
        }
      } catch (error) {
        console.error("Invalid token:", error);
      }
    }
  }, []);

  const login = (accessToken, refreshToken) => {
    localStorage.setItem("access", accessToken);
    localStorage.setItem("refresh", refreshToken);
    const decodedToken = jwtDecode(accessToken);
    setUser(decodedToken);
  };

const logout = async () => {
  const token = localStorage.getItem("access");

  try {
    const response = await fetch("http://127.0.0.1:8000/api/token/delete/", {
      method: "DELETE",
      headers: {
        "Authorization": `Bearer ${token}`,
      },
    });

    if (response.ok) {
      localStorage.removeItem("access");
      localStorage.removeItem("refresh");
      setUser(null);
    } else {
      console.error("Failed to logout from server");
    }
  } catch (error) {
    console.error("Error during logout:", error);
  }
};

  return (
    <AuthContext.Provider value={{ user, login, logout }}>
      {children}
    </AuthContext.Provider>
  );
};
