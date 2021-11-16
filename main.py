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
osicon = [
    " ################## ",
    "#                  #",
    "#  ######          #",
    "#  #    #          #",
    "#  ######          #",
    "#  #        #   #  #",
    "#  #         # #   #",
    "#  #          #    #",
    "#  #         #     #",
    "#                  #",
    " ################## "
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
        except:
            print(Fore.LIGHTRED_EX + "Failed to find command \"" + cmd + "\"" + Style.RESET_ALL)

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
62
            cf = open(osdir + "/user/" + username + "/pkg/" + cmd + ".py", "r")
63
            cf.close()
64
            ## actual command
65
​
66
            importantFunctions = [setPath]
67
            importantVars = [osdir, username, curdir, args, osicon] # do not change this order, you can add things to it
68
​
69
            spec = importlib.util.spec_from_file_location(cmd,osdir + "/user/" + username + "/pkg/" + cmd + ".py")
70
            cmdmod = importlib.util.module_from_spec(spec)
71
            spec.loader.exec_module(cmdmod)
72
            try:
73
                cmdmod.run(importantFunctions, importantVars)
74
            except Exception as error:
75
                print(Fore.LIGHTRED_EX + "ERROR EXECUTING COMMAND: " + error + Style.RESET_ALL)
76
        except:
77
            print(Fore.LIGHTRED_EX + "Failed to find command \"" + cmd + "\"" + Style.RESET_ALL)
78
​
79
def boot():
80
    global osdir
81
    global username
82
    global packagecount
83
    from setup import setupInit
84
    cls()
85
    if not exists(datafolder() + "/config.pykern"):
86
        setupInit()
87
    print("[-] Connecting installdir to PyKern instance")
88
    f = open(datafolder() + "/config.pykern", "r")
89
    osdir = f.readline()
90
    f.close()
91
    print("[x] Connected to " + osdir + ".")
92
    print("[-] Loading user")
93
    uf = open(osdir + "/user/.curuser", "r")
94
    username = uf.readline().lstrip().rstrip()
95
    uf.close()
96
    print("[x] Connected to user " + username)
97
    print("[-] Loading packages")
98
    pkgdir = osdir + "/user/" + username + "/pkg"
99
    for path in os.listdir(pkgdir):
100
        if os.path.isfile(os.path.join(pkgdir, path)):
101
            print("[-] - Loaded " + path.replace(".py", ""))
102
            packagecount += 1
103
    print("[x] Done, loaded " + str(packagecount) + " package(s).")
104
    cls()
105
    pykern()
106
​
107
print('Booting...')
108
boot()

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
