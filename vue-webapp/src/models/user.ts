import type { Character } from "./character";


export interface User {
    id: number,
    loggedIn: boolean,
    name: string,
    selectedCharacter: Character
}
