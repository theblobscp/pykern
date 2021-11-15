import os
from os.path import exists
import urllib.request

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def datafolder():
    return os.path.expanduser("~")

def installPackage(pkname, dir, username):
    urllib.request.urlretrieve("https://raw.githubusercontent.com/Kiffolisk/pykern-setup/main/" + pkname + ".py", dir + "/user/" + username + "/pkg/" + pkname + ".py")

def mkdir(newpath):
    if not os.path.exists(newpath):
        os.makedirs(newpath)

def setupInit():
    import main
    cls()
    print("PyKern setup")
    print("Choose install directory:")
    installdir = input()
    print("[-] Creating config file...")
    configfile = open(datafolder() + "/config.pykern", "w")
    configfile.write(installdir)
    configfile.close()
    print("[-] Creating directory for install...")

    mkdir(installdir)

    cls()
    print("Choose your username:")
    username = input()
    print("[-] Creating directory for user...")

    mkdir(installdir + "/user/" + username)

    print(installdir + "/user/" + username + "/pkg")

    mkdir(installdir + "/user/" + username + "/pkg")

    usrfile = open(installdir + "/user/.curuser", "w")
    usrfile.write(username)
    usrfile.close()

    print("[-] Done!")
    print("Attempting boot...")
    installPackage("sip", installdir, username)
    installPackage("sip-uninstall", installdir, username)
    installPackage("sip-update", installdir, username)
    main.boot()