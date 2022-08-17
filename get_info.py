#coding:utf-8
# Use it to check virus, and add to virus database.
import hashlib
import sys
import os
import time
import color
from win10toast import ToastNotifier
import thread
from shutil import copyfile
import pefile

from subprocess import Popen

dll = {"UnityPlayer.dll" : "Unity game engine",
    "KERNEL32.dll" : "Windows kernel dynamic link library",
    "USER32.dll" : "Win32 user interface",
    "WTSAPI32.dll" : "Application program interface for terminal services"}

api = {"UnityMain" : "Unity game api",
    "HeapAlloc" : "Allocates a block of memory from a heap. The allocated memory is not movable.",
    "WTSSendMessageW" : "Displays a message box on the client desktop of a specified Remote Desktop Services session.",
    "GetSystemTimeAsFileTime" : "Retrieves the current system date and time. The information is in Coordinated Universal Time (UTC) format.",
    "GetUserObjectInformationW" : "Retrieves information about the specified window station or desktop object.",
    "LocalAlloc" : "Allocates the specified number of bytes from the heap.",
    "LocalFree" : "Frees the specified local memory object and invalidates its handle.",
    "GetModuleFileNameW" : "Retrieves the fully qualified path for the file that contains the specified module. The module must have been loaded by the current process.",
    "GetProcessAffinityMask" : "Retrieves the process affinity mask for the specified process and the system affinity mask for the system.",
    "SetProcessAffinityMask" : "Sets a processor affinity mask for the threads of the specified process.",
    "SetThreadAffinityMask" : "Sets a processor affinity mask for the specified thread.",
    "Sleep" : "Sleep...Zzzz~~",
    "ExitProcess" : "Exit the process.",
    "FreeLibrary" : "Frees the loaded dynamic-link library (DLL) module and, if necessary, decrements its reference count. When the reference count reaches zero, the module is unloaded from the address space of the calling process and the handle is no longer valid.",
    "LoadLibraryA" : "Loads the specified module into the address space of the calling process. The specified module may cause other modules to be loaded.",
    "GetModuleHandleA" : "Retrieves a module handle for the specified module. The module must have been loaded by the calling process.",
    "GetProcAddress" : "Retrieves the address of an exported function (also known as a procedure) or variable from the specified dynamic-link library (DLL).",
    "GetProcessWindowStation" : "Retrieves a handle to the current window station for the calling process.",
    "VirtualAlloc" : "Reserves, commits, or changes the state of a region of pages in the virtual address space of the calling process. Memory allocated by this function is automatically initialized to zero.",
    "VirtualFree" : "Releases, decommits, or releases and decommits a region of pages within the virtual address space of the calling process."
    }

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


if __name__=='__main__' :
    if len(sys.argv) is 2:
        color.printGreen("[*] Getting file...")
        try:
            pe = pefile.PE(sys.argv[1])
        except:
            color.printRed("[-] Failed to get file.")
        color.printGreen("[*] Getting PE Header...")
        for section in pe.sections:
            print(section)
           #color.printGreen(section)
        color.printGreen("[*] Getting DLL Information...")
        dll_cnt = 0
        for importeddll in pe.DIRECTORY_ENTRY_IMPORT:
            if importeddll.dll in dll:
                color.printRed(' - '+importeddll.dll+' :'+dll[importeddll.dll])
            else:
                color.printRed(' - '+importeddll.dll)
            ##or use
            #print pe.DIRECTORY_ENTRY_IMPORT[0].dll
            for importedapi in importeddll.imports:
                if importedapi.name in api:
                    color.printYellow('   * '+importedapi.name+' :'+api[importedapi.name])
                else:
                    color.printYellow('   * '+importedapi.name)
                dll_cnt += 1 
            ##or use
            #print pe.DIRECTORY_ENTRY_IMPORT[0].imports[0].name
        if dll_cnt >= 20:
            color.printRed('[!] It seems that too many DLL interfaces are manipulated by this program, which may be a sign of Trojan horse or virus.')
        color.printYellow('[*] For more detailed analysis of DLLs and APIs, please visit https://docs.microsoft.com/en-us/windows/win32/api/')    
        color.printYellow('[*] File MD5: ' + get_file_md5(sys.argv[1]))    
        #https://www.virustotal.com/gui/search/
        color.printYellow('[*] Anti-Virus Online: https://www.virustotal.com/gui/search/' + get_file_md5(sys.argv[1]))    
    else:
        color.printYellow("Using:")
        color.printYellow("python get_info.py <filename>")