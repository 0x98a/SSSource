from calendar import c
from threading import local
from keyauth import api
from time import sleep
import sys
import os
from datetime import datetime
import time
import sys
import ctypes
from turtle import clear
from click import option
import requests
import glob
import psutil
import win32ui
from tkinter import N, messagebox, Tk
from colorama import Fore, Back, Style
import subprocess
import requests as req
import json
import keyboard
from colored import fg, bg, attr
import winsound
import win32gui
import ctypes
import win32console
import string
import random
import hashlib
import atexit


def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
    	path = path[:-2] + "exe"
    md5_hash = hashlib.md5()
    a_file = open(path,"rb")
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api(
	name = "Storm Spoofer",
	ownerid = "vxMTJA3Nhl",
	secret = "0cd9a3bb2b2f0f9a42f44536a31e4124adcf3ac440a84feefb40ee3bce42a59a",
	version = "2.4",
	hash_to_check = getchecksum()
)

defaultcolor = fg('27')
color = fg('27')
reset = attr('reset')
serverfound = 0
global localappdata

win32console.SetConsoleTitle("")
localappdata = os.environ["localappdata"]
keypath = localappdata+"/simp.txt"

def check_admin():
    
    try:
        isAdmin = ctypes.windll.shell32.IsUserAnAdmin()
    except AttributeError:
        isAdmin = False
    if not isAdmin:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
        sys.exit()

def get_id():
    return subprocess.Popen('dmidecode.exe -s system-uuid'.split())

now = datetime.now()
tim = now.strftime("%H:%M:%S")
osname = os.name

class simplecolors:
    error = '[\033[94m' + tim + '\x1b[0m]\033[91m [FAIL] \x1b[0m'
    ok = '[\033[94m' + tim + '\x1b[0m]\033[92m [SUCCESS] \x1b[0m'
    info = '\x1b[0m\033[96m[Info]\x1b[0m'


