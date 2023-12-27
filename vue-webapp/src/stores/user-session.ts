import type { Character } from '@/models/character';
import type { User } from '@/models/user';
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', {
  state: () => {
    return {
      id: -1,
      loggedIn: false,
      name: "",
      selectedCharacter:
      {
        id: -1,
        name: ""
      }
    } as User
  },
  // could also be defined as
  // state: () => ({ count: 0 })
  actions: {
    setLoggedIn(name: string, userId: number) {
      this.loggedIn = true;
      this.id = userId;
      this.name = name;
    },
    setLoggedOut() {
      this.id = -1;
      this.loggedIn = false;
      this.name = "";
    },
    setCharacter(ch: Character) {
      debugger
      this.selectedCharacter = JSON.parse(JSON.stringify(ch)) as Character;
    },
    resetCharacter() {
      this.selectedCharacter = {
        id: -1,
        name: "",
        level: -1,
        className: ""
      }
    }
  }
})