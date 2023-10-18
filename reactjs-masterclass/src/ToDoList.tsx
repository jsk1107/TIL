import { useState } from "react";
import { useForm } from "react-hook-form";
import { DefaultValue } from "recoil";

// function TodoList() {
//   const [toDo, setToDo] = useState("");
//   const onChange = (e: React.FormEvent<HTMLInputElement>) => {
//     const {
//       currentTarget: { value },
//     } = e;
//     setToDo(value);
//   };
//   const onSubmit = (e: React.FormEvent<HTMLFormElement>) => {
//     e.preventDefault();
//     console.log(toDo);
//   };

//   return (
//     <div>
//       <form onSubmit={onSubmit}>
//         <input onChange={onChange} value={toDo} placeholder="Write a to do" />
//         <button>Add</button>
//       </form>
//     </div>
//   );
// }

interface IForm {
  email: string;
  fistName: string;
  lastName: string;
  userName: string;
  password: string;
  password1: string;
  extraError?: string;
}

function TodoList() {
  const {
    register,
    watch,
    handleSubmit,
    formState: { errors },
    setError,
  } = useForm<IForm>();
  const onValid = (data: IForm) => {
    if (data.password !== data.password1) {
      setError(
        "password1",
        { message: "Password are not the same" },
        { shouldFocus: true }
      );
    }
    // setError(
    //   "extraError",
    //   { message: "Server Offline" }
    // );
  };
  // console.log(watch());
  console.log(errors);
  return (
    <div>
      <form
        style={{
          display: "flex",
          flexDirection: "column",
          width: "200px",
          margin: "20px",
        }}
        onSubmit={handleSubmit(onValid)}
      >
        <input
          {...register("email", {
            required: "email required",
            pattern: {
              value: /^[A-Za-z0-9._%+-]+@naver.com$/,
              message: "Only naver.com eamils allows",
            },
          })}
          placeholder="Email"
        />
        <span>{errors?.email?.message}</span>
        <input
          {...register("fistName", {
            required: "write here!",
            minLength: {
              value: 10,
              message: "at least 10 string",
            },
          })}
          placeholder="Fist Name"
        />
        <span>{errors?.fistName?.message}</span>
        <input
          {...register("lastName", {
            required: "password is required",
            minLength: {
              value: 5,
              message: "Too Short",
            },
          })}
          placeholder="Last Name"
        />
        <span>{errors?.lastName?.message}</span>
        <input
          {...register("userName", {
            required: true,
            validate: {
              noNico: (value) =>
                value.includes("nico") ? "No nico allowed" : true,
              noNick: (value) =>
                value.includes("nick") ? "No nick allowed" : true,
            },
          })}
          placeholder="UserName"
        />
        <span>{errors?.userName?.message}</span>
        <input
          {...register("password", { required: true, minLength: 10 })}
          placeholder="Password"
        />
        <span>{errors?.password?.message}</span>
        <input
          {...register("password1", { required: true, minLength: 10 })}
          placeholder="Password1"
        />
        <span>{errors?.password1?.message}</span>
        <button>Add</button>
        <span>{errors?.extraError?.message}</span>
      </form>
    </div>
  );
}

export default TodoList;
