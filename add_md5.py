
import hashlib
import sys
import os

def get_file_data(file_name) :
    file_object=open(file_name,'rb')
    file_data=file_object.read()
    file_object.close()
    return file_data

def get_md5(data) :
    md5=hashlib.md5()
    md5.update(data)
    return md5.hexdigest()
    
def get_sha1(data) :
    sha1=hashlib.sha1()
    sha1.update(data)
    return sha1.hexdigest()
    
def get_sha256(data) :
    sha256=hashlib.sha256()
    sha256.update(data)
    return sha256.hexdigest()
    
def get_file_md5(file_name) :
    return get_md5(get_file_data(file_name))

def get_file_sha1(file_name) :
    return get_sha1(get_file_data(file_name))

def get_file_sha256(file_name) :
    return get_sha256(get_file_data(file_name))


#print(get_file_md5(raw_input("filename:")))

root = 'Virus Tools'
path = os.path.join(root)
pathnames = []
for (dirpath, dirnames, filenames) in os.walk(path):
    for filename in filenames:
        pathnames += [os.path.join(dirpath, filename)]
for file in pathnames:
    if file.endswith('.exe'):
        print get_file_md5(file.decode('gbk').encode('gbk')) + ';' + 'Win32.HackTool' # Change it

