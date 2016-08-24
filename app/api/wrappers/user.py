from app import db
from app.models import User


class UserManager(object):
    def __init__(self):
        pass

    @staticmethod
    def get_user(id):
	get_user_data = User.query.all()
        	
        if not get_user_data:
            return dict(status='FAIL', message='No such user.',
			request_args=dict(id=id))
             
	return [i.serialize for i in get_user_data]

