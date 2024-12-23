import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';

// Убедитесь, что здесь правильно указываете id "root"
const rootElement = document.getElementById('root');

if (rootElement) {
  const root = ReactDOM.createRoot(rootElement);
  root.render(
    <React.StrictMode>
      <App />
    </React.StrictMode>
  );
} else {
  console.error('Element with id "root" not found');
}
