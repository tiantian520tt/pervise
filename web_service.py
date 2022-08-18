#coding:utf-8
import flask, json
from flask import request

version = "699fa638b80ac31d32e9cff8ce6a79e1"

server = flask.Flask(__name__)

@server.route('/database/version', methods=['get'])#'get',
def database_version():
    user_version=request.values.get('version')
    if user_version != version:
        return "False"
    else:
        return "True"

@server.route('/database/get_version', methods=['get'])#'get',
def database_get_version():
    return version

@server.route('/cloud/sumbit', methods=['get'])#'get',
def cloud_sumbit():
    hash = request.values.get('hash') # Get md5 hash
    # Open file        
    fileHandler  =  open  ("H:\\database\\"+hash[0]+".hash",  "r") # Change path (Get it from my index)
    while  True:
        # Get next line from file
        line  =  fileHandler.readline()
        if  not  line  :
            break;
        #print(line.strip())
        if line.strip().lower() == hash.lower():
            fileHandler.close()
            return "True"
    fileHandler.close()
    return "False"
    

    
    
if __name__ == "__main__":
    server.run(host='0.0.0.0', port=5000, debug=True)