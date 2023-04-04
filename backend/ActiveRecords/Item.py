from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *

class Item(Object):
    FIND_ITEM_BY_ID_STR = "SELECT * FROM ITEMS WHERE ITEMS.ID = {};"
    FIND_ALL_FOR_CHARACTER_STR = "SELECT a.id, a.name, a.DESCRIPTION, a.amount FROM ITEMS as a \
                                LEFT JOIN CHAR_ITEMS ON (a.ID = CHAR_ITEMS.ITEM_ID) \
                                LEFT JOIN CHARACTERS ON (CHAR_ITEMS.CHARACTER_ID = CHARACTERS.ID) \
                                WHERE CHAR_ITEMS.CHARACTER_ID = {};"

    INSERT_ITEM_STR = "INSERT INTO ITEMS (NAME, DESCRIPTION, AMOUNT) VALUES('{}', '{}', {}) RETURNING ID;"
    INSERT_CHARACTER_ITEM_STR = "INSERT INTO CHAR_ITEMS (CHARACTER_ID, ITEM_ID) VALUES({}, {});"

    UPDATE_ITEM_STR = "UPDATE ITEMS SET (NAME, DESCRIPTION, AMOUNT) = ('{}', '{}', {}) WHERE ITEMS.ID = {};"
    DELETE_ITEM_STR = "DELETE FROM ITEMS WHERE ID = {};"

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
                cur.execute(Item.FIND_ITEM_BY_ID_STR.format(id))
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
                cur.execute(Item.FIND_ALL_FOR_CHARACTER_STR.format(character_id))
                data = cur.fetchall()
                for art_tuple in data:
                    res.append(my_class(art_tuple[1], art_tuple[2], art_tuple[3], art_tuple[0]))
        return res

    def insert(self, character_id):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Item.INSERT_ITEM_STR.format(self.name, self.descr, self.amount))
                new_id = cur.fetchone()[0]
                cur.execute(Item.INSERT_CHARACTER_ITEM_STR.format(character_id, new_id))
                return new_id

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Item.UPDATE_ITEM_STR.format(self.name, self.descr, self.amount, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Item.DELETE_ITEM_STR.format(self.id))
    