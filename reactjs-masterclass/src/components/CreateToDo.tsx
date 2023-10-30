import { useForm } from "react-hook-form";
import { useSetRecoilState } from "recoil";
import { IToDo, toDoState } from "../atoms";

function CreateToDo() {
  const setToDos = useSetRecoilState(toDoState);
  const { register, handleSubmit, setValue } = useForm<IToDo>();
  const handleValid = ({ text }: IToDo) => {
    setValue("text", "");
    setToDos((oldToDos) => [
      { text: text, id: Date.now(), category: "TODO" },
      ...oldToDos,
    ]);
  };
  return (
    <form onSubmit={handleSubmit(handleValid)}>
      <input
        {...register("text", { required: "Write a ToDo" })}
        placeholder="Write a to do"
      />
      <button>Add</button>
    </form>
  );
}

export default CreateToDo;
