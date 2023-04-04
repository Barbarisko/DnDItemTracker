from flask import request, abort
from application import app


import APIHandlers.ExeptionHandler as ExeptionHandler 
from ActiveRecords.SpecialPower import SpecialPower
from Loging import *
from Constants import *


@app.route('/api/special_powers/get_all/<int:character_id>', methods=['GET'])
def special_power_get_all(character_id):
    @ExeptionHandler.abort_on_failure()
    def special_power_get_all_impl(character_id):
        res_json_arr = []
        all_powers = SpecialPower.from_character_id(character_id)
        for power in all_powers:
            res_json_arr.append({ "id": power.id, "name": power.name, "charges": power.charges, "used_charges": power.used_charges })
        return res_json_arr
    return special_power_get_all_impl(character_id)

@app.route('/api/special_powers/add', methods=['POST'])
def special_power_create():
    @ExeptionHandler.abort_on_failure()
    def special_power_create_impl():
        api_log("New special_power '{}' for character {}".format(request.json["name"], request.json["character_id"]))
        new_art = SpecialPower(request.json["name"], request.json["charges"], request.json["used_charges"])
        new_id = new_art.insert(request.json["character_id"])
        return { "id": new_id }
    return special_power_create_impl()

# @app.route('/api/special_power/<int:id>/get', methods=['GET'])
# def special_power_get(id):
#     @ExeptionHandler.abort_on_failure()
#     def special_power_get_impl(id):
#         api_log("Get request for character " + str(id))
#         art = Artifact.from_id(id)
#         return { "id": art.id, "name": art.name, "charges": art.charges, "used_charges": art.used_charges, "descr": art.descr }
#     return special_power_get_impl(id)

# @app.route('/api/special_power/<int:id>/set', methods=['POST'])
# def special_power_set(id):
#     @ExeptionHandler.abort_on_failure()
#     def special_power_set_impl(id):
#         api_log("Set request for character " + str(id))
#         edited_art = Artifact(request.json["name"], request.json["charges"], request.json["used_charges"], request.json["descr"], id)
#         edited_art.update()
#         return { }
#     return special_power_set_impl(id)