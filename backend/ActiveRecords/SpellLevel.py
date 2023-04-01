from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *

class SpellLevel(Object):
    FIND_SPELL_LEVEL_BY_ID_STRING = "SELECT * FROM SPELL_LEVELS WHERE SPELL_LEVELS.ID = {};"
    # FIND_SPELL_LEVEL_BY_IDS_STRING = "SELECT * FROM SPELL_LEVELS WHERE SPELL_LEVELS.ID = {};"
    INSERT_SPELL_LEVEL_STRING = "INSERT INTO SPELL_LEVELS (NAME, CHARGES, USED_CHARGES) VALUES({}, {}, {});"
    UPDATE_SPELL_LEVEL_STRING = "UPDATE SPELL_LEVELS SET (NAME, CHARGES, USED_CHARGES) VALUES({}, {}, {}) WHERE SPELL_LEVELS.ID = {};"
    DELETE_SPELL_LEVEL_STRING = "DELETE FROM SPELL_LEVELS WHERE ID = {};"

    def __init__(self, id):
        super(id)
        self.name = 0
        self.charges = 0
        self.used_charges = 0
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpellLevel.FIND_SPELL_LEVEL_BY_ID_STRING.format(id))
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
    #             cur.execute(SpellLevel.FIND_SPELL_LEVEL_BY_ID_STRING.format(id))
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
                cur.execute(SpellLevel.INSERT_SPELL_LEVEL_STRING.format(self.name, self.charges, self.used_charges))

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpellLevel.UPDATE_SPELL_LEVEL_STRING.format(self.name, self.charges, self.used_charges, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpellLevel.DELETE_SPELL_LEVEL_STRING.format(self.id))
    