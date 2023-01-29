import { useForm } from "react-hook-form";
import { useRecoilValue, useSetRecoilState } from "recoil";
import { categoryState, toDoState } from "../atom";


interface IForm {
    toDo: string
}


function CreateToDo() {
    const setToDos = useSetRecoilState(toDoState);
    const category = useRecoilValue(categoryState);
    const { register, handleSubmit, setValue } = useForm<IForm>();
    const onValid = ({ toDo }: IForm) => {
        setToDos((prevToDos) => [{ text: toDo, category: category, id: Date.now() }, ...prevToDos])
        setValue("toDo", "")
    }
    console.log(category)
    return <form onSubmit={handleSubmit(onValid)}>
        <input {...register("toDo", { required: "write a to-do" })} placeholder="ToDos" />
        <button> add </button>
    </form>
}

export default CreateToDo;