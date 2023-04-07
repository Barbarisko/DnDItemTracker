from flask import request, abort
from Application.application import app


import APIHandlers.ExeptionHandler as ExeptionHandler 
from ActiveRecords.SpellLevel import SpellLevel
from Application.Loging import *
from Application.Constants import *


@app.route('/api/spell_levels/get_all/<int:character_id>', methods=['GET'])
def spell_level_get_all(character_id):
    @ExeptionHandler.abort_on_failure()
    def spell_level_get_all_impl(character_id):
        res_json_arr = []
        all_levels = SpellLevel.from_character_id(character_id)
        for level in all_levels:
            res_json_arr.append({ "id": level.id, "level": level.level, "charges": level.charges, "used_charges": level.used_charges })
        return res_json_arr
    return spell_level_get_all_impl(character_id)

@app.route('/api/spell_levels/add', methods=['POST'])
def spell_level_create():
    @ExeptionHandler.abort_on_failure()
    def spell_level_create_impl():
        api_log("New spell_level '{}' for character {}".format(request.json["level"], request.json["character_id"]))
        new_art = SpellLevel(request.json["level"], request.json["charges"], request.json["used_charges"])
        new_id = new_art.insert(request.json["character_id"])
        return { "id": new_id }
    return spell_level_create_impl()

# @app.route('/api/spell_level/<int:id>/get', methods=['GET'])
# def spell_level_get(id):
#     @ExeptionHandler.abort_on_failure()
#     def spell_level_get_impl(id):
#         api_log("Get request for character " + str(id))
#         art = Artifact.from_id(id)
#         return { "id": art.id, "name": art.name, "charges": art.charges, "used_charges": art.used_charges, "descr": art.descr }
#     return spell_level_get_impl(id)

@app.route('/api/spell_levels/<int:id>/set', methods=['POST'])
def spell_level_set(id):
    @ExeptionHandler.abort_on_failure()
    def spell_level_set_impl(id):
        api_log("Set request for spell level " + str(id))
        edited_art = SpellLevel(request.json["level"], request.json["charges"], request.json["used_charges"], id)
        edited_art.update()
        return { }
    return spell_level_set_impl(id)