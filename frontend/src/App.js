import React from "react";
import { BrowserRouter as Router, Route, Routes, Navigate } from "react-router-dom";
import HomePage from "./pages/HomePage";
import UsersListPage from "./pages/UsersListPage";
import RegisterPage from "./pages/RegisterPage";
import LoginPage from "./pages/LoginPage";
import { AuthProvider } from "./context/AuthContext";
import PrivateRoute from "./components/PrivateRoute";

function App() {
  return (
    <AuthProvider>
      <Router>
        <div className="App">
          <Routes>

            <Route
              path="/main"
              element={<PrivateRoute element={HomePage} />}
            />

            <Route
              path="/users_list"
              element={<PrivateRoute element={UsersListPage} />}
            />

            <Route path="/login_page" element={<LoginPage />} />

            <Route path="/register_page" element={<RegisterPage />} />

            <Route path="/" element={<Navigate to="/main" />} />
          </Routes>
        </div>
      </Router>
    </AuthProvider>
  );
}

export default App;
