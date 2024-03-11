import { atom, selector } from "recoil";

export interface IToDo {
  text: string;
  id: number;
  category: "DONE" | "DOING" | "TODO";
}

export const toDoState = atom<IToDo[]>({
  key: "toDo",
  default: [],
});

export const toDoSelector = selector({
  key: "toDoSelector",
  get: ({ get }) => {
    const toDoLength = get(toDoState);
    console.log(toDoLength.length);
    return toDoLength.length;
  },
});
