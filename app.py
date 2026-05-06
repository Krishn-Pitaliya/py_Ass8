'''
Task1: Make a registration form using flask.
Execution steps are written in README.md file
'''
from flask import Flask,render_template,request

try:
    #Intilize constructor of Flask
    app=Flask(__name__)

    #Mapping
    @app.route('/')

    #Inputs(Registration Page)
    def home():
        return render_template('registration.html')

    #Mapping
    @app.route('/register_successful',methods=['POST','GET'])#to get username from registration page

    #Inputs
    def register():
        uname=request.form.get('uname')
        return render_template('register_successful.html',uname=uname)

except Exception as error:#If any error occur in above code
    print("Error:",error)
