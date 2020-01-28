from flask import Flask, render_template, request, redirect
import bcrypt
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://mubi:1234@cluster001-avto2.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)
print(mongo)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/home',methods=["POST"])
def home():
    return """<h1>Hello from Home Page</h1>"""

@app.route('/signupAuth', methods=["POST"])
def signupAuth():
    data = dict(request.form)
    print(data)
    usersData = mongo.db.usersData
    result = usersData.find_one({"email": data['email']})
    print(result)
    if(result):
        return redirect('/signup')
    bcrypt_password = bcrypt.hashpw(data['password'].encode('utf8'),bcrypt.gensalt(12))
    data['password'] = bcrypt_password
    usersData.insert_one(data)
    return redirect('/login')

@app.route('/loginAuth',methods=["POST"])
def loginAuth():
    data =dict(request.form)
    usersData = mongo.db.usersData
    findEmail = usersData.find_one({"email":data['email']})

    if(findEmail):
        checkPassword = bcrypt.checkpw(data['password'].encode('utf8'),findEmail['password'])
        if(checkPassword):
            return redirect('/home')
        return redirect('/login')
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True)