from ActiveRecords.Object import Object
from ConnectionManager import ConnectionManager
from Constants import *

class Artifact(Object):
    FIND_ARTIFACT_BY_ID_STRING = "SELECT * FROM ARTIFACTS WHERE ARTIFACTS.ID = {};"
    # FIND_ARTIFACT_BY_IDS_STRING = "SELECT * FROM ARTIFACTS WHERE ARTIFACTS.ID = {};"
    INSERT_ARTIFACT_STRING = "INSERT INTO ARTIFACTS (NAME, CHARGES, USED_CHARGES, DESCR) VALUES('{}', {}, {}, '{}');"
    UPDATE_ARTIFACT_STRING = "UPDATE ARTIFACTS SET (NAME, CHARGES, USED_CHARGES, DESCR) VALUES('{}', {}, {}, '{}') WHERE ARTIFACTS.ID = {};"
    DELETE_ARTIFACT_STRING = "DELETE FROM ARTIFACTS WHERE ID = {};"

    def __init__(self, id):
        super(id)
        self.name = ""
        self.charges = 0
        self.used_charges = 0
        self.descr = ""
        # Find by ID
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Artifact.FIND_ARTIFACT_BY_ID_STRING.format(id))
                data = cur.fetchone()
                self.id = data[0]
                self.name = data[1]
                self.charges = data[2]
                self.used_charges = data[3]
                self.descr = data[4]

    def __init__(self, name, charges, used_charges, descr, id = INVALID_ID):
        super(id)
        self.name = name
        self.charges = charges
        self.used_charges = used_charges
        self.descr = descr
    
    # @classmethod
    # def from_ids(this_class, ids):
    #     request_res = []
    #     with ConnectionManager() as manager:
    #         with manager.get_cursor() as cur:
    #             cur.execute(Artifact.FIND_ARTIFACT_BY_ID_STRING.format(id))
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
                cur.execute(Artifact.INSERT_ARTIFACT_STRING.format(self.name, self.charges, self.used_charges, self.descr))

    def update(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Artifact.UPDATE_ARTIFACT_STRING.format(self.name, self.charges, self.used_charges, self.descr, self.id))

    def delete(self):
        with ConnectionManager() as manager:
            with manager.get_cursor() as cur:
                cur.execute(Artifact.DELETE_ARTIFACT_STRING.format(self.id))
    