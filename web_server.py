import requests
import brotli
ip = "101.34.173.17" # Change it
def check_version():
    f = open("./DataBase/database.ini",'r+')
    version = f.read()
    f.close()
    url = "http://"+ip+":5000/database/version?version=" + version
    response = requests.get(url)
    if(response.status_code == 200):
        content = response.text
        if content == 'False':
            return False
        return True
    else:
        return True
def update_version():
    url = 'http://'+ ip +':5098/database.pvsd'
    res = requests.get(url)
    data = str(res.content,"utf-8")
    with open('./DataBase/database.pvsd', 'w+', encoding='utf-8') as f:
        f.write(data)
    url = 'http://'+ ip +':5000/database/get_version'
    res = requests.get(url)
    data = str(res.content,"utf-8")
    with open('./DataBase/database.ini', 'w+', encoding='utf-8') as f:
        f.write(data)
def cloud_sumbit(md5):
    url = "http://" + ip + ":5000/cloud/sumbit?hash=" + md5
    response = requests.get(url)
    if(response.status_code == 200):
        content = response.text
        if content == 'True':
            return True
        return False
    else:
        return False