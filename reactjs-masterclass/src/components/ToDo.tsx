import { IToDo } from "../atom";

function ToDo({ text, category }: IToDo) {
    const onClick = (newCategory: IToDo["category"]) => {
        console.log(newCategory)
    }
    return (
        <li>
            <span>
                {text}
            </span>
            {category !== "TODO" && <button onClick={() => onClick("TODO")}>TODO</button>}
            {category !== "DOING" && <button onClick={() => onClick("DOING")}>DOING</button>}
            {category !== "DONE" && <button onClick={() => onClick("DONE")}>DONE</button>}
        </li>
    );
}

export default ToDo;