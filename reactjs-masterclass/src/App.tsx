import React from "react";
import ReactDOM from "react-dom/client";
// import ReactDOM from 'react-dom/client';

import styled, { keyframes} from "styled-components";

const Wrapper = styled.div`
  background-color: ${(props) => props.theme.backgroundColor};
  display: flex;
`;

const Title = styled.h1`
  color: ${(props) => props.theme.textColor};
`;

// property를 넘겨받아서 dynamic하게 사용가능.

const rotateAnimation = keyframes`
  /* from {
    transform: rotate(0deg);
    border-radius: 0px;
  }
  to {
    transform: rotate(360deg);
    border-radius: 100px;
  } */
  0%{
    transform: rotate(0deg);
    border-radius: 0px;
  }
  50%{
    transform: rotate(360deg);
    border-radius: 100px;
  }
  100%{
    transform: rotate(0deg);
    border-radius: 0px;
  }
`;

const Emoji = styled.span`
  font-size: 36px;
`;

const Box = styled.div`
  background-color: "tomato";
  width: 200px;
  height: 200px;
  display: flexbox;
  justify-content: center;
  align-items: center;

  animation: ${rotateAnimation} 1s linear infinite;
  // box:span 하는것과 같은방법임. Pseudo Selector라고 부른다.
  ${Emoji}{
    // span 내부에 또다시 속성을 주려면 &: (span:hover와 같음)를 사용하면 된다.
    &:hover{
      font-size: 96px;
    }

    &:active{
      opacity: 0;
    }
  }
`;

function App() {
  return (
    <Wrapper>
      <Title> Hello world!!</Title>
      <Box>
        <Emoji as="div"> 😇 </Emoji>
      </Box>
      <Emoji> 🫀 </Emoji>
    </Wrapper>  
  );
}

export default App;
