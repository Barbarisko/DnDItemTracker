from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *

class SpellLevel(Object):
    FIND_SPELL_LEVELS_BY_ID_STR = "SELECT * FROM SPELL_LEVELS WHERE SPELL_LEVELS.ID = {};"
    FIND_ALL_FOR_CHARACTER_STR = "SELECT a.id, a.level, a.charges, a.used_charges FROM SPELL_LEVELS as a \
                                LEFT JOIN CHAR_SPELLS ON (a.ID = CHAR_SPELLS.SPELL_ID) \
                                LEFT JOIN CHARACTERS ON (CHAR_SPELLS.CHARACTER_ID = CHARACTERS.ID) \
                                WHERE CHAR_SPELLS.CHARACTER_ID = {};"

    INSERT_SPELL_LEVELS_STR = "INSERT INTO SPELL_LEVELS (\"level\", CHARGES, USED_CHARGES) VALUES({}, {}, {}) RETURNING ID;"
    INSERT_CHARACTER_SPELL_LEVELS_STR = "INSERT INTO CHAR_SPELLS (CHARACTER_ID, SPELL_ID) VALUES({}, {});"

    UPDATE_SPELL_LEVELS_STR = "UPDATE SPELL_LEVELS SET (LEVEL, CHARGES, USED_CHARGES) = ({}, {}, {}) WHERE SPELL_LEVELS.ID = {};"
    DELETE_SPELL_LEVELS_STR = "DELETE FROM SPELL_LEVELS WHERE ID = {};"

    def __init__(self, level, charges, used_charges, id = INVALID_ID):
        super().__init__(id)
        self.level = level
        self.charges = charges
        self.used_charges = used_charges

    @classmethod
    def from_id(my_class, id):
        res_id = INVALID_ID
        level = 0
        charges = 0
        used_charges = 0
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpellLevel.FIND_SPELL_LEVELS_BY_ID_STR.format(id))
                data = cur.fetchone()
                res_id = data[0]
                level = data[1]
                charges = data[2]
                used_charges = data[3]
        return my_class(level, charges, used_charges, res_id)
    
    @classmethod
    def from_character_id(my_class, character_id):
        res = []
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpellLevel.FIND_ALL_FOR_CHARACTER_STR.format(character_id))
                data = cur.fetchall()
                for spell_tuple in data:
                    res.append(my_class(spell_tuple[1], spell_tuple[2], spell_tuple[3], spell_tuple[0]))
        return res

    def insert(self, character_id):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpellLevel.INSERT_SPELL_LEVELS_STR.format(self.level, self.charges, self.used_charges))
                new_id = cur.fetchone()[0]
                cur.execute(SpellLevel.INSERT_CHARACTER_SPELL_LEVELS_STR.format(character_id, new_id))
                return new_id

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpellLevel.UPDATE_SPELL_LEVELS_STR.format(self.level, self.charges, self.used_charges, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(SpellLevel.DELETE_SPELL_LEVELS_STR.format(self.id))
    