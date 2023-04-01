from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *


class Character(Object):
    FIND_CHARACTER_BY_ID_STRING = "SELECT * FROM CHARACTERS WHERE CHARACTERS.ID = {};"
    INSERT_CHARACTER_STRING = "INSERT INTO CHARACTERS (NAME, LEVEL, CLASS) VALUES('{}', {}, '{}');"
    UPDATE_CHARACTER_STRING = "UPDATE CHARACTERS SET (NAME, LEVEL, CLASS) VALUES('{}', {}, '{}') WHERE CHARACTERS.ID = {};"
    DELETE_CHARACTER_STRING = "DELETE FROM CHARACTERS WHERE ID = {};"

    def __init__(self, id):
        super(id)
        self.name = ""
        self.level = 0
        self.class_name = ""
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.FIND_CHARACTER_BY_ID_STRING.format(id))
                data = cur.fetchone()
                self.id = data[0]
                self.name = data[1]
                self.level = data[2]
                self.class_name = data[3]

    def __init__(self, name, level, class_name, id = INVALID_ID):
        super(id)
        self.name = name
        self.level = level
        self.class_name = class_name
    
    def insert(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.INSERT_CHARACTER_STRING.format(self.name, self.level, self.class_name))

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.UPDATE_CHARACTER_STRING.format(self.name, self.level, self.class_name, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Character.DELETE_CHARACTER_STRING.format(self.id))
    
    def get_all_item_ids(self):
        pass
    
    def get_all_consumable_ids(self):
        pass
    
    def get_all_artifact_ids(self):
        pass
    
    def get_all_spell_level_ids(self):
        pass
    
    def get_all_special_power_ids(self):
        pass