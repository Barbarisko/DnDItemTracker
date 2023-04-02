from flask import Flask, request, abort
app = Flask(__name__)

import APIHandlers.ExeptionHandler as ExeptionHandler 
from ActiveRecords.Character import Character
from Loging import *
from Constants import *


@app.route('/api/character/get_all/<int:user_id>', methods=['GET'])
def character_get_all(user_id):
    @ExeptionHandler.abort_on_failure()
    def character_get_all_impl(user_id):
        return {}
    return character_get_all_impl(user_id)

@app.route('/api/character/add', methods=['POST'])
def character_create():
    @ExeptionHandler.abort_on_failure()
    def character_create_impl():
        api_log("New character '{}' for user {}".format(request.json["name"], request.json["user_id"]))
        new_ch = Character(request.json["name"], request.json["level"], request.json["class"])
        new_id = new_ch.insert(request.json["user_id"])
        return { "id": new_id }
    return character_create_impl()

@app.route('/api/character/<int:id>/get', methods=['GET'])
def character_get(id):
    @ExeptionHandler.abort_on_failure()
    def character_get_impl(id):
        api_log("Get request for user " + str(id))
        ch = Character.from_id(id)
        return { "id": ch.id, "name": ch.name, "level": ch.level, "class": ch.class_name }
    return character_get_impl(id)

@app.route('/api/character/<int:id>/set', methods=['POST'])
def character_set(id):
    @ExeptionHandler.abort_on_failure()
    def character_set_impl(id):
        api_log("Set request for user " + str(id))
        edited_ch = Character(request.json["name"], request.json["level"], request.json["class"], id)
        edited_ch.update()
        return { }
    return character_set_impl(id)