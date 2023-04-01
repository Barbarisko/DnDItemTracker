from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *

class Item(Object):
    FIND_ITEM_BY_ID_STRING = "SELECT * FROM ITEMS WHERE ITEMS.ID = {};"
    INSERT_ITEM_STRING = "INSERT INTO ITEMS (NAME, DESCR, AMOUNT) VALUES('{}', '{}', {});"
    UPDATE_ITEM_STRING = "UPDATE ITEMS SET (NAME, DESCR, AMOUNT) VALUES('{}', '{}', {}) WHERE ITEMS.ID = {};"
    DELETE_ITEM_STRING = "DELETE FROM ITEMS WHERE ID = {};"

    def __init__(self, id):
        super(id)
        self.name = ""
        self.descr = ""
        self.amount = 0
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Item.FIND_ITEM_BY_ID_STRING.format(id))
                data = cur.fetchone()
                self.id = data[0]
                self.name = data[1]
                self.descr = data[2]
                self.amount = data[3]

    def __init__(self, name, descr, amount, id = INVALID_ID):
        super(id)
        self.name = name
        self.descr = descr
        self.amount = amount
    
    def insert(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Item.INSERT_ITEM_STRING.format(self.name, self.descr, self.amount))

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Item.UPDATE_ITEM_STRING.format(self.name, self.descr, self.amount, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Item.DELETE_ITEM_STRING.format(self.id))
    