import React from "react";
import { useNavigate } from "react-router-dom";
import RegistrationForm from "./RegistrationForm";
import '../styles/RegisterPage.css';

function RegisterPage() {
  const navigate = useNavigate();

  const handleGoHome = () => {
    navigate("/");
  };

  return (
    <div>
      <RegistrationForm />
      <button className="btn-home" onClick={handleGoHome}>
        Go to Home
      </button>
    </div>
  );
}

export default RegisterPage;
