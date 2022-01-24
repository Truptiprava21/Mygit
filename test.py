from fileinput import filename
from os import getcwd
import pysftp
from flask import Flask, json,jsonify,request
from flask_restful import Resource,Api
import os.path
from os import path
import os


myHostname = "localhost"



app = Flask(__name__)
api = Api(app)



class test(Resource):
    def post(self):
        myUsername = request.form['myUsername']
        myPassword = request.form['myPassword']
        cnopts = pysftp.CnOpts()
        cnopts.hostkeys = None


        with pysftp.Connection(host = myHostname ,port = 22, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
        # Connection = pysftp.Connection(host=myHostname ,port = 22, username=myUsername, password=myPassword, cnopts=cnopts)
            #print(pysftp.Connection)
            print ("Connection succesfully stablished") 

           

            #print(sftp.listdir(remotepath='.'))
            

            
            with sftp.cd(remotepath='.'):
                files = sftp.listdir()
                for each_file in files:
                    old_file = path.isfile(each_file)
                    if old_file is True:
                        print(each_file,"alredy exist")
                    elif (each_file[-4:]=='.txt','.mp3','.mp4'):
                        sftp.get(each_file)
                        print(each_file,' downloaded successfully ')
                
                return jsonify ("Files Downloaded Successfully")
            sftp.close()

api.add_resource(test,'/test')

    
if __name__ =='__main__':
    app.run(debug=True)




