import type { Character } from '@/models/character';
import { useUserStore } from '../stores/user-session'
import type { User } from '@/models/user';


function delete_cookie(name: string, path?: string, domain?: string) {
    document.cookie = name + "=" +
        ((path) ? ";path=" + path : "") +
        ((domain) ? ";domain=" + domain : "") +
        ";expires=Thu, 01 Jan 1970 00:00:01 GMT";
}

function getUserCookies() {
    return document.cookie.split('; ');
}

export function logOut() {
    const userSession = useUserStore();
    userSession.setLoggedOut();
    delete_cookie("user_id");
    delete_cookie("user_name");
}

export function logIn(user_data: User) {
    var prev_login = getUserCookies();

    if (prev_login.length) {
        prev_login.forEach(element => {
            delete_cookie("user_id");
            delete_cookie("user_name");
        });
    }
    document.cookie = `user_id=${user_data.id};;max-age=max-age-in-seconds=${60 * 60 * 1};SameSite=Lax;`;
    document.cookie = `user_name=${user_data.name};;max-age=max-age-in-seconds=${60 * 60 * 1};SameSite=Lax;`;
    const userSession = useUserStore();

    userSession.setLoggedIn(user_data.name, user_data.id)
}

export function restoreUser() {
    var prev_login = getUserCookies();
    if (prev_login.length == 0) {
        throw Error("No users");
    }
    const id = prev_login.find(el => { return el.startsWith("user_id"); });
    const name = prev_login.find(el => { return el.startsWith("user_name"); });
    if (!id || !name) {
        logOut();
        throw Error("Invalid user");
    }

    const id_val = id.split("=")[1];
    const name_val = name.split("=")[1];

    const userSession = useUserStore();

    userSession.setLoggedIn(name_val, Number(id_val))
}