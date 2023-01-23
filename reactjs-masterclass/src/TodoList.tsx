import { useForm } from "react-hook-form";

interface IForm {
    email: string;
    firstName: string;
    lastName: string;
    userName: string;
    password: string;
    confirmPassword: string;
    extraError: string;
}

function TodoList() {
    const { register, handleSubmit, setError, formState: { errors } } = useForm<IForm>({
        defaultValues: {
            email: "@naver.com"
        }
    });
    console.log(errors);
    const onValid = (data: IForm) => {
        if (data.password !== data.confirmPassword) {
            setError("confirmPassword", { message: "Password art not Same!!" }, { shouldFocus: true })
        }
        setError("extraError", { message: "Server offline." })
    }
    return <div>
        <form style={{ display: "flex", flexDirection: "column" }}
            onSubmit={handleSubmit(onValid)} >
            <input {...register("email", {
                required: "email is required",
                pattern: {
                    value: /^[A-Za-z0-9._%+-]+@naver.com$/,
                    message: "Only naver.com emails allowed."
                }
            })} placeholder="Email" />
            <span>
                {errors?.email?.message}
            </span>
            <input {...register("firstName", {
                required: "FistName is required",
                minLength: {
                    value: 5,
                    message: "frstName is too short"
                },
                validate: {
                    noJSK: ((current) => current.includes("jsk") ? "No jsk allowed" : true),
                    noQQQ: ((current) => current.includes("qqq") ? "No qqq allowed" : true)
                }
            })}
                placeholder="firstName" />
            <span>
                {errors?.firstName?.message}
            </span>
            <input {...register("lastName", { required: "lastName is required" })} placeholder="lastName" />
            <span>
                {errors?.lastName?.message}
            </span>
            <input {...register("userName", { required: "userName is required" })} placeholder="userName" />
            <span>
                {errors?.userName?.message}
            </span>
            <input {...register("password", { required: "password is required" })} placeholder="password" />
            <span>
                {errors?.password?.message}
            </span>
            <input {...register("confirmPassword", { required: "password is required" })} placeholder="confirmPassword" />
            <span>
                {errors?.confirmPassword?.message}
            </span>
            <button> Add </button>
            <span>{errors?.extraError?.message}</span>
        </form>
    </div>
}

export default TodoList;