def logo():
    print(color +"""
    [40;38;2;109;0;255m [0m[40;38;2;106;6;255m [0m[40;38;2;103;13;255m [0m[40;38;2;100;19;255m_[0m[40;38;2;97;26;255m_[0m[40;38;2;94;32;255m_[0m[40;38;2;91;38;255m_[0m[40;38;2;88;45;255m_[0m[40;38;2;85;51;255m [0m[40;38;2;82;58;255m_[0m[40;38;2;79;64;255m_[0m[40;38;2;76;71;255m [0m[40;38;2;73;77;255m [0m[40;38;2;70;83;255m [0m[40;38;2;67;90;255m [0m[40;38;2;64;96;255m [0m[40;38;2;61;103;255m [0m[40;38;2;58;109;255m [0m[40;38;2;55;115;255m [0m[40;38;2;52;122;255m [0m[40;38;2;49;128;255m [0m[40;38;2;46;135;255m [0m[40;38;2;43;141;255m [0m[40;38;2;40;147;255m [0m[40;38;2;37;154;255m [0m[40;38;2;34;160;255m [0m[40;38;2;31;167;255m [0m[40;38;2;28;173;255m [0m[40;38;2;25;180;255m [0m[40;38;2;22;186;255m [0m[40;38;2;19;192;255m [0m[40;38;2;16;199;255m [0m[40;38;2;13;205;255m [0m[40;38;2;10;212;255m [0m[40;38;2;7;218;255m [0m[40;38;2;4;224;255m [0m[40;38;2;1;231;255m [0m[40;38;2;3;231;255m_[0m[40;38;2;10;224;255m_[0m[40;38;2;16;218;255m_[0m[40;38;2;23;212;255m_[0m[40;38;2;29;205;255m_[0m[40;38;2;36;199;255m [0m[40;38;2;42;192;255m [0m[40;38;2;49;186;255m [0m[40;38;2;55;180;255m [0m[40;38;2;62;173;255m [0m[40;38;2;68;167;255m [0m[40;38;2;75;160;255m [0m[40;38;2;81;154;255m [0m[40;38;2;88;147;255m [0m[40;38;2;94;141;255m [0m[40;38;2;101;135;255m [0m[40;38;2;107;128;255m [0m[40;38;2;114;122;255m [0m[40;38;2;120;115;255m [0m[40;38;2;127;109;255m [0m[40;38;2;133;103;255m [0m[40;38;2;140;96;255m [0m[40;38;2;146;90;255m [0m[40;38;2;153;83;255m [0m[40;38;2;159;77;255m_[0m[40;38;2;166;71;255m_[0m[40;38;2;172;64;255m_[0m[40;38;2;179;58;255m_[0m[40;38;2;185;51;255m [0m[40;38;2;192;45;255m [0m[40;38;2;198;38;255m [0m[40;38;2;205;32;255m [0m[40;38;2;211;26;255m [0m[40;38;2;218;19;255m [0m[40;38;2;224;13;255m [0m[40;38;2;231;6;255m [0m[40;38;2;237;0;255m [0m
    [40;38;2;109;0;255m [0m[40;38;2;106;6;255m [0m[40;38;2;103;13;255m/[0m[40;38;2;100;19;255m [0m[40;38;2;97;26;255m_[0m[40;38;2;94;32;255m_[0m[40;38;2;91;38;255m_[0m[40;38;2;88;45;255m/[0m[40;38;2;85;51;255m/[0m[40;38;2;82;58;255m [0m[40;38;2;79;64;255m/[0m[40;38;2;76;71;255m_[0m[40;38;2;73;77;255m_[0m[40;38;2;70;83;255m_[0m[40;38;2;67;90;255m_[0m[40;38;2;64;96;255m_[0m[40;38;2;61;103;255m [0m[40;38;2;58;109;255m [0m[40;38;2;55;115;255m_[0m[40;38;2;52;122;255m_[0m[40;38;2;49;128;255m_[0m[40;38;2;46;135;255m_[0m[40;38;2;43;141;255m_[0m[40;38;2;40;147;255m_[0m[40;38;2;37;154;255m_[0m[40;38;2;34;160;255m_[0m[40;38;2;31;167;255m_[0m[40;38;2;28;173;255m [0m[40;38;2;25;180;255m_[0m[40;38;2;22;186;255m_[0m[40;38;2;19;192;255m_[0m[40;38;2;16;199;255m [0m[40;38;2;13;205;255m [0m[40;38;2;10;212;255m [0m[40;38;2;7;218;255m [0m[40;38;2;4;224;255m [0m[40;38;2;1;231;255m/[0m[40;38;2;3;231;255m [0m[40;38;2;10;224;255m_[0m[40;38;2;16;218;255m_[0m[40;38;2;23;212;255m_[0m[40;38;2;29;205;255m/[0m[40;38;2;36;199;255m_[0m[40;38;2;42;192;255m_[0m[40;38;2;49;186;255m_[0m[40;38;2;55;180;255m_[0m[40;38;2;62;173;255m [0m[40;38;2;68;167;255m [0m[40;38;2;75;160;255m_[0m[40;38;2;81;154;255m_[0m[40;38;2;88;147;255m_[0m[40;38;2;94;141;255m_[0m[40;38;2;101;135;255m [0m[40;38;2;107;128;255m [0m[40;38;2;114;122;255m_[0m[40;38;2;120;115;255m_[0m[40;38;2;127;109;255m_[0m[40;38;2;133;103;255m_[0m[40;38;2;140;96;255m [0m[40;38;2;146;90;255m [0m[40;38;2;153;83;255m/[0m[40;38;2;159;77;255m [0m[40;38;2;166;71;255m_[0m[40;38;2;172;64;255m_[0m[40;38;2;179;58;255m/[0m[40;38;2;185;51;255m_[0m[40;38;2;192;45;255m_[0m[40;38;2;198;38;255m [0m[40;38;2;205;32;255m [0m[40;38;2;211;26;255m_[0m[40;38;2;218;19;255m_[0m[40;38;2;224;13;255m_[0m[40;38;2;231;6;255m_[0m[40;38;2;237;0;255m_[0m
    [40;38;2;109;0;255m [0m[40;38;2;106;6;255m [0m[40;38;2;103;13;255m\[0m[40;38;2;100;19;255m_[0m[40;38;2;97;26;255m_[0m[40;38;2;94;32;255m [0m[40;38;2;91;38;255m\[0m[40;38;2;88;45;255m/[0m[40;38;2;85;51;255m [0m[40;38;2;82;58;255m_[0m[40;38;2;79;64;255m_[0m[40;38;2;76;71;255m/[0m[40;38;2;73;77;255m [0m[40;38;2;70;83;255m_[0m[40;38;2;67;90;255m_[0m[40;38;2;64;96;255m [0m[40;38;2;61;103;255m\[0m[40;38;2;58;109;255m/[0m[40;38;2;55;115;255m [0m[40;38;2;52;122;255m_[0m[40;38;2;49;128;255m_[0m[40;38;2;46;135;255m_[0m[40;38;2;43;141;255m/[0m[40;38;2;40;147;255m [0m[40;38;2;37;154;255m_[0m[40;38;2;34;160;255m_[0m[40;38;2;31;167;255m [0m[40;38;2;28;173;255m`[0m[40;38;2;25;180;255m_[0m[40;38;2;22;186;255m_[0m[40;38;2;19;192;255m [0m[40;38;2;16;199;255m\[0m[40;38;2;13;205;255m [0m[40;38;2;10;212;255m [0m[40;38;2;7;218;255m [0m[40;38;2;4;224;255m [0m[40;38;2;1;231;255m\[0m[40;38;2;3;231;255m_[0m[40;38;2;10;224;255m_[0m[40;38;2;16;218;255m [0m[40;38;2;23;212;255m\[0m[40;38;2;29;205;255m/[0m[40;38;2;36;199;255m [0m[40;38;2;42;192;255m_[0m[40;38;2;49;186;255m_[0m[40;38;2;55;180;255m [0m[40;38;2;62;173;255m\[0m[40;38;2;68;167;255m/[0m[40;38;2;75;160;255m [0m[40;38;2;81;154;255m_[0m[40;38;2;88;147;255m_[0m[40;38;2;94;141;255m [0m[40;38;2;101;135;255m\[0m[40;38;2;107;128;255m/[0m[40;38;2;114;122;255m [0m[40;38;2;120;115;255m_[0m[40;38;2;127;109;255m_[0m[40;38;2;133;103;255m [0m[40;38;2;140;96;255m\[0m[40;38;2;146;90;255m/[0m[40;38;2;153;83;255m [0m[40;38;2;159;77;255m/[0m[40;38;2;166;71;255m_[0m[40;38;2;172;64;255m/[0m[40;38;2;179;58;255m [0m[40;38;2;185;51;255m_[0m[40;38;2;192;45;255m [0m[40;38;2;198;38;255m\[0m[40;38;2;205;32;255m/[0m[40;38;2;211;26;255m [0m[40;38;2;218;19;255m_[0m[40;38;2;224;13;255m_[0m[40;38;2;231;6;255m_[0m[40;38;2;237;0;255m/[0m
    [40;38;2;109;0;255m [0m[40;38;2;106;6;255m_[0m[40;38;2;103;13;255m_[0m[40;38;2;100;19;255m_[0m[40;38;2;97;26;255m/[0m[40;38;2;94;32;255m [0m[40;38;2;91;38;255m/[0m[40;38;2;88;45;255m [0m[40;38;2;85;51;255m/[0m[40;38;2;82;58;255m_[0m[40;38;2;79;64;255m/[0m[40;38;2;76;71;255m [0m[40;38;2;73;77;255m/[0m[40;38;2;70;83;255m_[0m[40;38;2;67;90;255m/[0m[40;38;2;64;96;255m [0m[40;38;2;61;103;255m/[0m[40;38;2;58;109;255m [0m[40;38;2;55;115;255m/[0m[40;38;2;52;122;255m [0m[40;38;2;49;128;255m [0m[40;38;2;46;135;255m/[0m[40;38;2;43;141;255m [0m[40;38;2;40;147;255m/[0m[40;38;2;37;154;255m [0m[40;38;2;34;160;255m/[0m[40;38;2;31;167;255m [0m[40;38;2;28;173;255m/[0m[40;38;2;25;180;255m [0m[40;38;2;22;186;255m/[0m[40;38;2;19;192;255m [0m[40;38;2;16;199;255m/[0m[40;38;2;13;205;255m [0m[40;38;2;10;212;255m [0m[40;38;2;7;218;255m [0m[40;38;2;4;224;255m_[0m[40;38;2;1;231;255m_[0m[40;38;2;3;231;255m_[0m[40;38;2;10;224;255m/[0m[40;38;2;16;218;255m [0m[40;38;2;23;212;255m/[0m[40;38;2;29;205;255m [0m[40;38;2;36;199;255m/[0m[40;38;2;42;192;255m_[0m[40;38;2;49;186;255m/[0m[40;38;2;55;180;255m [0m[40;38;2;62;173;255m/[0m[40;38;2;68;167;255m [0m[40;38;2;75;160;255m/[0m[40;38;2;81;154;255m_[0m[40;38;2;88;147;255m/[0m[40;38;2;94;141;255m [0m[40;38;2;101;135;255m/[0m[40;38;2;107;128;255m [0m[40;38;2;114;122;255m/[0m[40;38;2;120;115;255m_[0m[40;38;2;127;109;255m/[0m[40;38;2;133;103;255m [0m[40;38;2;140;96;255m/[0m[40;38;2;146;90;255m [0m[40;38;2;153;83;255m_[0m[40;38;2;159;77;255m_[0m[40;38;2;166;71;255m/[0m[40;38;2;172;64;255m [0m[40;38;2;179;58;255m [0m[40;38;2;185;51;255m_[0m[40;38;2;192;45;255m_[0m[40;38;2;198;38;255m/[0m[40;38;2;205;32;255m [0m[40;38;2;211;26;255m/[0m[40;38;2;218;19;255m [0m[40;38;2;224;13;255m [0m[40;38;2;231;6;255m [0m[40;38;2;237;0;255m [0m
    [40;38;2;109;0;255m/[0m[40;38;2;106;6;255m_[0m[40;38;2;103;13;255m_[0m[40;38;2;100;19;255m_[0m[40;38;2;97;26;255m_[0m[40;38;2;94;32;255m/[0m[40;38;2;91;38;255m\[0m[40;38;2;88;45;255m_[0m[40;38;2;85;51;255m_[0m[40;38;2;82;58;255m/[0m[40;38;2;79;64;255m\[0m[40;38;2;76;71;255m_[0m[40;38;2;73;77;255m_[0m[40;38;2;70;83;255m_[0m[40;38;2;67;90;255m_[0m[40;38;2;64;96;255m/[0m[40;38;2;61;103;255m_[0m[40;38;2;58;109;255m/[0m[40;38;2;55;115;255m [0m[40;38;2;52;122;255m [0m[40;38;2;49;128;255m/[0m[40;38;2;46;135;255m_[0m[40;38;2;43;141;255m/[0m[40;38;2;40;147;255m [0m[40;38;2;37;154;255m/[0m[40;38;2;34;160;255m_[0m[40;38;2;31;167;255m/[0m[40;38;2;28;173;255m [0m[40;38;2;25;180;255m/[0m[40;38;2;22;186;255m_[0m[40;38;2;19;192;255m/[0m[40;38;2;16;199;255m [0m[40;38;2;13;205;255m [0m[40;38;2;10;212;255m [0m[40;38;2;7;218;255m/[0m[40;38;2;4;224;255m_[0m[40;38;2;1;231;255m_[0m[40;38;2;3;231;255m_[0m[40;38;2;10;224;255m_[0m[40;38;2;16;218;255m/[0m[40;38;2;23;212;255m [0m[40;38;2;29;205;255m.[0m[40;38;2;36;199;255m_[0m[40;38;2;42;192;255m_[0m[40;38;2;49;186;255m_[0m[40;38;2;55;180;255m/[0m[40;38;2;62;173;255m\[0m[40;38;2;68;167;255m_[0m[40;38;2;75;160;255m_[0m[40;38;2;81;154;255m_[0m[40;38;2;88;147;255m_[0m[40;38;2;94;141;255m/[0m[40;38;2;101;135;255m\[0m[40;38;2;107;128;255m_[0m[40;38;2;114;122;255m_[0m[40;38;2;120;115;255m_[0m[40;38;2;127;109;255m_[0m[40;38;2;133;103;255m/[0m[40;38;2;140;96;255m_[0m[40;38;2;146;90;255m/[0m[40;38;2;153;83;255m [0m[40;38;2;159;77;255m [0m[40;38;2;166;71;255m\[0m[40;38;2;172;64;255m_[0m[40;38;2;179;58;255m_[0m[40;38;2;185;51;255m_[0m[40;38;2;192;45;255m/[0m[40;38;2;198;38;255m_[0m[40;38;2;205;32;255m/[0m[40;38;2;211;26;255m [0m[40;38;2;218;19;255m [0m[40;38;2;224;13;255m [0m[40;38;2;231;6;255m [0m[40;38;2;237;0;255m [0m
    [40;38;2;109;0;255m [0m[40;38;2;106;6;255m [0m[40;38;2;103;13;255m [0m[40;38;2;100;19;255m [0m[40;38;2;97;26;255m [0m[40;38;2;94;32;255m [0m[40;38;2;91;38;255m [0m[40;38;2;88;45;255m [0m[40;38;2;85;51;255m [0m[40;38;2;82;58;255m [0m[40;38;2;79;64;255m [0m[40;38;2;76;71;255m [0m[40;38;2;73;77;255m [0m[40;38;2;70;83;255m [0m[40;38;2;67;90;255m [0m[40;38;2;64;96;255m [0m[40;38;2;61;103;255m [0m[40;38;2;58;109;255m [0m[40;38;2;55;115;255m [0m[40;38;2;52;122;255m [0m[40;38;2;49;128;255m [0m[40;38;2;46;135;255m [0m[40;38;2;43;141;255m [0m[40;38;2;40;147;255m [0m[40;38;2;37;154;255m [0m[40;38;2;34;160;255m [0m[40;38;2;31;167;255m [0m[40;38;2;28;173;255m [0m[40;38;2;25;180;255m [0m[40;38;2;22;186;255m [0m[40;38;2;19;192;255m [0m[40;38;2;16;199;255m [0m[40;38;2;13;205;255m [0m[40;38;2;10;212;255m [0m[40;38;2;7;218;255m [0m[40;38;2;4;224;255m [0m[40;38;2;1;231;255m [0m[40;38;2;3;231;255m [0m[40;38;2;10;224;255m/[0m[40;38;2;16;218;255m_[0m[40;38;2;23;212;255m/[0m[40;38;2;29;205;255m [0m[40;38;2;36;199;255m [0m[40;38;2;42;192;255m [0m[40;38;2;49;186;255m [0m[40;38;2;55;180;255m [0m[40;38;2;62;173;255m [0m[40;38;2;68;167;255m [0m[40;38;2;75;160;255m [0m[40;38;2;81;154;255m [0m[40;38;2;88;147;255m [0m[40;38;2;94;141;255m [0m[40;38;2;101;135;255m [0m[40;38;2;107;128;255m [0m[40;38;2;114;122;255m [0m[40;38;2;120;115;255m [0m[40;38;2;127;109;255m [0m[40;38;2;133;103;255m [0m[40;38;2;140;96;255m [0m[40;38;2;146;90;255m [0m[40;38;2;153;83;255m [0m[40;38;2;159;77;255m [0m[40;38;2;166;71;255m [0m[40;38;2;172;64;255m [0m[40;38;2;179;58;255m [0m[40;38;2;185;51;255m [0m[40;38;2;192;45;255m [0m[40;38;2;198;38;255m [0m[40;38;2;205;32;255m [0m
                                                   
    """ + reset + defaultcolor)

                                                                            
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    os.system('mode con: cols=80 lines=27')
    win32console.SetConsoleTitle("")
    logo()

