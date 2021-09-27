from flask import Flask,render_template,request
import pyrebase

Config={'apiKey': "AIzaSyCPtnaLWWVt05BopqxMgw2_3tux7fvUvzA",
  'authDomain': "myfirstproject-fde41.firebaseapp.com",
  'databaseURL': "https://myfirstproject-fde41-default-rtdb.firebaseio.com",
  'projectId': "myfirstproject-fde41",
  'storageBucket': "myfirstproject-fde41.appspot.com",
  'messagingSenderId': "873580657824",
  'appId': "1:873580657824:web:30d1908014c06b377c5dc5",
  'measurementId': "G-ZF0P86K23Y"}

firebase=pyrebase.initialize_app(Config)
#db= firebase.database()
auth=firebase.auth()

app= Flask(__name__)

@app.route("/")
@app.route("/register")

def basic():
    return render_template("register.html")
@app.route('/display',methods=["POST","GET"])

def mydisplay():
    if request.method=="POST":
        e=request.form.get("email")
        p=request.form.get("password")
        response=auth.sign_in_with_email_and_password(e,p)
        print(response)
    return render_template('/display.html',email=e,password=p)

if __name__ ==  '__main__':
    app.run(debug=True)
