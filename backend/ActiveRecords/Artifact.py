from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *

class Artifact(Object):
    FIND_ARTIFACT_BY_ID_STR = "SELECT * FROM ARTIFACTS WHERE ARTIFACTS.ID = {};"
    FIND_ALL_FOR_CHARACTER_STR = "SELECT a.id, a.name, a.charges, a.used_charges, a.description FROM ARTIFACTS as a \
                                LEFT JOIN CHAR_ARTIFACTS ON (a.ID = CHAR_ARTIFACTS.ARTIFACT_ID) \
                                LEFT JOIN CHARACTERS ON (CHAR_ARTIFACTS.CHARACTER_ID = CHARACTERS.ID) \
                                WHERE CHAR_ARTIFACTS.CHARACTER_ID = {};"

    INSERT_ARTIFACT_STR = "INSERT INTO ARTIFACTS (NAME, CHARGES, USED_CHARGES, DESCRIPTION) VALUES('{}', {}, {}, '{}') RETURNING ID;"
    INSERT_CHARACTER_ARTIFACT_STR = "INSERT INTO CHAR_ARTIFACTS (CHARACTER_ID, ARTIFACT_ID) VALUES({}, {});"

    UPDATE_ARTIFACT_STR = "UPDATE ARTIFACTS SET (NAME, CHARGES, USED_CHARGES, DESCRIPTION) = ('{}', {}, {}, '{}') WHERE ARTIFACTS.ID = {};"
    DELETE_ARTIFACT_STR = "DELETE FROM ARTIFACTS WHERE ID = {};"

    def __init__(self, name, charges, used_charges, descr, id = INVALID_ID):
        super().__init__(id)
        self.name = name
        self.charges = charges
        self.used_charges = used_charges
        self.descr = descr

    @classmethod
    def from_id(my_class, id):
        res_id = INVALID_ID
        name = ""
        charges = 0
        used_charges = 0
        descr = ""
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Artifact.FIND_ARTIFACT_BY_ID_STR.format(id))
                data = cur.fetchone()
                res_id = data[0]
                name = data[1]
                charges = data[2]
                used_charges = data[3]
                descr = data[4]
        return my_class(name, charges, used_charges, descr, res_id)
    
    @classmethod
    def from_character_id(my_class, character_id):
        res = []
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Artifact.FIND_ALL_FOR_CHARACTER_STR.format(character_id))
                data = cur.fetchall()
                for art_tuple in data:
                    res.append(my_class(art_tuple[1], art_tuple[2], art_tuple[3], art_tuple[4], art_tuple[0]))
        return res

    def insert(self, character_id):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Artifact.INSERT_ARTIFACT_STR.format(self.name, self.charges, self.used_charges, self.descr))
                new_id = cur.fetchone()[0]
                cur.execute(Artifact.INSERT_CHARACTER_ARTIFACT_STR.format(character_id, new_id))
                return new_id

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Artifact.UPDATE_ARTIFACT_STR.format(self.name, self.charges, self.used_charges, self.descr, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Artifact.DELETE_ARTIFACT_STR.format(self.id))
    