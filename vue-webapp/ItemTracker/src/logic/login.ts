import type { Character } from '@/models/character';
import { useUserStore } from '../stores/user-session'
import type { User } from '@/models/user';


function delete_cookie(name: string, path?: string, domain?: string) {
    document.cookie = name + "=" +
        ((path) ? ";path=" + path : "") +
        ((domain) ? ";domain=" + domain : "") +
        ";expires=Thu, 01 Jan 1970 00:00:01 GMT";
}

function getUserIdCookie() {
    return document.cookie.split(';').filter((item) => item.trim().startsWith('user_id='));
}

export function logOut() {
    const userSession = useUserStore();

    userSession.setLoggedOut();
    delete_cookie("user_id");
}

export function logIn(user_data: User) {
    var prev_login = getUserIdCookie();

    if (prev_login.length) {
        prev_login.forEach(element => {
            delete_cookie("user_id");
        });
    }
    document.cookie = `user_id=${user_data.id}; ;max-age=max-age-in-seconds=${60 * 60 * 1};SameSite=Lax;`;
    const userSession = useUserStore();

    userSession.setLoggedIn(user_data.name, user_data.id)
}