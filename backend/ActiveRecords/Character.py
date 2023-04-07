from ActiveRecords.Object import Object
from Application.ConnectionManager import ConnectionManager
from Application.Constants import *


class Character(Object):
    FIND_CHARACTER_BY_ID_STRING = "SELECT * FROM CHARACTERS WHERE CHARACTERS.ID = {};"
    INSERT_CHARACTER_STRING = "INSERT INTO CHARACTERS (NAME, LEVEL, CLASS) VALUES('{}', {}, '{}') RETURNING ID;"
    INSERT_USER_CHARACTER_STRING = "INSERT INTO USER_CHARACTERS (USER_ID, CHARACTER_ID) VALUES({}, {})"
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

    def insert(self, user_id):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.INSERT_CHARACTER_STRING.format(self.name, self.level, self.class_name))
                new_id = cur.fetchone()[0]
                # cur.execute(Character.INSERT_USER_CHARACTER_STRING.format(user_id, new_id))
                return new_id

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.UPDATE_CHARACTER_STRING.format(self.name, self.level, self.class_name, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.DELETE_CHARACTER_STRING.format(self.id))
