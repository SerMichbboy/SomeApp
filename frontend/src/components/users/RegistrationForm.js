import React, { useState } from "react";
import axios from "axios";

const RegistrationForm = () => {
  const [formData, setFormData] = useState({
    username: "",
    password: "",
    email: "",
    first_name: "",
    last_name: "",
    date_of_birth: "",
    phone_number: "",
    address: "",
    bio: "",
    website: "",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const api = axios.create({
    baseURL: "http://127.0.0.1:8000/api/",
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await api.post("users/", formData);
      setMessage("User registered successfully!");
      console.log(response);
    } catch (error) {
      if (error.response) {
        setMessage("Error: " + JSON.stringify(error.response.data));
        console.error(error.response.data);
      } else {
        setMessage("Error: " + error.message);
        console.error(error.message);
      }
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "0 auto", padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1 style={{ textAlign: "center" }}>User Registration</h1>
      <form onSubmit={handleSubmit} style={{ display: "flex", flexDirection: "column", gap: "10px" }}>
        <label>
          Username:
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <label>
          Email:
          <input
            type="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <label>
          First Name:
          <input
            type="text"
            name="first_name"
            value={formData.first_name}
            onChange={handleChange}
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <label>
          Last Name:
          <input
            type="text"
            name="last_name"
            value={formData.last_name}
            onChange={handleChange}
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <label>
          Date of Birth:
          <input
            type="date"
            name="date_of_birth"
            value={formData.date_of_birth}
            onChange={handleChange}
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <label>
          Phone Number:
          <input
            type="text"
            name="phone_number"
            value={formData.phone_number}
            onChange={handleChange}
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <label>
          Address:
          <input
            type="text"
            name="address"
            value={formData.address}
            onChange={handleChange}
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <label>
          Bio:
          <textarea
            name="bio"
            value={formData.bio}
            onChange={handleChange}
            rows="3"
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <label>
          Website:
          <input
            type="url"
            name="website"
            value={formData.website}
            onChange={handleChange}
            style={{ width: "100%", padding: "8px" }}
          />
        </label>
        <button type="reset" style={{ padding: "10px", backgroundColor: "#f5f5f5", border: "1px solid #ccc" }}>Clear</button>
        <button type="submit" style={{ padding: "10px", backgroundColor: "#007bff", color: "white", border: "none" }}>Register</button>
      </form>
      {message && <p style={{ textAlign: "center", marginTop: "10px", color: message.includes("Error") ? "red" : "green" }}>{message}</p>}
    </div>
  );
};

export default RegistrationForm;
