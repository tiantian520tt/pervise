#coding:utf-8
import random
import hashlib
import sys
import os
import time
import color
from win10toast import ToastNotifier
import thread
from shutil import copyfile
import web_server
from subprocess import Popen



def MsgBox(title,content):
    toaster = ToastNotifier()
    try:
        toaster.show_toast(title,
                    content,
                    icon_path=None,
                    duration=5,
                    threaded=True)
    except:
        pass
    while toaster.notification_active(): time.sleep(0.1)

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

def search_hash_from_file(file_list) :
    file_object=open('.\\DataBase\\database.pvsd','rb')
    for file_line in file_object :
        if file_line[0]=='#' or len(file_line) is 0 :
            continue
        
        hash_recode=file_line[:file_line.find(';')].lower()
        virus_recode=file_line[file_line.find(';')+1:]

        #print('Now: '+hash_recode)
        #print('Now: '+virus_recode)
        for i in range(len(file_list)) :
            
            file_list_index = file_list[i]
            
            #print('Now: '+str(hash_recode==file_list_index.get('file_md5')))
            #time.sleep(1)
            if hash_recode==file_list_index.get('file_md5') :
                file_list[i]['is_virus']=True
                #print(file_list[i]['is_virus'])
                file_list[i]['virus_infomarion']=virus_recode
                continue
            elif hash_recode==file_list_index.get('file_sha1') :
                file_list[i]['is_virus']=True
                file_list[i]['virus_infomarion']=virus_recode
                continue
            elif hash_recode==file_list_index.get('file_sha256') :
                file_list[i]['is_virus']=True
                file_list[i]['virus_infomarion']=virus_recode
                continue
    file_object.close()
    if len(sys.argv) == 3:
        if sys.argv[2] == 'cloud':
            color.printGreen("[*] The quick scan ends. Cloud scanning is being used for further confirmation.")
            for i in range(len(file_list)) :
                
                file_list_index = file_list[i]
                virus = web_server.cloud_sumbit(file_list_index.get('file_md5'))
                #print('Now: '+str(hash_recode==file_list_index.get('file_md5')))
                #time.sleep(1)
                if virus:
                    file_list[i]['is_virus']=True
                    #print(file_list[i]['is_virus'])
                    file_list[i]['virus_infomarion']="Cloud:Virus"
                    continue
            color.printGreen("[*] The cloud scan has ended. Analyzing report.")
                
    #print(file_list)
    return file_list

def add_file_in_file_list(file_list,file_path) :
    file_index={}
    file_index['file_path']=file_path
    file_index['file_md5']=get_file_md5(file_path)
    file_index['file_sha1']=get_file_sha1(file_path)
    file_index['file_sha256']=get_file_sha256(file_path)
    file_list.append(file_index)

