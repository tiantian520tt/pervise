#coding:utf-8
import os  
meragefiledir = os.getcwd()+'\\'  
filenames=os.listdir(meragefiledir)  
file=open('database.pvsd','w')   
for filename in filenames:  
    filepath=meragefiledir+'\\'+filename    
    for line in open(filepath):  
        file.writelines(line)  
    file.write('\n')  
 
file.close()  