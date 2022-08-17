import requests
def check_version():
    f = open("./DataBase/database.ini",'r+')
    version = f.read()
    f.close()
    url = "http://101.34.173.17:5000/database/version?version=" + version
    response = requests.get(url)
    if(response.status_code == 200):
        content = response.text
        if content == 'False':
            return False
        return True
    else:
        return True
def update_version():
    url = 'http://101.34.173.17:5098/database.pvsd'
    res = requests.get(url)
    with open('./DataBase/database.pvsd', 'w+') as f:
        f.write(res.content)
    url = 'http://101.34.173.17:5000/database/get_version'
    response = requests.get(url)
    with open('./DataBase/database.ini', 'w+') as f:
        f.write(response.content)