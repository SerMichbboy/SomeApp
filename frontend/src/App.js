import React from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
import UsersListPage from "./pages/UsersListPage";
import RegisterPage from "./pages/RegisterPage";
import Navbar from "./components/Navbar";
import LoginPage from "./pages/LoginPage";

function App() {
  return (
    <Router>
      <div className="App">
        {/*<Navbar />*/}
        <Routes>
          {/* Главная страница */}
          <Route path="/main" element={<HomePage />} />

          {/* Страница со списком пользователей */}
          <Route path="/users_list" element={<UsersListPage />} />

          {/* Страница входа */}
          <Route path="/login_page" element={<LoginPage />} />

          {/* Страница регистрации */}
          <Route path="/register_page" element={<RegisterPage />} />

          {/* Редирект на главную страницу по умолчанию */}
          <Route path="/" element={<Navigate to="/main" />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
