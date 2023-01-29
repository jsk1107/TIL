import { useSetRecoilState } from "recoil";
import { IToDo, toDoState } from "../atom";
import { Categories } from "../atom";

function ToDo({ text, category, id }: IToDo) {
    const setTodos = useSetRecoilState(toDoState);
    const onClick = (newCategory: IToDo["category"]) => {
        setTodos((allToDo) => {
            const targetIndex = allToDo.findIndex((toDo) => toDo.id == id);
            const newToDos = { text, category: newCategory, id };
            // slice는 new array를 생성한다. splice는 기존 array를 수정한다. 원본수정하기 때문에 버그발생 존재
            return [...allToDo.slice(0, targetIndex), newToDos, ...allToDo.slice(targetIndex + 1)];
        })
    };
    console.log(Categories.TODO);
    return (
        <li>
            <span>
                {text}
            </span>
            {category !== Categories.TODO && <button onClick={() => onClick(Categories.TODO)}>TODO</button>}
            {category !== Categories.DOING && <button onClick={() => onClick(Categories.DOING)}>DOING</button>}
            {category !== Categories.DONE && <button onClick={() => onClick(Categories.DONE)}>DONE</button>}
        </li>
    );
}

export default ToDo;