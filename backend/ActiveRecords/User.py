from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *


class User(Object):
    FIND_USER_BY_ID_STRING = "SELECT * FROM USERS WHERE USERS.ID = {};"
    FIND_USER_BY_USERNAME_STRING = "SELECT * FROM USERS WHERE USERS.USERNAME = '{}';"
    INSERT_USER_STRING = "INSERT INTO USERS (username, PWD_HASH) VALUES('{}', '{}');"
    UPDATE_USER_STRING = "UPDATE USERS SET (USERNAME, PWD_HASH) VALUES('{}', '{}') WHERE USERS.ID = {};"
    DELETE_USER_STRING = "DELETE FROM USERS WHERE ID = {};"

    def __init__(self, id):
        super(id)
        self.username = ""
        self.password_hash = ""
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.FIND_USER_BY_ID_STRING.format(id))
                data = cur.fetchone()
                self.id = data[0]
                self.username = data[1]
                self.password_hash = data[2]

    def __init__(self, username, password_hash, id = INVALID_ID):
        super().__init__(id)
        self.username = username
        self.password_hash = password_hash

    @classmethod
    def from_username(this_class, username):
        # Find user
        id = INVALID_ID
        res_username = ""
        pwd = ""
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.FIND_USER_BY_USERNAME_STRING.format(username))
                data = cur.fetchone()
                id = data[0]
                res_username = data[1]
                pwd = data[2]
        return this_class(res_username, pwd, id)
    
    def insert(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.INSERT_USER_STRING.format(self.username, self.password_hash))

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.UPDATE_USER_STRING.format(self.username, self.password_hash, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(User.DELETE_USER_STRING.format(self.id))
    
    def get_all_character_ids(self):
        pass
