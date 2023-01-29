import { useForm } from "react-hook-form";
import { useRecoilState, useRecoilValue } from "recoil";
import { toDoState } from "./atom";
import CreateToDo from "./components/CreateToDo";
import ToDo from "./components/ToDo";


function TodoList() {
    const toDos = useRecoilValue(toDoState);
    return <div>
        <h1> ToDos !!</h1>
        <hr />

        <CreateToDo />
        <ul>
            {toDos.map((toDo) => <ToDo key={toDo.id} {...toDo} />)}
        </ul>
    </div>
}

export default TodoList;