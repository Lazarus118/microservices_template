from flask import url_for, abort
from app.api import api
from flask import jsonify, request
from app import app, db
from app.models import User
from app.api.wrappers import Manager

#************************************
#=> App Manager
manage = Manager()  

#************************************
#=> User route
@api.route('/user/', methods=['GET'])
def user():
    username = request.args.get('id')	
    response = manage.user.get_user(username)
    return jsonify(data=response)

#***********************************
#=> User route with id in url
@app.route('/api/users/<int:id>')
def get_user(id):
    user = User.query.get(id)
    if not user:
        abort(400)
    return jsonify({'username': user.username})



