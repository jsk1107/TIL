import { ThemeProvider, createGlobalStyle } from "styled-components";
import Router from "./Router";
import { Reset } from "styled-reset";
import { ReactQueryDevtools } from "react-query/devtools";
import { darkTheme, lightTheme } from "./theme";
import { useState } from "react";
import { useRecoilValue } from "recoil";
import { isDarkAtom } from "./atom";

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
`;

function App() {
  const isDark = useRecoilValue(isDarkAtom);
  return (
    <>
      <ThemeProvider theme={isDark ? darkTheme : lightTheme}>
        <Reset />
        <GlobalStyle />
        <Router />
        <ReactQueryDevtools initialIsOpen={true} />
      </ThemeProvider>
    </>
  );
}

export default App;
