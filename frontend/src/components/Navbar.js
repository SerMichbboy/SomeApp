import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
  return (
    <nav>
      <ul>
        <li><Link to="/main">Home</Link></li>
        <li><Link to="/users_list">Users List</Link></li>
        <li><Link to="/register_page">Register</Link></li>
      </ul>
    </nav>
  );
}

export default Navbar;