def clearConsolenologo():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)
    os.system('mode con: cols=80 lines=27')
    win32console.SetConsoleTitle("")

def space(amount):
    for i in range(amount):
        print("\n")

def WindowExists(windowname):
    try:
        win32ui.FindWindow(None, windowname)

    except win32ui.error:
        return False
    else:
        return True

def alert(title, message, kind='info', hidemain=True):
    if kind not in ('error', 'warning', 'info'):
        raise ValueError('Unsupported alert kind.')

    show_method = getattr(messagebox, 'show{}'.format(kind))
    show_method(title, message)

def pathfivem():
    global fpath
    defaultpath = localappdata + "\FiveM\FiveM.app"
    simplepath = "C:\FiveM\FiveM.app"
    if os.path.exists(defaultpath):
        fpath = localappdata + "\FiveM"
    elif os.path.exists(simplepath):
        fpath = "C:\FiveM"
    else:
        print(" No FiveM path found")
        space(1)
        maybepath = input(" Enter your path here: ")
        if os.path.exists(maybepath+"/FiveM.exe"):
            fpath = maybepath
        else:
            clearConsole()
            print(" Invalid path. Your path must include FiveM.exe")
            time.sleep(2)
            clearConsole()
            pathfivem()
               

def sp():
    print("")

def fixthing():
    pathfivem()
    adhesive1path = fpath+"\FiveM.App/adhesive1.dll"
    adhesivepath = fpath+"\FiveM.App/adhesive.dll"
    if os.path.exists(adhesive1path):
        if os.path.exists(adhesivepath):
            os.remove(adhesive1path)
        else:
            os.rename(adhesive1path, adhesivepath)
    os.popen("netsh firewall reset")
    sp()
    print("                                   Fixed!")
    time.sleep(1)
    clearConsole()
    options()

