import { IToDo } from "../atoms";

function ToDo({ text, category, id }: IToDo) {
  //   const onClick = (newCategory: IToDo["category"]) => {
  // console.log("I wanna to ", newCategory);
  //   };
  const onClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    const {
      currentTarget: { name },
    } = event;
    console.log("I wanna to ", name);
  };
  return (
    <li>
      <span>{text}</span>
      {category !== "DOING" && (
        // <button onClick={() => onClick("DOING")}>Doing</button>
        <button name="DOING" onClick={onClick}>
          {" "}
          Doing{" "}
        </button>
      )}
      {category !== "TODO" && (
        // <button onClick={() => onClick("TODO")}>TODO</button>
        <button name="TODO" onClick={onClick}>
          {" "}
          TODO{" "}
        </button>
      )}
      {category !== "DONE" && (
        // <button onClick={() => onClick("DONE")}>Done</button>
        <button name="DONE" onClick={onClick}>
          {" "}
          DONE{" "}
        </button>
      )}
    </li>
  );
}

export default ToDo;
