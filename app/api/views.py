from flask import url_for, abort, jsonify, request
from app.api import api
from app import app, db
from app.models import Api
from app.api.wrappers import Manager

#************************************
#=> App Manager
manage = Manager()  

#************************************
#=> HOME
@api.route('/')
def home():
	return jsonify({'home': 'This is the home address, welcome'})

#************************************
#=> GET
@api.route('/get/', methods=['GET'])
def get():
    id = request.args.get('id')	
    response = manage.get.get_req(id)
    return jsonify(data=response)

#***********************************
#=> POST
@api.route('/post/', methods=['POST'])
def post():
    response = manage.post.post_req(request)
    return jsonify(data=response)

#***********************************
#=> UPDATE
@app.route('/update/<int:id>', methods=['PUT'])
def update():
    return jsonify(data=response)

#***********************************
#=> DELETE
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete():
    return jsonify(data=response)

#***********************************
#=> 404 ERROR Page
@app.errorhandler(404)
def page_404(e):
    response = dict(status='FAIL', message='Sorry. We could not find what you are looking for', error=str(e))
    return jsonify(data=response)

#***********************************
#=> 500 ERROR page
@app.errorhandler(500)
def page_500(e):
    response = dict(status='FAIL', message='Oops... something went horribly wrong', error=str(e))
    return jsonify(data=response)