def options():
    clearConsole()
    print("                        ╔══════════════════════════════╗")
    print("                        ║                              ║")
    print("                        ║    [1]: Play FiveM           ║")
    print("                        ║                              ║")
    print("                        ║    [2]: Signout Rockstar     ║")
    print("                        ║                              ║")
    print("                        ║    [3]: FiveM Build          ║")
    print("                        ║                              ║")
    print("                        ║    [4]: Debugger             ║")
    print("                        ║                              ║")
    print("                        ║    [5]: Update FiveM         ║")
    print("                        ║                              ║")
    print("                        ║    [6]: Other                ║")
    print("                        ║                              ║")
    print("                        ╚══════════════════════════════╝")
    print("7 on")
    print("8 off")
    sp()
    optionchoice = input("     Enter Here > ")
    if optionchoice == "1":
        methodmenu()
    elif optionchoice == "2":
        clearConsole()
        signout("autoclean")
    elif optionchoice == "3":
        clearConsole()
        buildmenu()
    elif optionchoice == "4":
        clearConsole()
        fixthing()
    elif optionchoice == "5":
        clearConsole()
        update()
    elif optionchoice == "6":
        clearConsole()
        other()
    elif optionchoice == "7":
        blockentire()
        clearConsole()
        options()
    elif optionchoice == "8":
        unblock()
        clearConsole()
        options()
    elif optionchoice == "69":
        clearConsole()
        print(" Nice")
        time.sleep(1)
        clearConsole()
        options()
    else:
        clearConsole()
        options()

