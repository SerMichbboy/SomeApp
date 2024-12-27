import React, { useContext } from "react";
import { Navigate } from "react-router-dom";
import { AuthContext } from "../context/AuthContext";

const PrivateRoute = ({ element: Element, ...rest }) => {
  const { user } = useContext(AuthContext);
  return <Element {...rest} />;
};

export default PrivateRoute;
