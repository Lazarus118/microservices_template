from flask import session
from app import db
from app.models import Api

#************************
#=> POST manager
class PostManager(object):
    def __init__(self):
        pass


    @staticmethod
    def post_req(request):
			
			data = request.args.get('data')
			
			meta_data = request.args.get('meta_data')
			
			status = request.args.get('status')
			
			post = Api( status, meta_data, data)
			
			db.session.add(post)
			
			db.session.commit()
			
			return dict( data, meta_data, status)
