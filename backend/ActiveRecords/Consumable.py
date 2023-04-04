from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *

class Consumable(Object):
    FIND_CONSUMABLE_BY_ID_STR = "SELECT * FROM CONSUMABLES WHERE CONSUMABLES.ID = {};"
    FIND_ALL_FOR_CHARACTER_STR = "SELECT a.id, a.name, a.DESCRIPTION, a.amount FROM CONSUMABLES as a \
                                LEFT JOIN CHAR_CONS ON (a.ID = CHAR_CONS.CONSUMABLE_ID) \
                                LEFT JOIN CHARACTERS ON (CHAR_CONS.CHARACTER_ID = CHARACTERS.ID) \
                                WHERE CHAR_CONS.CHARACTER_ID = {};"

    INSERT_CONSUMABLE_STR = "INSERT INTO CONSUMABLES (NAME, DESCRIPTION, AMOUNT) VALUES('{}', '{}', {}) RETURNING ID;"
    INSERT_CHARACTER_CONSUMABLE_STR = "INSERT INTO CHAR_CONS (CHARACTER_ID, CONSUMABLE_ID) VALUES({}, {});"

    UPDATE_CONSUMABLE_STR = "UPDATE CONSUMABLES SET (NAME, DESCRIPTION, AMOUNT) = ('{}', '{}', {}) WHERE CONSUMABLES.ID = {};"
    DELETE_CONSUMABLE_STR = "DELETE FROM CONSUMABLES WHERE ID = {};"

    def __init__(self, name, descr, amount, id = INVALID_ID):
        super().__init__(id)
        self.name = name
        self.descr = descr
        self.amount = amount

    @classmethod
    def from_id(my_class, id):
        res_id = INVALID_ID
        name = ""
        descr = ""
        amount = 0
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Consumable.FIND_CONSUMABLE_BY_ID_STR.format(id))
                data = cur.fetchone()
                res_id = data[0]
                name = data[1]
                descr = data[2]
                amount = data[3]
        return my_class(name, descr, amount, res_id)
    
    @classmethod
    def from_character_id(my_class, character_id):
        res = []
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Consumable.FIND_ALL_FOR_CHARACTER_STR.format(character_id))
                data = cur.fetchall()
                for art_tuple in data:
                    res.append(my_class(art_tuple[1], art_tuple[2], art_tuple[3], art_tuple[0]))
        return res

    def insert(self, character_id):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Consumable.INSERT_CONSUMABLE_STR.format(self.name, self.descr, self.amount))
                new_id = cur.fetchone()[0]
                cur.execute(Consumable.INSERT_CHARACTER_CONSUMABLE_STR.format(character_id, new_id))
                return new_id

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Consumable.UPDATE_CONSUMABLE_STR.format(self.name, self.descr, self.amount, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Consumable.DELETE_CONSUMABLE_STR.format(self.id))
    