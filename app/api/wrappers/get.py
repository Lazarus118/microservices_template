from app import db
from app.models import Api

#************************
#=> GET manager
class GetManager(object):
    def __init__(self):
        pass

    @staticmethod
    def get_req(id):
	api_data = Api.query.all()
        	
        if not api_data:
            return dict(status='FAIL', message='No such data.',
			request_args=dict(id=id))
             
	return [i.serialize for i in api_data]

