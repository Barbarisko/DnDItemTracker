from ActiveRecords.Object import Object
from Application.ConnectionManager import ConnectionManager
from Application.Constants import *


class Character(Object):
    FIND_CHARACTER_BY_ID_STRING = "SELECT * FROM CHARACTERS WHERE CHARACTERS.ID = {};"
    FIND_ALL_FOR_USER = "SELECT a.id, a.name, a.level, a.class FROM CHARACTERS as a \
                                LEFT JOIN USERS_CHARS ON (a.ID = USERS_CHARS.character_id) \
                                LEFT JOIN USERS ON (USERS_CHARS.user_id = USERS.ID) \
                                WHERE USERS_CHARS.USER_ID = {}"
    INSERT_CHARACTER_STRING = "INSERT INTO CHARACTERS (NAME, LEVEL, CLASS) VALUES('{}', {}, '{}') RETURNING ID;"
    INSERT_USER_CHARACTER_STRING = "INSERT INTO USERS_CHARS (USER_ID, CHARACTER_ID) VALUES({}, {})"
    UPDATE_CHARACTER_STRING = "UPDATE CHARACTERS SET (NAME, LEVEL, CLASS) = ('{}', {}, '{}') WHERE CHARACTERS.ID = {};"
    DELETE_CHARACTER_STRING = "DELETE FROM CHARACTERS WHERE ID = {};"

    def __init__(self, name, level, class_name, id = INVALID_ID):
        super().__init__(id)
        self.name = name
        self.level = level
        self.class_name = class_name
    
    @classmethod
    def from_id(my_class, id):
        res_id = INVALID_ID
        name = ""
        level = 0
        class_name = ""
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.FIND_CHARACTER_BY_ID_STRING.format(id))
                data = cur.fetchone()
                res_id = data[0]
                name = data[1]
                level = data[2]
                class_name = data[3]
        return my_class(name, level, class_name, res_id)
    
    @classmethod
    def from_user_id(my_class, user_id):
        res = []
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.FIND_ALL_FOR_USER.format(user_id))
                data = cur.fetchall()
                for character_tuple in data:
                    res.append(my_class(character_tuple[1], character_tuple[2], character_tuple[3], character_tuple[0]))
        return res

    def insert(self, user_id):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.INSERT_CHARACTER_STRING.format(self.name, self.level, self.class_name))
                new_id = cur.fetchone()[0]
                cur.execute(Character.INSERT_USER_CHARACTER_STRING.format(user_id, new_id))
                return new_id

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.UPDATE_CHARACTER_STRING.format(self.name, self.level, self.class_name, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.DELETE_CHARACTER_STRING.format(self.id))
