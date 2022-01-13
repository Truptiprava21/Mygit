from os import name
from flask import Flask, json,jsonify,request
from flask_restful import Resource,Api
import pymongo

myclient = pymongo.MongoClient("mongodb+srv://root:root@cluster0.2ojce.mongodb.net/test")
mydatabase = myclient["userdatabase"]
usercollection = mydatabase["usercol"]

app = Flask(__name__)
api = Api(app)


class Registration(Resource):
    def post(self):
        uname = request.form['uname']
        pword = request.form['pword']
        email = request.form['email']
        contact = request.form['contact']
        DOB = request.form['DOB']
        
        if " " in uname:
            message='user name must be in alphanumeric'
            return message
    
        if str(contact).isdigit():
            s=str(contact)
            t=s.split()
            c=0
            for x in t:
                for i in x:
                    c=c+1
            if c!=10:
                message = 'Contact number must be 10 digit !'
                return message

        if not email.endswith('@gmail.com'):
            message = 'incorrect email format'
            return message
        usercollection.insert_one({"name" : uname , "email" : email, "contact" : contact, "DOB" : DOB, "password" : pword})
        return jsonify("Thanks for Registration")




    def get(self):
        user_email = request.args.get("email")
        user = list(usercollection.find({"email": user_email}))
        print(user)
        return jsonify ("Userdetails")




    def put(self):
        user_email = request.args.get("email")
        user = list(usercollection.find({"email": user_email}))
        print(user)
        
        uname = request.form['uname']
        DOB = request.form['DOB']
        predetails = {"name":user[0]['name']}
        newdetails = {"$set":{"name":uname, "DOB":DOB}}
        usercollection.update_one(predetails,newdetails)
        message = "user update Sucessfully"
        return jsonify(message)


    def delete(self):
        username = request.form['username']

        for user in usercollection.find():
            pass
        if username!=user['name']:
            return jsonify ("user is not Available")
        else:
            usercollection.delete_one(user)
            return jsonify ("User is Succesfully Deleted!")

    
class Login(Resource):
    def post(self):
        username = request.form['username']
        password = request.form['password']
        print(username,password)

        for test in usercollection.find({},{"_id": 0,"name":1, "password":1}):
            print(test,"db result")
            pass

        if username!=test['name'] or password!=test['password']:
            return jsonify("Wrong username or Password")

    # access_token = create_access_token(identity=username)
        return jsonify("Login Succeeded!")



api.add_resource(Registration,'/')
api.add_resource(Login,'/login')

if __name__ =='__main__':
    app.run(debug=True)