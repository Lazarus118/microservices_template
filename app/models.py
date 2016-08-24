from app import db


#*************************************************************************************#
# //User database class 
#*************************************************************************************#
class User(db.Model):
    __tablename__ = 'user'
	
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), index=True)
    password = db.Column(db.String(64), index=True)
    social_id = db.Column(db.String(64), nullable=True, index=True)
    nickname = db.Column(db.String(64), nullable=True, index=True)
    email = db.Column(db.String(64), index=True)
    user_points = db.Column(db.String(1000), index=True)

    products = db.relationship('Products', backref='user', lazy='dynamic') #______ // Database relational link for Products

    @property
    def serialize(self):
	return {
	    'username': self.username,
	    #'password': self.password,
	    #'social_id': self.social_id,
	    #'nickname': self.nickname,
	    'email': self.email,
	    'products': [i.serialize for i in self.products]
		}  	 	 	 				 


    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_auth_token(self):
        return unicode(hashlib.sha1(self.username +
        self.password).hexdigest())
    def get_id(self):
        return unicode(self.id)
    def __repr__(self):
        return '<User %r>' % (self.username)

    def __init__(self, username, password, email, user_points):
        self.username = username
        self.password = password
        self.email = email
        self.user_points = user_points
      
    

#*************************************************************************************#
# //Product database class 
#*************************************************************************************#		
class Products(db.Model):
    __tablename__ = 'products'
	
    id = db.Column(db.Integer, primary_key=True)
    food = db.Column(db.String(64), index=True)
    drink = db.Column(db.String(64), index=True)
    amount = db.Column(db.String(64), index=True)
    actual_food_amount = db.Column(db.String(64), index=True)
    location = db.Column(db.String(64), index=True)
    #geo = db.Column(db.String(64), index=True)
	
    
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #__________ // ForeignKey link to User

    @property
    def serialize(self):
        return {
	    'id': self.id,
	    'food': self.food,
	    'drink': self.drink,
	    'amount': self.amount,
        'actual_food_amount': self.actual_food_amount,
	    'location': self.location		
        }
	


    			
    def __init__(self, food, drink, amount, location, user_id):
    	self.food = food
    	self.drink = drink
    	self.amount = amount
    	self.location = location
        self.user_id = user_id 


