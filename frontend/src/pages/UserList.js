import React, { useState, useEffect } from "react";
import axios from "axios";

const UserList = () => {
  const [users, setUsers] = useState([]);
  const [message, setMessage] = useState("");

  useEffect(() => {
    // Отправляем GET-запрос к серверу
    const fetchUsers = async () => {
      try {
        const response = await axios.get("http://127.0.0.1:8000/api/users/");
        setUsers(response.data);  // Сохраняем полученные данные в состояние
      } catch (error) {
        setMessage("Error: " + error.message);
      }
    };

    fetchUsers();
  }, []);  // Запрос только при монтировании компонента

  return (
    <div>
      <h1>Registered Users</h1>
      {message && <p>{message}</p>}
      <ul>
        {users.length > 0 ? (
          users.map((user) => (
            <li key={user.id}>
              {user.first_name} {user.last_name} ({user.username}) - {user.email}
            </li>
          ))
        ) : (
          <p>No users found.</p>
        )}
      </ul>
    </div>
  );
};

export default UserList;
