import React from "react";
import { ReactDOM } from "react-dom";
import styled from "styled-components";

const Father = styled.div`
  display: flex;
`;

// property를 넘겨받아서 dynamic하게 사용가능.
const Box = styled.div`
  background-color: ${(props) => props.bgColor};
  width: 100px;
  height: 100px;
`;

// Box의 모든 스타일을 상속받으려면 styled(Obj)를 사용하면됨.
const Circle = styled(Box)`
  border-radius: 50px;
`;

const Btn = styled.button`
  color: white;
  background-color: tomato;
  border: 0;
  border-radius: 10px;
`;

const Input = styled.input.attrs({ required: true, minLength: 10 })`
  color: white;
  background-color: tomato;
`;

function App() {
  return (
    <Father>
      <Btn> LogIn</Btn>
      <Btn as="a" href="/"> LogIn</Btn>

      <Input></Input>
      <Input></Input>
      <Input></Input>
      <Input></Input>
    </Father>  
  );
}

export default App;
