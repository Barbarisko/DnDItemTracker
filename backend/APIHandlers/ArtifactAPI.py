from flask import request, abort
from application import app


import APIHandlers.ExeptionHandler as ExeptionHandler 
from ActiveRecords.Artifact import Artifact
from Loging import *
from Constants import *


@app.route('/api/artifact/get_all/<int:character_id>', methods=['GET'])
def artifact_get_all(character_id):
    @ExeptionHandler.abort_on_failure()
    def artifact_get_all_impl(character_id):
        res_json_arr = []
        all_artifacts = Artifact.from_character_id(character_id)
        for art in all_artifacts:
            res_json_arr.append({ "id": art.id, "name": art.name, "charges": art.charges, "used_charges": art.used_charges, "descr": art.descr })
        return res_json_arr
    return artifact_get_all_impl(character_id)

@app.route('/api/artifact/add', methods=['POST'])
def artifact_create():
    @ExeptionHandler.abort_on_failure()
    def artifact_create_impl():
        api_log("New artifact '{}' for user {}".format(request.json["name"], request.json["character_id"]))
        new_art = Artifact(request.json["name"], request.json["charges"], request.json["used_charges"], request.json["descr"])
        new_id = new_art.insert(request.json["character_id"])
        return { "id": new_id }
    return artifact_create_impl()

@app.route('/api/artifact/<int:id>/get', methods=['GET'])
def artifact_get(id):
    @ExeptionHandler.abort_on_failure()
    def artifact_get_impl(id):
        api_log("Get request for user " + str(id))
        art = Artifact.from_id(id)
        return { "id": art.id, "name": art.name, "charges": art.charges, "used_charges": art.used_charges, "descr": art.descr }
    return artifact_get_impl(id)

@app.route('/api/artifact/<int:id>/set', methods=['POST'])
def artifact_set(id):
    @ExeptionHandler.abort_on_failure()
    def artifact_set_impl(id):
        api_log("Set request for user " + str(id))
        edited_art = Artifact(request.json["name"], request.json["charges"], request.json["used_charges"], request.json["descr"], id)
        edited_art.update()
        return { }
    return artifact_set_impl(id)