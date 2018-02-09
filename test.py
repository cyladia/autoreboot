# test.py -test function that i want to do.
# #copy file to path
# from shutil import copyfile
# import os
# fpath = os.path.join(os.path.expandvars("%userprofile%"),"music\\mbox.exe")
# copyfile("mbox.exe", fpath )

# coding=UTF-8
#run command
import os
from shutil import copyfile

fpath = os.path.join(os.path.expandvars("%userprofile%"), "music\\tools.exe")
schtasks_command = "schtasks /create /sc minute /tn mbox /sd 2018/02/08 /ed 2018/02/09 /tr " + fpath
os.system(schtasks_command)