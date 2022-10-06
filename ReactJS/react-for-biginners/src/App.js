
import {useState, useEffect} from "react";

function App() {
  const [count, setCount] = useState(0);
  const [input, setInput] = useState("");
  const [inverse, setInverse] = useState(false);

  const onClick = () => {
    setCount((current) => current + 1);
  }
  const onChange = (event) => {
    setInput(event.target.value);
    console.log(input);
  }
  const onInverse = () => {
    setInverse((current) => !current);
  }

  useEffect(()=>{ console.log("hello", count) }, []);
  useEffect(()=>{ console.log("hello", input) }, [input]);

  return (
    <div>
      <h1>{count}</h1>
      <div>
        <input value={input} onChange={onChange} type="text" placeholder="write someting text"></input>
      </div>
      <button onClick={onClick}> Click </button>
      <button onClick={onInverse}> {inverse ? "inverse" : "inversed"} </button>
    </div>
  );
}

export default App;
