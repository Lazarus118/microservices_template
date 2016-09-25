from app import db


#*************************************************************************************#
# // API database class 
#*************************************************************************************#
class Api(db.Model):
    __tablename__ = 'api'
	
    id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(512), index=True)
    meta_data = db.Column(db.String(512), index=True)
    data = db.Column(db.String(512), index=True)

    @property
    def serialize(self):
        return { 
                'status': self.status,
                'meta_data': self.meta_data,     
                'data': self.data 
                }  	 	 	 				 


    def __init__(self, status, meta_data, data):    
        self.status = status
        self.meta_data = meta_data
        self.data = data 
      
    

