import React, { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import RegistrationForm from "./RegistrationForm";
import '../styles/RegisterPage.css';

function RegisterPage() {
  const navigate = useNavigate();

  const handleGoHome = () => {
    navigate("/");
  };

  const handleKeyPress = (event) => {
    if (event.key === "Escape") {
      handleGoHome(); // Переход на главную страницу при нажатии Esc
    }
  };

  // Добавляем обработчик события при монтировании компонента
  useEffect(() => {
    window.addEventListener("keydown", handleKeyPress); // Слушаем все клавиши на уровне окна
    return () => {
      window.removeEventListener("keydown", handleKeyPress); // Убираем обработчик при размонтировании
    };
  }, []);

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
