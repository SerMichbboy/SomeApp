import React from "react";
import RegistrationForm from "../components/users/RegistrationForm"; // Путь к компоненту формы регистрации

function RegisterPage() {
  return (
    <div>
      <h1>Register New User</h1>
      <RegistrationForm />
    </div>
  );
}

export default RegisterPage;
