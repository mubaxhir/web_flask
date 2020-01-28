from flask import Flask, render_template , redirect,request,jsonify
from flask_pymongo import PyMongo  #fire base is also good

app = Flask(__name__)
"""app.config['MONGO_URI'] = 'mongodb+srv://mubi:1234@cluster001-avto2.mongodb.net/test?retryWrites=true&w=majority'
mongo = PyMongo(app)
print(mongo)"""

database={"aman":'1',"mubashir":'2',"furqan":'3',"jawwad":'4',"yousuf":'5',"ali":'6',
"nasir":'1',"hanuman":'2',"shehazd":'3',"hamza":'4'}

@app.route('/')
def index():
    # response is importent
    return jsonify({"messege":"hello from jsonify"}) #convert dictionary to json format

@app.route('/test',methods=["POST"])
def test():
    #data = request.form
    data = dict(data)
    if data['username'] in database:
        if  data['password']==database[data['username']] :
            #logging_in = mongo.db.logging_in
            #result = logging_in.insert_one(data)
            #print(result.inserted_id)
            return redirect('http://127.0.0.1:5000/home')
    return redirect('http://127.0.0.1:5000/login')
if __name__ ==  "__main__":
    app.run(debug=True ,port=5001)