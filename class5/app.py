from flask import Flask,render_template,request,redirect,jsonify
from flask_pymongo import PyMongo  #fire base is also good
#pymongo is a driver that connects python to mongodb
app = Flask(__name__)

app.config['MONGO_URI'] = 'mongodb+srv://mubi:1234@cluster001-avto2.mongodb.net/test?retryWrites=true&w=majority'
#mongo = PyMongo(app)

@app.route('/home')
def home():
    return """ <h1>Welcome from homepage</h1>"""

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/signupAuth', methods=["POST"])
def signupAuth():
    data = dict(request.form)
    usersData = mongo.db.usersData
    result = usersData.find_one({"email":data["email"]})
    print(result)
    usersData.insert_one(data)
    return redirect('/login')

@app.route('/<name>')
def show_html(name):
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True,port=5000)

# install robo3T for mongodb app to check your onlie datasets

# user se email or password lena hy or issy mongo db se check kr k login ya phir home pr redirect karwana hy 