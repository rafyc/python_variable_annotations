#!/usr/bin/env python3
'''
'''

from flask import Flask, jsonify, redirect, request, abort, make_response
from auth import Auth


app = Flask(__name__)
AUTH = Auth()


@app.route('/')
def hello_world():
    '''Main
    '''
    return jsonify(message='Bienvenue')


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email=email, password=password)
        return jsonify(email=email, message='user created')
    except ValueError:
        return jsonify(message='email already registered'), 400


@app.route('/sessions', methods=['POST'], strict_slashes=False)
def login() -> str:
    ''' POST on session
    '''
    email: str = request.form.get('email')
    password: str = request.form.get('password')
    if not email or not password:
        return abort(401)

    check: bool = AUTH.valid_login(email=email, password=password)
    if not check:
        abort(401)

    session_id: str = AUTH.create_session(email=email)
    res = jsonify(email=email, message='logged in')
    res.set_cookie('session_id', session_id)
    return res

@app.route("/sessions", methods=['DELETE'], strict_slashes=False)
def logout():
    """ DELETE /sessions """
    session_id = request.cookies.get("session_id")
    if not session_id:
        abort(403)

    try:
        user = AUTH.get_user_from_session_id(session_id)
        AUTH.destroy_session(user_id=user.id)
        return make_response(redirect("/", 302))
    except Exception:
        return abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