def methodmenu():
    epic = "EpicGamesLauncher.exe" in (i.name() for i in psutil.process_iter())
    if epic == True:
        os.system("taskkill /f /im EpicGamesLauncher.exe")
    clearConsole()
    print("           ╔═════════════════════════════════════════════════════════╗")
    print("           ║                                                         ║")
    print("           ║         [1]: Only block auth servers (Stable)           ║")
    print("           ║                                                         ║")
    print("           ║         [2]: Block entire process (Testing)             ║")
    print("           ║                                                         ║")
    print("           ╚═════════════════════════════════════════════════════════╝")
    sp()
    methodchoice = input("     Enter Here > ")
    if methodchoice == "1":
        clearConsole()
        oldmethod1()
    elif methodchoice == "2":
        clearConsole()
        method2()
    else:
        clearConsole()
        print(" Invalid answer!")
        time.sleep(2)
        clearConsole()
        methodmenu()

def method2():
    os.popen("netsh advfirewall firewall delete rule name=prank dir=in")
    os.popen("netsh advfirewall firewall delete rule name=prank dir=out")
    fivem= "FiveM.exe" in (i.name() for i in psutil.process_iter())
    if fivem == True:
        os.system("taskkill /f /im FiveM.exe")
        clearConsole()
    clearConsole()
    blockentire()
    sys.stdout.write('\r Preparing bypass |   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass /   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass -   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass \\   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass |   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass /   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass -   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass \\   ')
    time.sleep(0.1)
    clearConsole()
    jaap = 1
    while jaap == 1:
        sys.stdout.write('                                             \r Waiting for FiveM |   ')
        time.sleep(0.1)
        sys.stdout.write('                                             \r Waiting for FiveM /   ')
        time.sleep(0.1)
        sys.stdout.write('                                             \r Waiting for FiveM -   ')
        time.sleep(0.1)
        sys.stdout.write('                                             \r Waiting for FiveM \\   ')
        time.sleep(0.1)
        fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
        if fivem == True:
            jaap = 3
            clearConsole()
    time.sleep(1)
    print(" Method 2")
    print(" ")
    print(" Press ENTER in the main menu")
    d = input()
    unblock()
    clearConsole()
    print(" Wait 15 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 14 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 13 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 12 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 11 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 10 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 9 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 8 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 7 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 6 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 5 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 4 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 3 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 2 seconds.")
    time.sleep(1)
    clearConsole()
    print(" Wait 1 seconds.")
    time.sleep(1)
    clearConsole()
    winsound.Beep(400, 500)
    sp()
    print("                                  Unblocked.")
    sp()
    print("                            You can connect now!")
    time.sleep(1.5)
    clearConsole()
    print("                                    Quit")
    print(" ")
    print("                         Press ENTER to stop playing")
    input("")
    clearConsole()
    blockentire()
    time.sleep(1.5)
    fivem= "FiveM.exe" in (i.name() for i in psutil.process_iter())
    if fivem == True:
        os.system("taskkill /f /im FiveM.exe")
        clearConsole()
    clearConsole()
    options()





