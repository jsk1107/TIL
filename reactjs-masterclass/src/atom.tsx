import { atom, selector } from "recoil";

// type categories = "TODO" | "DOING" | "DONE";

export enum Categories {
    "TODO" = "TODO",
    "DOING" = "DOING",
    "DONE" = "DONE"
}

export interface IToDo {
    text: string;
    id: number;
    category: Categories
}

export const categoryState = atom<Categories>({
    key: "category",
    default: Categories.TODO
})

export const toDoState = atom<IToDo[]>(
    {
        key: "toDo",
        default: []
    }
)

export const toDoSelector = selector({
    key: "selector",
    get: ({ get }) => {
        const toDos = get(toDoState);
        const category = get(categoryState);
        return toDos.filter(toDo => toDo.category == category);
    }
})