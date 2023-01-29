import { useRecoilState, useRecoilValue } from "recoil";
import { Categories, categoryState, toDoSelector } from "./atom";
import CreateToDo from "./components/CreateToDo";
import ToDo from "./components/ToDo";


function TodoList() {
    const toDos = useRecoilValue(toDoSelector);
    const [category, setCategory] = useRecoilState(categoryState)
    const onInput = (event: React.FormEvent<HTMLSelectElement>) => {
        setCategory(event.currentTarget.value as any);
    };
    return <div>
        <h1> ToDos !!</h1>
        <select value={category} onInput={onInput}>
            <option value={Categories.TODO}>TODO</option>
            <option value={Categories.DOING}>DOING</option>
            <option value={Categories.DONE}>DONE</option>
        </select>
        <hr />
        <CreateToDo />
        {toDos?.map((toDo) => <ToDo key={toDo.id} {...toDo} />)
        }
    </div >
}

export default TodoList;