def oldmethod1():
    os.popen("netsh advfirewall firewall delete rule name=prank dir=in")
    os.popen("netsh advfirewall firewall delete rule name=prank dir=out")
    pathfivem()
    fivem= "FiveM.exe" in (i.name() for i in psutil.process_iter())
    if fivem == True:
        os.system("taskkill /f /im FiveM.exe")
        clearConsole()
    clearConsole()
    block1()
    sys.stdout.write('\r Preparing bypass |   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass /   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass -   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass \\   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass |   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass /   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass -   ')
    time.sleep(0.1)
    sys.stdout.write('\r Preparing bypass \\   ')
    clearConsole()
    jaap = 1
    while jaap == 1:
        sys.stdout.write('                                             \r Waiting for FiveM |   ')
        time.sleep(0.1)
        sys.stdout.write('                                             \r Waiting for FiveM /   ')
        time.sleep(0.1)
        sys.stdout.write('                                             \r Waiting for FiveM -   ')
        time.sleep(0.1)
        sys.stdout.write('                                             \r Waiting for FiveM \\   ')
        time.sleep(0.1)
        fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
        if fivem == True:
            jaap = 3
            clearConsole()
    loopie = 1
    time.sleep(1)
    print(" Method 1")
    print(" ")
    print(" Press F10 in the main menu")
    print(" ")
    print(" Press F12 to return to the option menu.")
    keynotfound = "1"
    while keynotfound == "1":
        if keyboard.read_key() == "f10":
            keynotfound = "0"
            clearConsole()
            print(" Wait 15 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 14 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 13 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 12 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 11 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 10 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 9 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 8 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 7 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 6 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 5 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 4 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 3 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 2 seconds.")
            time.sleep(1)
            clearConsole()
            print(" Wait 1 seconds.")
            time.sleep(1)
            clearConsole()
            winsound.Beep(400, 500)
            block1()
            pathfivem()
            print(" ")
            print(" Press F10 to unblock/fix connection error.")
            print("")
            print(" Press F12 to return to the option menu.")
            print("")
            while loopie == 1:
                fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
                if fivem == False:
                    loopie = 3
                    clearConsole()
                    print(" FiveM connection lost...")
                    time.sleep(3)
                    clearConsole()
                    options()
                elif keyboard.read_key() == "f10":
                    os.popen("netsh advfirewall firewall delete rule name=prank dir=in")
                    os.popen("netsh advfirewall firewall delete rule name=prank dir=out")
                    clearConsole()
                    winsound.Beep(400, 500)
                    print(" You have 2 Seconds to connect to a server.")
                    time.sleep(1)
                    clearConsole()
                    print(" You have 1 Seconds to connect to a server.")
                    time.sleep(1)
                    clearConsole()
                    block2()
                elif keyboard.read_key() == "f12":
                    loopie = 0
                    clearConsole()
                    options()
                    
        elif keyboard.read_key() == "f12":
            keynotfound = "0"
            clearConsole()
            options()



def update():
    pathfivem()
    unblock()
    signout("sus")
    global poepsok
    clearConsole()
    space(1)
    steam = "steam.exe" in (i.name() for i in psutil.process_iter())
    if steam == True:
        print(" Closing steam.")
        space(1)
        os.system("taskkill /f /im steam.exe")
        clearConsole()
    space(2)
    jaap = 1
    while jaap == 1:
        sys.stdout.write('\r                            Waiting for FiveM |   ')
        time.sleep(0.1)
        sys.stdout.write('\r                            Waiting for FiveM /   ')
        time.sleep(0.1)
        sys.stdout.write('\r                            Waiting for FiveM -   ')
        time.sleep(0.1)
        sys.stdout.write('\r                            Waiting for FiveM \\   ')
        time.sleep(0.1)
        fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
        if fivem == True:
            jaap = 3
            clearConsole()
    poepsok = 3
    space(2)
    while poepsok > 2:
        if WindowExists("Rockstar Games - Social Club") == False:
                sys.stdout.write('\r                             Updating FiveM |   ')
                time.sleep(0.1)
                sys.stdout.write('\r                             Updating FiveM /   ')
                time.sleep(0.1)
                sys.stdout.write('\r                             Updating FiveM -   ')
                time.sleep(0.1)
                sys.stdout.write('\r                             Updating FiveM \\   ')
                time.sleep(0.1)
                steam = "steam.exe" in (i.name() for i in psutil.process_iter())
                if steam == True:
                    print(" Closing steam.")
                    space(1)
                    os.system("taskkill /f /im steam.exe")
                    clearConsole()
        if WindowExists("Rockstar Games - Social Club") == True:
            poepsok = 1
    os.system("taskkill /f /im FiveM.exe")
    clearConsole()
    print("                             FiveM updated!")
    time.sleep(3)
    clearConsole()
    options()

def other():
    clearConsole()
    print("                     ╔═══════════════════════════════════╗")
    print("                     ║                                   ║")
    print("                     ║        [1]: Unlink Xbox           ║")
    print("                     ║                                   ║")
    print("                     ║        [2]: Link Discord          ║")
    print("                     ║                                   ║")
    print("                     ╚═══════════════════════════════════╝")
    sp()
    linkchoice = input("     Enter Here > ")
    if linkchoice == "1":
        clearConsole()
        unlinkxbox()
    elif linkchoice == "2":
        linkdiscord()
    else:
        clearConsole()
        sp()
        ctypes.windll.user32.MessageBoxW(0, "Invalid answer", "Error", 0)
        time.sleep(1)
        clearConsole()
        other()

