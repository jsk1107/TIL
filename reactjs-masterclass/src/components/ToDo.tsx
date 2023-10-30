import { useRecoilValue, useSetRecoilState } from "recoil";
import { IToDo, toDoState } from "../atoms";

function ToDo({ text, category, id }: IToDo) {
  //   const onClick = (newCategory: IToDo["category"]) => {
  // console.log("I wanna to ", newCategory);
  //   };
  const setToDos = useSetRecoilState(toDoState);
  const onClick = (event: React.MouseEvent<HTMLButtonElement>) => {
    const {
      currentTarget: { name },
    } = event;
    setToDos((oldToDos) => {
      const targetIndex = oldToDos.findIndex(
        (arrayValue) => arrayValue.id === id
      );
      const newToDos = { text, id, category: name as any };
      return [
        ...oldToDos.slice(0, targetIndex),
        newToDos,
        ...oldToDos.slice(targetIndex + 1),
      ];
    });
  };
  return (
    <li>
      <span>{text}</span>
      {category !== "DOING" && (
        // <button onClick={() => onClick("DOING")}>Doing</button>
        <button name="DOING" onClick={onClick}>
          Doing
        </button>
      )}
      {category !== "TODO" && (
        // <button onClick={() => onClick("TODO")}>TODO</button>
        <button name="TODO" onClick={onClick}>
          TODO
        </button>
      )}
      {category !== "DONE" && (
        // <button onClick={() => onClick("DONE")}>Done</button>
        <button name="DONE" onClick={onClick}>
          DONE
        </button>
      )}
    </li>
  );
}

export default ToDo;
