import styled, { createGlobalStyle } from "styled-components";
import TodoList from "./TodoList";
import { useState } from "react";
import Router from "./Router";

const Theme = styled.div`
  background-color: ${props => props.theme.bgColor};
`;

const GlobalStyle = createGlobalStyle`
  @import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400&display=swap');
  body {
    font-weight: 300;
    line-height: 1.2;
    font-family: 'Source Sans Pro', sans-serif;
    background-color: ${props => props.theme.bgColor};
    color: ${props => props.theme.textColor};
  }
  a{
    text-decoration: None;
    color:inherit;
  }
  * {
    box-sizing: border-box;
  }
`;

function App() {
  return (
    <Router></Router>
  )
}

export default App;
