from flask import request, abort
from Application.application import app


import APIHandlers.ExeptionHandler as ExeptionHandler 
from ActiveRecords.Consumable import Consumable
from Application.Loging import *
from Application.Constants import *


@app.route('/api/consumables/get_all/<int:character_id>', methods=['GET'])
def consumable_get_all(character_id):
    @ExeptionHandler.abort_on_failure()
    def consumable_get_all_impl(character_id):
        res_json_arr = []
        all_consumables = Consumable.from_character_id(character_id)
        for cons in all_consumables:
            res_json_arr.append({ "id": cons.id, "name": cons.name, "descr": cons.descr, "amount": cons.amount })
        return res_json_arr
    return consumable_get_all_impl(character_id)

@app.route('/api/consumables/add', methods=['POST'])
def consumable_create():
    @ExeptionHandler.abort_on_failure()
    def consumable_create_impl():
        api_log("New consumable '{}' for character {}".format(request.json["name"], request.json["character_id"]))
        new_art = Consumable(request.json["name"], request.json["descr"], request.json["amount"])
        new_id = new_art.insert(request.json["character_id"])
        return { "id": new_id }
    return consumable_create_impl()

# @app.route('/api/consumables/<int:id>/get', methods=['GET'])
# def consumable_get(id):
#     @ExeptionHandler.abort_on_failure()
#     def consumable_get_impl(id):
#         api_log("Get request for character " + str(id))
#         art = Artifact.from_id(id)
#         return { "id": art.id, "name": art.name, "charges": art.charges, "used_charges": art.used_charges, "descr": art.descr }
#     return consumable_get_impl(id)

@app.route('/api/consumables/<int:id>/set', methods=['POST'])
def consumable_set(id):
    @ExeptionHandler.abort_on_failure()
    def consumable_set_impl(id):
        api_log("Set Consumable request for character " + str(id))
        edited_art = Consumable(request.json["name"], request.json["descr"], request.json["amount"], id)
        edited_art.update()
        return { }
    return consumable_set_impl(id)