def unlinkxbox():
    xboxpath = "C:/Windows/System32/drivers/etc/hosts"
    if os.path.exists(xboxpath):
        with open(xboxpath, "r+") as f:
            oldxbox = f.read() # read everything in the file
            if "xbox" in oldxbox:
                f.close()
                clearConsole()
                print(" Xbox already unlinked.")
                time.sleep(3)
                clearConsole()
                options()
            else:
                f.seek(0)
                f.write(oldxbox + "\n127.0.0.1 xboxlive.com\n127.0.0.1 user.auth.xboxlive.com\n127.0.0.1 presence-heartbeat.xboxlive.com")
                f.close()
                clearConsole()
                print(" Xbox unlinked!")
                time.sleep(3)
                clearConsole()
                options()
    else:
        clearConsole()
        print(" Could not unlink xbox, try doing it manually with revo.")
        time.sleep(3)
        clearConsole()
        options()


def linkdiscord():
    clearConsole()
    block1()
    pathfivem()
    adhesivepath = fpath+"\FiveM.App/adhesive.dll"
    adhesive1path = fpath+"\FiveM.App/adhesive1.dll"
    if os.path.exists(adhesivepath):
        os.rename(adhesivepath, adhesive1path)
        clearConsole()
        space(3)
        jaap1 = 1
        while jaap1 == 1:
            sys.stdout.write('\r                            Waiting for FiveM |   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM /   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM -   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM \\   ')
            time.sleep(0.1)
            fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
            if fivem == True:
                jaap1 = 3
        
        clearConsole()
        print("                    Login with your current rockstar.")
        sp()
        print("                  Press ENTER if you authorised discord")
        f = input("")
        os.rename(adhesive1path, adhesivepath)
        os.system("taskkill /f /im FiveM.exe")
        clearConsole()
        print("                        Succesfully linked discord!")
        time.sleep(3)
        clearConsole()
        options()
    elif os.path.exists(adhesive1path):
        space(3)
        jaap = 1
        while jaap == 1:
            sys.stdout.write('\r                            Waiting for FiveM |   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM /   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM -   ')
            time.sleep(0.1)
            sys.stdout.write('\r                            Waiting for FiveM \\   ')
            time.sleep(0.1)
            fivem = "FiveM.exe" in (i.name() for i in psutil.process_iter())
            if fivem == True:
                jaap = 3
        clearConsole()
        print("                    Login with your current rockstar.")
        sp()
        print("                  Press ENTER if you authorised discord")
        f = input("")
        os.rename(adhesive1path, adhesivepath)
        os.system("taskkill /f /im FiveM.exe")
        clearConsole()
        print("                        Succesfully linked discord!")
        time.sleep(3)
        clearConsole()
        options()
    else:
        clearConsole()
        sp()
        print(" Failed, could not find you're FiveM data folder.")
        time.sleep(2)
        clearConsole()
        options()


def buildmenu():
    global fb
    clearConsole()
    pathfivem()
    print("                            ╔════════════════════╗")
    print("                            ║                    ║")
    print("                            ║     [1]: 1604      ║")
    print("                            ║                    ║")
    print("                            ║     [2]: 2060      ║")
    print("                            ║                    ║")
    print("                            ║     [3]: 2189      ║")
    print("                            ║                    ║")
    print("                            ║     [4]: 2372      ║")
    print("                            ║                    ║")
    print("                            ║     [5]: 2545      ║")
    print("                            ║                    ║")
    print("                            ╚════════════════════╝")
    sp()
    fbchoice = input("     Enter Here > ")
    if fbchoice == "1":
        clearConsole()
        changebuild("1604")
    elif fbchoice == "2":
        clearConsole()
        changebuild("2060")
    elif fbchoice == "3":
        clearConsole()
        changebuild("2189")
    elif fbchoice == "4":
        clearConsole()
        changebuild("2372")
    elif fbchoice == "5":
        clearConsole()
        changebuild("2545")
    else:
        clearConsole()
        buildmenu()

def changebuild(build):
    citizenpath = fpath+"/FiveM.app/CitizenFX.ini"
    if os.path.exists(citizenpath):
        with open(citizenpath, "r+") as f:
            old = f.read()
            if "SavedBuildNumber" in old:
                if "2189" in old:
                    f.seek(0)
                    replace_string = old.replace('2189', build)
                    f.write(replace_string)
                elif "1604" in old:
                    f.seek(0)
                    replace_string = old.replace('1604', build)
                    f.write(replace_string)
                elif "2372" in old:
                    f.seek(0)
                    replace_string = old.replace('2372', build)
                    f.write(replace_string)
                elif "2060" in old:
                    f.seek(0)
                    replace_string = old.replace('2060', build)
                    f.write(replace_string)
                elif "2545" in old:
                    f.seek(0)
                    replace_string = old.replace('2545', build)
                    f.write(replace_string)
            else:
                f.seek(0)
                f.write(old + "\nSavedBuildNumber="+build)
        sp()
        sys.stdout.write('\r                             Swaping builds |')
        time.sleep(0.2)
        sys.stdout.write('\r                             Swaping builds /')
        time.sleep(0.2)
        sys.stdout.write('\r                             Swaping builds -')
        time.sleep(0.2)
        sys.stdout.write('\r                             Swaping builds \\')
        time.sleep(0.2)
        with open(citizenpath, "r+") as f:
            old = f.read()
            if build in old:
                clearConsole()
                sp()
                print("                              Swaped builds!")
                time.sleep(3)
                clearConsole()
                options()
            else:
                clearConsole()
                print("                      Failed swaping, contact support")
                time.sleep(5)
                sys.exit()
    else:
        clearConsole()
        print(" Failed!")
        space(1)
        print(" Did not find CitizenFX file, check if your fivem folder is complete.")
        time.sleep(5)
        options()



    

