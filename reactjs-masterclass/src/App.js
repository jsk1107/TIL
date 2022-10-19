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
`

function App() {
  return (
    <Father>
      <Box bgColor="tomato"/>
      <Circle bgColor="teal"/>
    </Father>  
  );
}

export default App;
