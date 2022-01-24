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







import os
  
# Directory
directory = "GeeksforGeeks"
  
# Parent Directory path
parent_dir = "D:/Pycharm projects/"
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
os.mkdir(path)
print("Directory '% s' created" % directory)
  
# Directory
directory = "Geeks"
  
# Parent Directory path
parent_dir = "D:/Pycharm projects"
  
# mode
mode = 0o666
  
# Path
path = os.path.join(parent_dir, directory)
  
# Create the directory
# 'GeeksForGeeks' in
# '/home / User / Documents'
# with mode 0o666
os.mkdir(path, mode)
print("Directory '% s' created" % directory)    