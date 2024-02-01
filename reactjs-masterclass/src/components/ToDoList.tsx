import { useRecoilValue } from "recoil";
import { toDoSelector, toDoState } from "../atoms";
import CreateToDo from "./CreateToDo";
import ToDo from "./ToDo";

function TodoList() {
  const toDos = useRecoilValue(toDoState);
  const selectorOutPut = useRecoilValue(toDoSelector);

  return (
    <div>
      <h1> To Do</h1>
      <hr />
      <form>
        <select>
          <option value="TODO"> TODO1 </option>
          <option value="DOING"> DOING </option>
          <option value="DONE"> DONE </option>
        </select>
      </form>
      <CreateToDo />
      <ul>
        {toDos.map((toDo) => (
          // <ToDo text={toDo.text} category={toDo.category} id={toDo.id} />
          <ToDo key={toDo.id} {...toDo} />
        ))}
      </ul>
    </div>
  );
}

export default TodoList;
