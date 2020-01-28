from flask import Flask,render_template,request,redirect,jsonify
import bcrypt
from pymongo import ReturnDocument
from flask_pymongo import PyMongo 

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://mubi:1234@cluster001-avto2.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)

@app.route('/')
def index():
    return """ <h1>Welcome</h1>"""

@app.route('/updateUser', methods=["GET","POST"])
def updateUser():
    data = dict(request.json)
    usersData = mongo.db.usersData
    findEmail = usersData.find_one({"email":data['email']})
    
    print(data)
    encrypted_new_password = bcrypt.hashpw(data["new_password"].encode('utf8'),
    bcrypt.gensalt(12))
    print(encrypted_new_password)
    checkPassword = bcrypt.checkpw(data['old_password'].encode('utf8'),
    findEmail['password'])    

    result = usersData.find_one({"email":data["email"]})
    if (findEmail):    
        if (checkPassword):
            result = usersData.find_one_and_update({"email":data["email"]},
            {"$set":{"password":encrypted_new_password}})
            print(result)
            return "done"
    else:
        return "not done"

if __name__ == "__main__":
    app.run(debug=True)
