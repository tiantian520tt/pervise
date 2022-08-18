# Pervise
![logo](https://user-images.githubusercontent.com/64673335/185289899-4d6c6b67-7daa-44c8-a556-ff867629aa38.png)<br/>
(Powered by Python2.7)<br/>
(动力源自Python2.7)<br/>
(Server Powered by Python2.7/3.8)<br/>

(服务器动力源自Python2.7或Python3.8)<br/>
A simple and complete security software kernel based on MD5 matching<br/>
一个简易而完整的安全软件内核程序。

This project will show you how to make an anti-virus software based on MD5 detection.<br/>
此项目将向您展示如何制作一个基于MD5检测的完整架构的防病毒软件。

# Process
Currently implemented functions:<br/>
目前实现的功能：<br/>

  - Virus scanning based on MD5 matching
  - 基于MD5匹配的病毒扫描
  - Process virus files
  - 处理病毒文件
  - Update the virus library from the server (your server running script is required)
  - 从服务器更新病毒库（需要您的服务器在运行我们的脚本）
  
 Future plans:<br/>
 未来计划：<br/>
  - Better user interface than commands
  - 比命令更好的UI界面
  - More ways to kill virus and clean up
  - 更多样的杀毒方式与清理方式
  - ...
  - 。。。
 
 # How to use it
 
## Server
 First, install a python environment to debug it. Currently, the client of this project only supports Python 2.7. However, the server supports both Python 2.7 and python 3.6 and above. Follow the instructions to install. Please note that the version may be changed at any time in the future.<br/>
 首先，安装一个python环境来调试它。目前，这个项目的客户端仅支持Python2.7。但服务端同时支持Python2.7以及Python3.6以上版本。请按照指示安装。请注意，今后随时可能更改版本。<br/>
Next, you need to configure the server, otherwise it will not work properly. You can configure the server locally or on your cloud server. You can do this by using the GIT clone command on your host.<br/>
接下来，您需要配置服务器，否则它将无法正常工作。您可以在本地或云服务器上配置服务器。您可以在主机上使用GIT clone命令来实现这一点。<br/>
Use command: python web_service.py , start the server. However, this is not correct. If you need to configure the server to the cloud server, you need to change the file. Open this file and modify the IP variable of the header.<br/>
使用命令：python web_service.py ，启动服务器。然而，这可能是不正确的。如果需要将服务器配置为云服务器，则需要更改文件。打开此文件并修改标头的IP变量。<br/>
At this point, you should see some log files in the output. Good, your configuration is half finished<br/>
此时，您可以看到日志。恭喜，你的任务已经完成了一半了！<br/>

Next, you need to install the cloud database on the server. Please refer to the database branch, use the command to download it and save it to a location with sufficient space. Then, modify the web_service.py:<br/>
fileHandler  =  open  ("H:\\database\\"+hash[0]+".hash",  "r") # Change path (Get it from my index)<br/>
Modify "H: \ \ database \ \" to the path where you save the file. Then restart the server.(python)<br/>
接下来，您需要将云端数据库安装到服务器上。请参见database分支，使用命令下载他，保存到一个空间充足的位置。然后，修改web_service.py中的：<br/>
fileHandler  =  open  ("H:\\database\\"+hash[0]+".hash",  "r") # Change path (Get it from my index)<br/>
![image](https://user-images.githubusercontent.com/64673335/185305542-bb48d0d3-07a5-4b74-9aa9-0c2eb461ed3e.png)

将“H:\\database\\”修改为您保存文件的路径。然后重启服务器。(python脚本)<br/>

So far, the server has completed the configuration.
## Client
Your client also needs to install python. Please refer to server for instructions.<br/>
你的客户端也需要安装python。说明请见《服务端》。<br/>

After installation, please configure your client files to point to the correct server IP address.<br/>
安装后，请配置您的客户端文件指向到正确的服务器ip地址上。<br/>

![image](https://user-images.githubusercontent.com/64673335/185305311-11d6d09d-8a20-4099-abf0-9ab0a8ab9585.png) <br/>
Change it.<br/>
Next, run the script using Python:quick_scan_virus.py, you will get the correct instructions.<br/>
 接着，使用Python运行脚本quick_scan_virus.py，你会得到正确的指示。
 
 # Welcome to the project.
 
 
 
 
