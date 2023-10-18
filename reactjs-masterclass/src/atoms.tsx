import { atom } from "recoil";

export interface IToDo {
  text: string;
  id: number;
  category: "DONE" | "DOING" | "TODO";
}

export const toDoState = atom<IToDo[]>({
  key: "toDo",
  default: [],
});
