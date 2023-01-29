import { useForm } from "react-hook-form";
import { useSetRecoilState } from "recoil";
import { toDoState } from "../atom";


interface IForm {
    toDo: string
}


function CreateToDo() {
    const setToDos = useSetRecoilState(toDoState);
    const { register, handleSubmit, setValue } = useForm<IForm>();
    const onValid = ({ toDo }: IForm) => {
        setToDos((prevToDos) => [{ text: toDo, category: "TODO", id: Date.now() }, ...prevToDos])
        setValue("toDo", "")
    }
    return <form onSubmit={handleSubmit(onValid)}>
        <input {...register("toDo", { required: "write a to-do" })} placeholder="ToDos" />
        <button> add </button>
    </form>
}

export default CreateToDo;