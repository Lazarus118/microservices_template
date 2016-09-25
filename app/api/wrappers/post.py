from flask import session
from app import db
from app.models import Api
import pickle 

#************************
#=> POST manager
class PostManager(object):
    def __init__(self):
        pass


    @staticmethod
    def post_req(request):
        try:
            '''
                Serialization and Deserialization of json 
                data Strings
                Tested in POSTMAN (raw body) with
                {
                    "data": "some text of some data"
                }

            '''
            data = request.get_json()
            data_serializedString = pickle.dumps( data )
            data_deserialized = pickle.loads( data_serializedString )
            for key in data_deserialized:
                '''
                    Save Deserialized json data Strings
                    to Db 
                '''
                post = Api( "OK", "[]", data_deserialized[key] )
                db.session.add(post)
                db.session.commit()
            '''
                Return Output and/or Error 
            '''               
            return dict(data)

        except Exception as e:
                return dict(
                    status='FAIL',
                    message='Could not create that post.',
                    error=str(e))