def signout(way):
    defaultpath = localappdata+"/DigitalEntitlements"
    if os.path.exists(defaultpath):
        files = glob.glob(defaultpath+"/*")
        for f in files:
            os.remove(f)
        os.rmdir(defaultpath)
        time.sleep(1)
        clearConsole()
        if way == "autoclean":
            options()
    else:
        time.sleep(1)
        clearConsole
        if way == "autoclean":
            options()


def check():
    userpath = localappdata+"/stormuser.txt"
    passpath = localappdata+"/stormpass.txt"
    if os.path.exists(userpath):
        if os.path.exists(passpath):
            with open(userpath, "r+") as f:
                user = f.read()
                f.close()
                with open(passpath, "r+") as g:
                    password = g.read()
                    g.close()
                    keyauthapp.login(user,password)
                    clearConsole()
                    options()




def unblock():
    os.popen("netsh advfirewall firewall delete rule name=prank dir=in")
    os.popen("netsh advfirewall firewall delete rule name=prank dir=out")


def blockentire():
    pathfivem()
    poeppath = os.path.realpath(fpath) 
    mainfivem = poeppath+"\\FiveM.exe"
    b2372 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_GTAProcess.exe"
    b1604 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b1604_GTAProcess.exe"
    b2060 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_GTAProcess.exe"
    b2189 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_GTAProcess.exe"
    b2545 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_GTAProcess.exe"
    steam1 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam2 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_SteamChild.exe"
    steam3 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam4 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_SteamChild.exe"
    steam6 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_SteamChild.exe"
    steam5 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_SteamChild"
    gtaprocess = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_GTAProcess.exe"
    dumpserver1 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_DumpServer"
    dumpserver2 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_DumpServer"
    dumpserver3 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_DumpServer"
    dumpserver4 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_DumpServer"
    dumpserver5 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b1604_DumpServer"
    dumpserver6 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_DumpServer"
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+dumpserver6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+dumpserver6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out action=block program="+b2545+" enable=yes profile=any")


def block1():
    pathfivem()
    poeppath = os.path.realpath(fpath) 
    mainfivem = poeppath+"\\FiveM.exe"
    authserver = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_AuthBrowser"
    b2372 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_GTAProcess.exe"
    b1604 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b1604_GTAProcess.exe"
    b2060 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_GTAProcess.exe"
    b2189 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_GTAProcess.exe"
    b2545 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_GTAProcess.exe"
    steam1 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam2 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_SteamChild.exe"
    steam3 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam4 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_SteamChild.exe"
    steam6 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_SteamChild.exe"
    steam5 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_SteamChild"
    gtaprocess = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_GTAProcess.exe"
    dumpserver1 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_DumpServer"
    dumpserver2 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_DumpServer"
    dumpserver3 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_DumpServer"
    dumpserver4 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_DumpServer"
    dumpserver5 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b1604_DumpServer"
    dumpserver6 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_DumpServer"
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver6+" enable=yes profile=any")



def block2():
    pathfivem()
    poeppath = os.path.realpath(fpath) 
    mainfivem = poeppath+"\\FiveM.exe"
    authserver = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_AuthBrowser"
    b2372 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_GTAProcess.exe"
    b1604 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b1604_GTAProcess.exe"
    b2060 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_GTAProcess.exe"
    b2189 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_GTAProcess.exe"
    b2545 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_GTAProcess.exe"
    steam1 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam2 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_SteamChild.exe"
    steam3 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_SteamChild.exe"
    steam4 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2372_SteamChild.exe"
    steam6 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_SteamChild.exe"
    steam5 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_SteamChild"
    gtaprocess = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_GTAProcess.exe"
    dumpserver1 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_DumpServer"
    dumpserver2 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2060_DumpServer"
    dumpserver3 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2189_DumpServer"
    dumpserver4 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b2545_DumpServer"
    dumpserver5 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_b1604_DumpServer"
    dumpserver6 = poeppath+"\\FiveM.app\\data\\cache\\subprocess\\FiveM_DumpServer"
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.1.89 action=block program="+dumpserver6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.1.89 action=block program="+dumpserver6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+authserver+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+gtaprocess+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+mainfivem+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2372+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2060+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2545+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b2189+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+b1604+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+steam6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver1+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver2+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver3+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver4+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver5+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=out remoteip=104.18.0.89 action=block program="+dumpserver6+" enable=yes profile=any")
    os.popen("netsh advfirewall firewall add rule name=prank dir=in remoteip=104.18.0.89 action=block program="+dumpserver6+" enable=yes profile=any")
    print(" ")
    print(" Press F10 to unblock/fix connection error.")
    print("")
    print(" Press F12 to return to the option menu.")
    print("")

os.system('mode con: cols=80 lines=27')
check_admin()
check()
