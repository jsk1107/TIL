import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import { ThemeProvider } from 'styled-components';

const darkmode = {
  textColor: "whitesmoke",
  backgroundColor: "#111"
};

const whitemode = {
  textColor: "#111",
  backgroundColor: "whitesmoke"
}

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(
  <React.StrictMode>
    <ThemeProvider theme={whitemode}>
      <App />
    </ThemeProvider>
  </React.StrictMode>
);