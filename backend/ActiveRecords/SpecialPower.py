from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *

class SpecialPower(Object):
    FIND_SPECIAL_POWER_BY_ID_STRING = "SELECT * FROM SPECIAL_POWERS WHERE SPECIAL_POWERS.ID = {};"
    # FIND_SPECIAL_POWER_BY_IDS_STRING = "SELECT * FROM SPECIAL_POWERS WHERE SPECIAL_POWERS.ID = {};"
    INSERT_SPECIAL_POWER_STRING = "INSERT INTO SPECIAL_POWERS (NAME, CHARGES, USED_CHARGES) VALUES('{}', {}, {});"
    UPDATE_SPECIAL_POWER_STRING = "UPDATE SPECIAL_POWERS SET (NAME, CHARGES, USED_CHARGES) VALUES('{}', {}, {}) WHERE SPECIAL_POWERS.ID = {};"
    DELETE_SPECIAL_POWER_STRING = "DELETE FROM SPECIAL_POWERS WHERE ID = {};"

    def __init__(self, id):
        super(id)
        self.name = ""
        self.charges = 0
        self.used_charges = 0
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpecialPower.FIND_SPECIAL_POWER_BY_ID_STRING.format(id))
                data = cur.fetchone()
                self.id = data[0]
                self.name = data[1]
                self.charges = data[2]
                self.used_charges = data[3]

    def __init__(self, name, charges, used_charges, id = INVALID_ID):
        super(id)
        self.name = name
        self.charges = charges
        self.used_charges = used_charges
    
    # @classmethod
    # def from_ids(this_class, ids):
    #     request_res = []
    #     with ConnectionManager() as manager:
    #         with manager.get_cursor() as cur:
    #             cur.execute(SpecialPower.FIND_SPECIAL_POWER_BY_ID_STRING.format(id))
    #             request_res = cur.fetchall()
    #     # Find all elements and create classes
    #     result = []
    #     for item in request_res:
    #         id = -1
    #         username = ""
    #         pwd = ""
    #         result.append(this_class(id, username, pwd))
    #     return result

    def insert(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpecialPower.INSERT_SPECIAL_POWER_STRING.format(self.name, self.charges, self.used_charges))

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpecialPower.UPDATE_SPECIAL_POWER_STRING.format(self.name, self.charges, self.used_charges, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpecialPower.DELETE_SPECIAL_POWER_STRING.format(self.id))
    