from flask import Flask, render_template, redirect, request, jsonify

from flask_pymongo import PyMongo

app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://mubi:1234@cluster001-avto2.mongodb.net/test?retryWrites=true&w=majority'

mongo = PyMongo(app)

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
    return jsonify({"message": "Hello from 5001", "users": users})

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/home')
def home():
    return "Hello from Home Page"

@app.route('/auth', methods=["POST"])
def auth():
    data = request.form
    for i, v in enumerate(users):
        if(data['userName'] == v['name'] and data['password'] == v['password']):
            print(i)
            return redirect('/home')
    return redirect('/login')


@app.route('/test', methods=["POST"])
def test():
    data = request.form
    data = dict(data)

    for i, v in enumerate(users):
        if(data['userName'] == v['name'] and data['password'] == v['password']):
            login = mongo.db.login
            result = login.insert_one(data)
            print(result.inserted_id)
            return redirect('/home')
    return redirect('/login')

if __name__ == "__main__":
    app.run(debug=True, port=5001)