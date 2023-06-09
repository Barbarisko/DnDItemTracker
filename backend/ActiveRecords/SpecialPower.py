from ActiveRecords.Object import Object
from Application.ConnectionManager import ConnectionManager
from Application.Constants import *

class SpecialPower(Object):
    FIND_SPECIAL_POWER_BY_ID_STR = "SELECT * FROM SPECIAL_POWERS WHERE SPECIAL_POWERS.ID = {};"
    FIND_ALL_FOR_CHARACTER_STR = "SELECT a.id, a.name, a.charges, a.used_charges FROM SPECIAL_POWERS as a \
                                LEFT JOIN CHAR_POWERS ON (a.ID = CHAR_POWERS.POWER_ID) \
                                LEFT JOIN CHARACTERS ON (CHAR_POWERS.CHARACTER_ID = CHARACTERS.ID) \
                                WHERE CHAR_POWERS.CHARACTER_ID = {};"

    INSERT_SPECIAL_POWER_STR = "INSERT INTO SPECIAL_POWERS (NAME, CHARGES, USED_CHARGES) VALUES('{}', {}, {}) RETURNING ID;"
    INSERT_CHARACTER_SPECIAL_POWER_STR = "INSERT INTO CHAR_POWERS (CHARACTER_ID, POWER_ID) VALUES({}, {});"

    UPDATE_SPECIAL_POWER_STR = "UPDATE SPECIAL_POWERS SET (NAME, CHARGES, USED_CHARGES) = ('{}', {}, {}) WHERE SPECIAL_POWERS.ID = {};"
    DELETE_SPECIAL_POWER_STR = "DELETE FROM SPECIAL_POWERS WHERE ID = {};"

    def __init__(self, name, charges, used_charges, id = INVALID_ID):
        super().__init__(id)
        self.name = name
        self.charges = charges
        self.used_charges = used_charges

    @classmethod
    def from_id(my_class, id):
        res_id = INVALID_ID
        name = ""
        charges = 0
        used_charges = 0
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpecialPower.FIND_SPECIAL_POWER_BY_ID_STR.format(id))
                data = cur.fetchone()
                res_id = data[0]
                name = data[1]
                charges = data[2]
                used_charges = data[3]
        return my_class(name, charges, used_charges, res_id)
    
    @classmethod
    def from_character_id(my_class, character_id):
        res = []
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpecialPower.FIND_ALL_FOR_CHARACTER_STR.format(character_id))
                data = cur.fetchall()
                for art_tuple in data:
                    res.append(my_class(art_tuple[1], art_tuple[2], art_tuple[3], art_tuple[0]))
        return res

    def insert(self, character_id):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpecialPower.INSERT_SPECIAL_POWER_STR.format(self.name, self.charges, self.used_charges))
                new_id = cur.fetchone()[0]
                cur.execute(SpecialPower.INSERT_CHARACTER_SPECIAL_POWER_STR.format(character_id, new_id))
                return new_id

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpecialPower.UPDATE_SPECIAL_POWER_STR.format(self.name, self.charges, self.used_charges, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpecialPower.DELETE_SPECIAL_POWER_STR.format(self.id))
    