import os
from os.path import exists
from colorama import init
from colorama import Fore, Back, Style
import importlib.util
import re
init()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

osdir = ""
username = ""
packagecount = 0

curdir = ""

def datafolder():
    return 'C:\\Users\\*\\' if os.name=="nt" else os.path.expanduser("~")

output = ""
Fore.LIGHTBLUE_EX
THISISLIGHTGREENN = Fore.LIGHTYELLOW_EX
osicon = [
    Fore.LIGHTBLUE_EX + " ################## " + Style.RESET_ALL,
    Fore.LIGHTBLUE_EX + "#                  #" + Style.RESET_ALL,
    THISISLIGHTGREENN + "#  ######          #" + Style.RESET_ALL,
    THISISLIGHTGREENN + "#  #    #          #" + Style.RESET_ALL,
    Fore.LIGHTBLUE_EX + "#  ######          #" + Style.RESET_ALL,
    Fore.LIGHTBLUE_EX + "#  #        #   #  #" + Style.RESET_ALL,
    THISISLIGHTGREENN + "#  #         # #   #" + Style.RESET_ALL,
    THISISLIGHTGREENN + "#  #          #    #" + Style.RESET_ALL,
    Fore.LIGHTBLUE_EX + "#  #         #     #" + Style.RESET_ALL,
    Fore.LIGHTBLUE_EX + "#                  #" + Style.RESET_ALL,
    THISISLIGHTGREENN + " ################## " + Style.RESET_ALL
]

def setPath(new):
    global curdir
    curdir = new

def pykern():
    global osdir
    global username
    global packagecount
    global curdir
    global output
    global osicon
    curdir = osdir
    print(Fore.BLUE + "PyKern v0.0.1" + Style.RESET_ALL)
    while (True):
        if curdir.find(osdir) == -1:
            curdir = osdir
        cmd = input(Fore.GREEN + curdir + Style.RESET_ALL + ": " + Fore.RED + username + Style.RESET_ALL + " >> ")
        try:
            ## first setup
            args = []
            if cmd.find(" ") != -1:
                args = re.split(" (?=(?:[^\"]*\"[^\"]*\")*(?![^\"]*\"))", cmd)
                for x in range(len(args)):
                    args[x] = args[x].replace("\"", "")
                cmd = args[0]
            
            ## filecheck
            cf = open(osdir + "/user/" + username + "/pkg/" + cmd + ".py", "r")
            cf.close()
            ## actual command

            importantFunctions = [setPath]
            importantVars = [osdir, username, curdir, args, osicon] # do not change this order, you can add things to it

            spec = importlib.util.spec_from_file_location(cmd,osdir + "/user/" + username + "/pkg/" + cmd + ".py")
            cmdmod = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(cmdmod)
            try:
                cmdmod.run(importantFunctions, importantVars)
            except Exception as error:
                print(Fore.LIGHTRED_EX + "ERROR EXECUTING COMMAND: " + error + Style.RESET_ALL)
        except Exception as error:
            print(Fore.LIGHTRED_EX + "Failed to find command \"" + cmd + "\"" + Style.RESET_ALL + ":")
            print(error)

def boot():
    global osdir
    global username
    global packagecount
    from setup import setupInit
    cls()
    if not exists(datafolder() + "/config.pykern"):
        setupInit()
    print("[-] Connecting installdir to PyKern instance")
    f = open(datafolder() + "/config.pykern", "r")
    osdir = f.readline()
    f.close()
    print("[x] Connected to " + osdir + ".")
    print("[-] Loading user")
    uf = open(osdir + "/user/.curuser", "r")
    username = uf.readline().lstrip().rstrip()
    uf.close()
    print("[x] Connected to user " + username)
    print("[-] Loading packages")
    pkgdir = osdir + "/user/" + username + "/pkg"
    for path in os.listdir(pkgdir):
        if os.path.isfile(os.path.join(pkgdir, path)):
            print("[-] - Loaded " + path.replace(".py", ""))
            packagecount += 1
    print("[x] Done, loaded " + str(packagecount) + " package(s).")
    cls()
    pykern()

print('Booting...')
boot()
