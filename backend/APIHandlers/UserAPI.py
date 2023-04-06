from flask import request, abort
from application import app

import APIHandlers.ExeptionHandler as ExeptionHandler 
from ActiveRecords.User import User
from Loging import *
from Constants import *


@app.route('/api/user/login', methods=['POST'])
def user_login():
    @ExeptionHandler.abort_on_failure()
    def user_login_impl():
        api_log("New login request for " + request.json["username"])
        user = User.from_username(request.json["username"])
        if user.password_hash == request.json["password_hash"]:
            return { "id": user.id }
        abort(400)
    return user_login_impl()


@app.route('/api/user/create', methods=['POST'])
def user_create():
    @ExeptionHandler.abort_on_failure()
    def user_create_impl():
        api_log("New registration request for " + request.json["username"])
        new_user = User(request.json["username"], request.json["password_hash"], request.json["is_pidr"])
        new_id = new_user.insert()
        return { "id": new_id }
    return user_create_impl()

 
@app.route('/api/user/<int:id>/get', methods=['GET'])
def user_get(id):
    @ExeptionHandler.abort_on_failure()
    def user_get_impl(id):
        api_log("Get request for user " + str(id))
        user = User.from_id(id)
        return { "id": user.id, "username": user.username, "is_pidr": user.is_pidr }
    return user_get_impl(id)