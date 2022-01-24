from fileinput import filename
from msilib.schema import Directory
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
                directory= request.form['directory']
                parent_dir = "C:/Users/Lenovo/OneDrive/Desktop/SFTP/"
                path = os.path.join(parent_dir, directory)
                print(path)
                try:
                    os.makedirs(path, exist_ok = True)
                    print("Directory '%s' created successfully" % directory)
                except OSError as error:
                    print("Directory '%s' can not be created" % directory)
              
                try:
                    os.chdir(path)
                    print("Current working directory: {0}".format(os.getcwd()))
                except FileNotFoundError:
                    print("Directory: {0} does not exist".format(path))
                except NotADirectoryError:
                    print("{0} is not a directory".format(path))
                except PermissionError:
                    print("You do not have permissions to change to {0}".format(path))


                for each_file in files:
                    old_file = os.path.isfile(each_file)
                    if old_file is True:
                        print(each_file,"alredy exist")
                    elif (each_file[-4:]=='.txt','.mp3','.mp4'):
                        # sftp.get(remotepath = '.', localpath=None, callback=None, preserve_mtime=False)
                        
                        sftp.get(each_file)
                        print(each_file,' downloaded successfully ')
                
                return jsonify ("Files Downloaded Successfully")
            sftp.close()

api.add_resource(test,'/test')


  
if __name__ =='__main__':
    app.run(debug=True)



