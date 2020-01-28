from flask import Flask, render_template , redirect,request,jsonify
from flask_pymongo import PyMongo  #fire base is also good

app = Flask(__name__)
"""app.config['MONGO_URI'] = 'mongodb+srv://mubi:1234@cluster001-avto2.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)
print(mongo)"""

users = [
    {
        "name": "ali",
        "password": "abc"
    },
    {
        "name": "hussain",
        "password": "abc1"
    },
    {
        "name": "ali1",
        "password": "abc1"
    },{
        "name": "ali2",
        "password": "abc2"
    },
    {
        "name": "ali3",
        "password": "abc4"
    },
    {
        "name": "ali4",
        "password": "abc4"
    },
    {
        "name": "ali5",
        "password": "abc5"
    },
    {
        "name": "ali6",
        "password": "abc7"
    },
]

@app.route('/')
def index():
    # response is importent
    return jsonify({"messege":"hello from jsonify"}) #convert dictionary to json format

@app.route('/test',methods=["POST"])
def test():
    #data = request.form
    data = dict(data)
    for i, v in enumerate(users):
        if(data['userName'] == v['name'] and data['password'] == v['password']):
            #logging_in = mongo.db.logging_in
            #result = logging_in.insert_one(data)
            #print(result.inserted_id)
            return redirect('http://127.0.0.1:5000/home')
    return redirect('http://127.0.0.1:5000/login')

if __name__ ==  "__main__":
    app.run(debug=True ,port=5001)