from ActiveRecords.Object import Object
from Application.ConnectionManager import ConnectionManager
from Application.Constants import *
from Application.DomainExeption import DatabaseGatewayError


class User(Object):
    FIND_USER_BY_ID_STRING = "SELECT * FROM USERS WHERE USERS.ID = {};"
    FIND_USER_BY_USERNAME_STRING = "SELECT * FROM USERS WHERE USERS.USERNAME = '{}';"
    INSERT_USER_STRING = "INSERT INTO USERS (username, PWD_HASH, IS_PIDR) VALUES('{}', '{}', {}) RETURNING ID;"
    UPDATE_USER_STRING = "UPDATE USERS SET (USERNAME, PWD_HASH, IS_PIDR) = ('{}', '{}', {}) WHERE USERS.ID = {};"
    DELETE_USER_STRING = "DELETE FROM USERS WHERE ID = {};"

    def __init__(self, username, password_hash, is_pidr, id = INVALID_ID):
        super().__init__(id)
        self.username = username
        self.password_hash = password_hash
        self.is_pidr = is_pidr

    @classmethod
    def from_id(this_class, id):
        username = ""
        password_hash = ""
        is_pidr = False
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.FIND_USER_BY_ID_STRING.format(id))
                data = cur.fetchone()
                id = data[0]
                username = data[1]
                password_hash = data[2]
                is_pidr = data[3]
        return this_class(username, password_hash, is_pidr, id)

    @classmethod
    def from_username(this_class, username):
        # Find user
        id = INVALID_ID
        res_username = ""
        pwd = ""
        is_pidr = False
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.FIND_USER_BY_USERNAME_STRING.format(username))
                data = cur.fetchone()
                if not data:
                    raise DatabaseGatewayError("Could not find existing users with name " + username)
                id = data[0]
                res_username = data[1]
                pwd = data[2]
                is_pidr = data[3]
        return this_class(res_username, pwd, is_pidr, id)
    
    def insert(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.INSERT_USER_STRING.format(self.username, self.password_hash, self.is_pidr))
                return cur.fetchone()[0]

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.UPDATE_USER_STRING.format(self.username, self.password_hash, self.is_pidr, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.DELETE_USER_STRING.format(self.id))
    
    def get_all_character_ids(self):
        pass
