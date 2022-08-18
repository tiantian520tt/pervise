import requests
import hashlib
import sys
import os
import time
import color
def check_version(ip):
    f = open("./DataBase/database.ini",'r+')
    version = f.read()
    f.close()
    url = "http://"+ip+":5000/database/version?version=" + version
    try:
        response = requests.get(url)
    except:
        return False
    if(response.status_code == 200):
        return True
    else:
        return False
def update_version(ip):
    url = 'http://'+ ip +':5098/database.pvsd'
    try:
        res = requests.get(url)
    except:
        return False
    if(res.status_code == 200):
        return True
    else:
        return False
def cloud_sumbit(ip):
    url = "http://" + ip + ":5000/cloud/sumbit?hash=1dbcb300991c95658984df661b41f75d"
    try:
        response = requests.get(url)
    except:
        return False
    if(response.status_code == 200):
        content = response.text
        if content == 'True':
            return True
        return False
    else:
        return False
# This script helps you test whether your server is successfully built and its reaction speed.
# Powered by tiantian520tt
# Date : 2022/8/18 15:30
# Usage: python server_test.py [Your Server IP]
# Example: python server_test.py 127.0.0.1
if __name__=='__main__' :
    if len(sys.argv) is 2:
        color.printGreen('[*] Start testing.')
        res = check_version(sys.argv[1])
        if res:
            color.printGreen('[*] Check version module runs successfully.')
        else:
            color.printYellow('[!] Check version module failed to run.')
        res = update_version(sys.argv[1])
        if res:
            color.printGreen('[*] Update module runs successfully.')
        else:
            color.printYellow('[!] Update module failed to run.')
        res = cloud_sumbit(sys.argv[1])
        if res:
            color.printGreen('[*] Cloud Check module runs successfully.')
        else:
            color.printYellow('[!] Cloud Check module failed to run.')
        color.printGreen('[*] Nothing to do.')
    else:
        color.printGreen('[*] This script helps you test whether your server is successfully built and its reaction speed.')
        color.printGreen('[*] Usage: python server_test.py [Your Server IP]')
        color.printGreen('[*] Example: python server_test.py 127.0.0.1')
