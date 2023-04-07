from flask import request, abort
from Application.application import app


import APIHandlers.ExeptionHandler as ExeptionHandler 
from ActiveRecords.Item import Item
from Application.Loging import *
from Application.Constants import *


@app.route('/api/items/get_all/<int:character_id>', methods=['GET'])
def item_get_all(character_id):
    @ExeptionHandler.abort_on_failure()
    def item_get_all_impl(character_id):
        res_json_arr = []
        all_items = Item.from_character_id(character_id)
        for item in all_items:
            res_json_arr.append({ "id": item.id, "name": item.name, "descr": item.descr, "amount": item.amount })
        return res_json_arr
    return item_get_all_impl(character_id)

@app.route('/api/items/add', methods=['POST'])
def item_create():
    @ExeptionHandler.abort_on_failure()
    def item_create_impl():
        api_log("New item '{}' for character {}".format(request.json["name"], request.json["character_id"]))
        new_art = Item(request.json["name"], request.json["descr"], request.json["amount"])
        new_id = new_art.insert(request.json["character_id"])
        return { "id": new_id }
    return item_create_impl()

# @app.route('/api/items/<int:id>/get', methods=['GET'])
# def item_get(id):
#     @ExeptionHandler.abort_on_failure()
#     def item_get_impl(id):
#         api_log("Get request for character " + str(id))
#         art = Artifact.from_id(id)
#         return { "id": art.id, "name": art.name, "charges": art.charges, "used_charges": art.used_charges, "descr": art.descr }
#     return item_get_impl(id)

# @app.route('/api/items/<int:id>/set', methods=['POST'])
# def item_set(id):
#     @ExeptionHandler.abort_on_failure()
#     def item_set_impl(id):
#         api_log("Set request for character " + str(id))
#         edited_art = Artifact(request.json["name"], request.json["charges"], request.json["used_charges"], request.json["descr"], id)
#         edited_art.update()
#         return { }
#     return item_set_impl(id)