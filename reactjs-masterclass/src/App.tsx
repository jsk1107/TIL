import { ThemeProvider, createGlobalStyle } from "styled-components";
import { Reset } from "styled-reset";
import { useRecoilValue } from "recoil";
import TodoList from "./components/ToDoList";

const GlobalStyle = createGlobalStyle`
  @import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400&display=swap');
  body {
    font-weight: 300;
    line-height: 1.2;
    font-family: 'Source Sans Pro', sans-serif;
    background-color: ${(props) => props.theme.bgColor};
    color: ${(props) => props.theme.textColor};
  }
  a{
    text-decoration: None;
    color:inherit;
  }
  * {
    box-sizing: border-box;
  }
  h1{
    font-size: 1.5rem;
    font-weight: bold;
  }
`;

function App() {
  return (
    <>
      <Reset />
      <GlobalStyle />
      <TodoList />
    </>
  );
}

export default App;