if __name__=='__main__' :
    logo1="""
  ____   U _____ u   ____   __     __           ____   U _____ u 
U|  _"\ u\| ___"|/U |  _"\ u\ \   /"/u  ___    / __"| u\| ___"|/ 
\| |_) |/ |  _|"   \| |_) |/ \ \ / //  |_"_|  <\___ \/  |  _|"   
 |  __/   | |___    |  _ <   /\ V /_,-. | |    u___) |  | |___   
 |_|      |_____|   |_| \_\ U  \_/-(_/U/| |\u  |____/>> |_____|  
 ||>>_    <<   >>   //   \\_  //   .-,_|___|_,-.)(  (__)<<   >>  
(__)__)  (__) (__) (__)  (__)(__)   \_)-' '-(_/(__)    (__) (__) 
    """
    logo2="""
 _______                                 __                     
|       \                               |  \                    
| $$$$$$$\  ______    ______  __     __  \$$  _______   ______  
| $$__/ $$ /      \  /      \|  \   /  \|  \ /       \ /      \ 
| $$    $$|  $$$$$$\|  $$$$$$\\\$$\ /  $$| $$|  $$$$$$$|  $$$$$$\\
| $$$$$$$ | $$    $$| $$   \$$ \$$\  $$ | $$ \$$    \ | $$    $$
| $$      | $$$$$$$$| $$        \$$ $$  | $$ _\$$$$$$\| $$$$$$$$
| $$       \$$     \| $$         \$$$   | $$|       $$ \$$     \\
 \$$        \$$$$$$$ \$$          \$     \$$ \$$$$$$$   \$$$$$$$
                                                                                                                         
    """
    logo3="""
     _ __       ,----.                     ,-.-. .=-.-.  ,-,--.     ,----.  
  .-`.' ,`.  ,-.--` , \  .-.,.---.  ,--.-./=/ ,//==/_ /,-.'-  _\ ,-.--` , \ 
 /==/, -   \|==|-  _.-` /==/  `   \/==/, ||=| -|==|, |/==/_ ,_.'|==|-  _.-` 
|==| _ .=. ||==|   `.-.|==|-, .=., \==\,  \ / ,|==|  |\==\  \   |==|   `.-. 
|==| , '=',/==/_ ,    /|==|   '='  /\==\ - ' - /==|- | \==\ -\ /==/_ ,    / 
|==|-  '..'|==|    .-' |==|- ,   .'  \==\ ,   ||==| ,| _\==\ ,\|==|    .-'  
|==|,  |   |==|_  ,`-._|==|_  . ,'.  |==| -  ,/|==|- |/==/\/ _ |==|_  ,`-._ 
/==/ - |   /==/ ,     //==/  /\ ,  ) \==\  _ / /==/. /\==\ - , /==/ ,     / 
`--`---'   `--`-----`` `--`-`--`--'   `--`--'  `--`-`  `--`---'`--`-----``  
    """
    logo4="""
                                                                                                                                 
                                                                                                                             
PPPPPPPPPPPPPPPPP                                                                 iiii                                       
P::::::::::::::::P                                                               i::::i                                      
P::::::PPPPPP:::::P                                                               iiii                                       
PP:::::P     P:::::P                                                                                                         
  P::::P     P:::::P  eeeeeeeeeeee    rrrrr   rrrrrrrrrvvvvvvv           vvvvvvviiiiiii     ssssssssss       eeeeeeeeeeee    
  P::::P     P:::::Pee::::::::::::ee  r::::rrr:::::::::rv:::::v         v:::::v i:::::i   ss::::::::::s    ee::::::::::::ee  
  P::::PPPPPP:::::Pe::::::eeeee:::::eer:::::::::::::::::rv:::::v       v:::::v   i::::i ss:::::::::::::s  e::::::eeeee:::::ee
  P:::::::::::::PPe::::::e     e:::::err::::::rrrrr::::::rv:::::v     v:::::v    i::::i s::::::ssss:::::se::::::e     e:::::e
  P::::PPPPPPPPP  e:::::::eeeee::::::e r:::::r     r:::::r v:::::v   v:::::v     i::::i  s:::::s  ssssss e:::::::eeeee::::::e
  P::::P          e:::::::::::::::::e  r:::::r     rrrrrrr  v:::::v v:::::v      i::::i    s::::::s      e:::::::::::::::::e 
  P::::P          e::::::eeeeeeeeeee   r:::::r               v:::::v:::::v       i::::i       s::::::s   e::::::eeeeeeeeeee  
  P::::P          e:::::::e            r:::::r                v:::::::::v        i::::i ssssss   s:::::s e:::::::e           
PP::::::PP        e::::::::e           r:::::r                 v:::::::v        i::::::is:::::ssss::::::se::::::::e          
P::::::::P         e::::::::eeeeeeee   r:::::r                  v:::::v         i::::::is::::::::::::::s  e::::::::eeeeeeee  
P::::::::P          ee:::::::::::::e   r:::::r                   v:::v          i::::::i s:::::::::::ss    ee:::::::::::::e  
PPPPPPPPPP            eeeeeeeeeeeeee   rrrrrrr                    vvv           iiiiiiii  sssssssssss        eeeeeeeeeeeeee  
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
                                                                                                                             
    """
    logos = [logo1,logo2,logo3,logo4]
    color.printGreen(logos[random.randint(0,3)])
    update = web_server.check_version()
    if update == False:
        color.printYellow("[!] New virus library update found! Updating virus library.")
        web_server.update_version()
        color.printGreen("[!] Updated.")
    # http://127.0.0.1:5000/database/version?version=
    

    if len(sys.argv) >= 2:
        file_list=[]
        if os.path.isfile(sys.argv[1]) :
            add_file_in_file_list(file_list,sys.argv[1])
        elif not os.path.isfile(sys.argv[1]) and os.path.exists(sys.argv[1]) :
            for walk_directory, walk_directory_subdirs, walk_directory_files in os.walk(sys.argv[1]) :
                for walk_directory_file in walk_directory_files :
                    add_file_in_file_list(file_list,walk_directory+'\\'+walk_directory_file)
        elif sys.argv[1]=='all' :
            try:
                for walk_directory, walk_directory_subdirs, walk_directory_files in os.walk("C:\\") :
                    for walk_directory_file in walk_directory_files :
                        add_file_in_file_list(file_list,walk_directory+'\\'+walk_directory_file)
            except:
                pass
        else :
            print 'Parameter ERROR !'
            print '    1.Maybe this file/directory is not exist'
            print '    2.Paramter is not string all'
            exit()

        file_list = search_hash_from_file(file_list)
        print 'Report Scan Result'
        virus_cnt = 0
        for i in range(len(file_list)):
            file_scan_index = file_list[i]

            color.printGreen('[*] Now: '+ file_scan_index.get('file_md5'))
            color.printGreen('[*] Now: '+ file_scan_index.get('file_path') )
            if file_scan_index.get('is_virus') == True:
                color.printRed('[!] Virus :'+file_scan_index.get('file_path')+' \n[!] Info  :'+file_scan_index.get('virus_infomarion'))
                virus_cnt += 1
        color.printYellow('[!] Found ' + str(virus_cnt) + ' Viruses.')
        if virus_cnt:
            MsgBox("Warning","The virus has been found, please deal with it immediately.")
            color.printYellow('The location of the virus has been determined. Do you want to force the virus to move to quarantine and terminate the virus program? (of course, the virus may not be running.) if yes, please enter y. Otherwise, please terminate the program.')
            try:
                raw_input()
            except:
                print('[-] Stopped.')
                exit()
            time.sleep(1)
            virus_cnt = 0
            virus_cnt2 = 0
            for i in range(len(file_list)):
                file_scan_index = file_list[i]
                if file_scan_index.get('is_virus') == True:
                    color.printGreen('[*] Now: '+ file_scan_index.get('file_md5'))
                    color.printGreen('[*] Now: '+ file_scan_index.get('file_path') )
                    color.printRed('[!] Virus :'+file_scan_index.get('file_path')+' \n[!] Info  :'+file_scan_index.get('virus_infomarion'))
                    color.printYellow('[!] Killing...')
                    res=Popen("taskkill /f /IM " +  os.path.basename(file_scan_index.get('file_path')))
                    #print(res)
                    color.printYellow('[!] Moving...')
                    res=Popen("mv " +  file_scan_index.get('file_path') + ' ' + os.getcwd() + '\\Virus\\' + file_scan_index.get('file_md5') + '.virus')
                    time.sleep(0.1)
                    #print(os.path.exists(file_scan_index.get('file_path')))
                    if os.path.exists(file_scan_index.get('file_path')) == False:
                        if os.path.exists(os.getcwd() + '\\Virus\\' + file_scan_index.get('file_md5') + '.virus'):
                            color.printGreen('[*] The virus named ' + os.path.basename(file_scan_index.get('file_path')) + ' is now safe.')
                            virus_cnt += 1
                        else:
                            color.printYellow('[-] ' + os.path.basename(file_scan_index.get('file_path')) + ' failed to move to quarantine correctly. But it is not in its original position. It may have been deleted.')
                    else:
                        color.printRed('[!] ' + os.path.basename(file_scan_index.get('file_path')) + ' cannot be deleted and moved. Be alert, it may still be running.')
                        virus_cnt2 += 1
            color.printGreen('[*] Successfully processed ' + str(virus_cnt) + ' virus.')
            color.printYellow('[-] ' + str(virus_cnt2) + ' virus failed to process.')
        
        exit()
    else :
        print 'Using:'
        print '    quick_scan_virus.py %file_path%|%directory_path%|all (cloud)'
        print 'Example:'
        print '    quick_scan_virus.py C:\\Windows\\system32\\kernel32.dll'
        print '        scan this file(quick)'
        print '    quick_scan_virus.py C:\\Windows\\system32\\'
        print '        scan all files of this directory(quick) '
        print '    quick_scan_virus.py all'
        print '        scan all files in your computer for device C(quick)'
        print '    quick_scan_virus.py C:\\Windows\\system32\\kernel32.dll cloud'
        print '        scan the file(cloud and slowly)'