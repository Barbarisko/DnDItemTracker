from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *

class Consumable(Object):
    FIND_CONSUMABLE_BY_ID_STRING = "SELECT * FROM CONSUMABLES WHERE CONSUMABLES.ID = {};"
    INSERT_CONSUMABLE_STRING = "INSERT INTO CONSUMABLES (NAME, DESCR, AMOUNT) VALUES('{}', '{}', {});"
    UPDATE_CONSUMABLE_STRING = "UPDATE CONSUMABLES SET (NAME, DESCR, AMOUNT) VALUES('{}', '{}', {}) WHERE CONSUMABLES.ID = {};"
    DELETE_CONSUMABLE_STRING = "DELETE FROM CONSUMABLES WHERE ID = {};"

    def __init__(self, id):
        super(id)
        self.name = ""
        self.descr = ""
        self.amount = 0
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Consumable.FIND_CONSUMABLE_BY_ID_STRING.format(id))
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
                cur.execute(Consumable.INSERT_CONSUMABLE_STRING.format(self.name, self.descr, self.amount))

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Consumable.UPDATE_CONSUMABLE_STRING.format(self.name, self.descr, self.amount, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Consumable.DELETE_CONSUMABLE_STRING.format(self.id))
    