from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/home')
def home():
    return """ <h1>Welcome from homepage</h1>"""

@app.route('/login')
def login():
    return render_template('login.html')

database={"aman":'1',"mubashir":'2',"furqan":'3',"jawwad":'4',"yousuf":'5',"ali":'6',"nasir":'1',"hanuman":'2',"shehazd":'3',"hamza":'4'}

@app.route('/auth', methods=["POST"])
def auth():
    data = request.form
    if data['username'] in database:
        if  data['password']==database[data['username']] :
            return redirect('/home')
        else: return redirect('/login')
    else:
        return redirect('/login')

a = list(range(11))
@app.route('/<name>')
def show_html(name):
    return render_template('index.html',slug=a)

if __name__ == "__main__":
    app.run(debug=True)