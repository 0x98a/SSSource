# File: TDS_UnbanTool_V1.7.pyc.tmp.pyc (Python 3.12a)

from calendar import c
from threading import local
from urllib import request
from pkg_resources import cleanup_resources
from keyauth import api
from time import sleep
import sys
import os
from datetime import datetime
import time
import sys
import ctypes
from turtle import clear, clearscreen
from click import option
import glob
from tkinter import N, messagebox, Tk
from colorama import Fore, Back, Style
import subprocess
import requests as req
from colored import fg, bg, attr
import winsound
import win32gui
import ctypes
import win32console
import string
import random
import hashlib
import discord_rpc
import win32ui
import shutil
import requests
from zipfile import ZipFile
import psutil

def WindowExists(windowname):
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
    pass
# WARNING: Decompile incomplete


def check_admin():
Unsupported opcode: JUMP_IF_NOT_EXC_MATCH
    pass
# WARNING: Decompile incomplete


def getchecksum():
    path = os.path.basename(__file__)
    if not os.path.exists(path):
        path = path[:-2] + 'exe'
    md5_hash = hashlib.md5()
    a_file = open(path, 'rb')
    content = a_file.read()
    md5_hash.update(content)
    digest = md5_hash.hexdigest()
    return digest

keyauthapp = api('TDS Unban', 'HCT7tsMoxp', '61ec607e5d520f74a0e3154e5432ae2d2c62f26e6a8471dc983f0cec830ade83', '1.7', getchecksum(), **('name', 'ownerid', 'secret', 'version', 'hash_to_check'))
defaultcolor = fg('161')
color = fg('161')
note = fg('124')
reset = attr('reset')
serverfound = 0
win32console.SetConsoleTitle('TDS Unban Tool')
localappdata = os.environ['localappdata']

def get_id():
    return subprocess.Popen('dmidecode.exe -s system-uuid'.split())

now = datetime.now()
tim = now.strftime('%H:%M:%S')
osname = os.name

class simplecolors:
    error = '[\x1b[94m' + tim + '\x1b[0m]\x1b[91m [FAIL] \x1b[0m'
    ok = '[\x1b[94m' + tim + '\x1b[0m]\x1b[92m [SUCCESS] \x1b[0m'
    info = '\x1b[0m\x1b[96m[Info]\x1b[0m'


def logo():
    print(color + "\n       _________  ______     ______   \n      |  _   _  ||_   _ `. .' ____ \\  \n      |_/ | | \\_|  | | `. \\| (___ \\_| \n          | |      | |  | | _.____`.  \n         _| |_    _| |_.' /| \\____) | \n        |_____|  |______.'  \\______.' \n                                     \n    " + reset + defaultcolor)


def cls():
    os.system('mode con: cols=43 lines=22')
    os.system('cls')
    logo()


def progressbar(it, prefix, size, out = ('', 15, sys.stdout)):
[WARNING] Opcode not supported: GEN_START
    pass
# Decompile incomplete


def check():
    cls()
    print(note + '  AFTER ENTERING KEY THERE IS NO WAY BACK' + color)
    print('')
    key = input(' Key: ')
    cls()
    print(' Checking key...')
    time.sleep(0.1)
    keyauthapp.license(key)
    cls()
    thisniggaissafefortheloader(key)


def preparen(): the gen start is something like If launcher.exe in list of all running processes
Unsupported opcode: GEN_START
    launcher = 'Launcher.exe' in (lambda .0: pass# WARNING: Decompile incomplete
)(psutil.process_iter())
    if launcher == True:
        os.system('taskkill /f /im Launcher.exe')
        time.sleep(0.2)
        os.system('taskkill /F /IM LauncherPatcher.exe')
        cls()
Unsupported opcode: GEN_START
    steam = 'Steam.exe' in (lambda .0: pass# WARNING: Decompile incomplete
)(psutil.process_iter())
    if steam == True:
        os.system('taskkill /f /im Steam.exe')
        cls()
Unsupported opcode: GEN_START
    epicgames = 'EpicGamesLauncher.exe' in (lambda .0: pass# WARNING: Decompile incomplete
)(psutil.process_iter())
    if epicgames == True:
        os.system('taskkill /f /im EpicGamesLauncher.exe')
        cls()
Unsupported opcode: GEN_START
    fivem = 'FiveM.exe' in (lambda .0: pass# WARNING: Decompile incomplete
)(psutil.process_iter())
    if fivem == True:
        os.system('taskkill /f /im FiveM.exe')
        cls()
        return None


def signoutrockstar():
    defaultpath = localappdata + '/DigitalEntitlements'
    if os.path.exists(defaultpath):
        files = glob.glob(defaultpath + '/*')
        os.rmdir(defaultpath)
        time.sleep(1)


def swap(key):
Unsupported opcode: WITH_EXCEPT_START
    pathdocunormal = 'C:' + os.environ['HOMEPATH'] + '\\Documents'
    pathdocuonedrive = 'C:' + os.environ['HOMEPATH'] + '\\OneDrive\\Documents'
    if os.path.exists(pathdocuonedrive):
        pathdocu = 'C:' + os.environ['HOMEPATH'] + '\\OneDrive\\Documents\\'
    elif os.path.exists(pathdocunormal):
        pathdocu = 'C:' + os.environ['HOMEPATH'] + '\\Documents\\'
    if not os.path.exists(pathdocu + 'Rockstar Games\\Social Club\\Profiles'):
        if not os.path.exists(pathdocu + 'Rockstar Games'):
            os.mkdir(pathdocu + 'Rockstar Games')
        if not os.path.exists(pathdocu + 'Rockstar Games\\Social Club'):
            os.mkdir(pathdocu + 'Rockstar Games\\Social Club')
        if not os.path.exists(pathdocu + 'Rockstar Games\\Social Club\\Profiles'):
            os.mkdir(pathdocu + 'Rockstar Games\\Social Club\\Profiles')
        time.sleep(0.1)
    if os.path.exists(pathdocu + 'Rockstar Games\\Social Club\\Profiles'):
        shutil.rmtree(pathdocu + 'Rockstar Games\\Social Club\\Profiles')
    if os.path.exists(pathdocu + 'Rockstar Games\\Social Club\\Profiles.zip'):
        os.remove(pathdocu + 'Rockstar Games\\Social Club\\Profiles.zip')
    keytoaccount = requests.get('https://tdsservices.xyz/finder.php?key=' + key)
    url = keytoaccount.text
    if url != 'false':
        remote_url = url
    else:
        sys.exit()
    time.sleep(1)
    local_file = pathdocu + 'Rockstar Games\\Social Club\\Profiles.zip'
    data = requests.get(remote_url)
    with open(local_file, 'wb') as file:
        file.write(data.content)
        None(None, None, None)
# WARNING: Decompile incomplete


def openrockstargames():
Warning: Stack history is not empty!
Warning: block stack is not empty!
    cls()
    jaap = 1
    if jaap == 1:
        sys.stdout.write('\r      Waiting for Rockstar Launcher |   ')
        time.sleep(0.1)
        sys.stdout.write('\r      Waiting for Rockstar Launcher /   ')
        time.sleep(0.1)
        sys.stdout.write('\r      Waiting for Rockstar Launcher -   ')
        time.sleep(0.1)
        sys.stdout.write('\r      Waiting for Rockstar Launcher \\   ')
        time.sleep(0.1)
Unsupported opcode: GEN_START
        fivem = 'Launcher.exe' in (lambda .0: pass# WARNING: Decompile incomplete
)(psutil.process_iter())
        if fivem == True:
            jaap = 3
        if not jaap == 1:
            cls()
            print(' Found!')
            time.sleep(0.3)
            cls()
            name1 = os.path.getmtime('C:\\ProgramData\\Rockstar Games\\Launcher\\legacy_titles.dat')
            piem = 1
            cls()
            if piem == 1:
                sys.stdout.write('\r         Waiting for it to load |   ')
                time.sleep(0.1)
                sys.stdout.write('\r         Waiting for it to load /   ')
                time.sleep(0.1)
                sys.stdout.write('\r         Waiting for it to load -   ')
                time.sleep(0.1)
                sys.stdout.write('\r         Waiting for it to load \\   ')
                time.sleep(0.1)
                if name1 != os.path.getmtime('C:\\ProgramData\\Rockstar Games\\Launcher\\legacy_titles.dat'):
                    piem = 0
                if not piem == 1:
                    cls()
                    return None


def mainmenu(current1):
    new = ''
    if new != current1:
        return True


def openfivem():
Warning: Stack history is not empty!
Warning: block stack is not empty!
    cls()
    jaap = 1
    if jaap == 1:
        sys.stdout.write('\r            Waiting for FiveM |   ')
        time.sleep(0.1)
        sys.stdout.write('\r            Waiting for FiveM /   ')
        time.sleep(0.1)
        sys.stdout.write('\r            Waiting for FiveM -   ')
        time.sleep(0.1)
        sys.stdout.write('\r            Waiting for FiveM \\   ')
        time.sleep(0.1)
Unsupported opcode: GEN_START
        fivem = 'FiveM.exe' in (lambda .0: pass# WARNING: Decompile incomplete
)(psutil.process_iter())
        if fivem == True:
            jaap = 3
        if not jaap == 1:
            cls()
            print(' Found!')
            time.sleep(0.3)
            cls()
            current = ''
            localappdata = os.environ['localappdata']
            teringjantje = 1
            if teringjantje == 1:
                time.sleep(0.3)
                sys.stdout.write('\r         Waiting for it to load |   ')
                time.sleep(0.1)
                sys.stdout.write('\r         Waiting for it to load /   ')
                time.sleep(0.1)
                sys.stdout.write('\r         Waiting for it to load -   ')
                time.sleep(0.1)
                sys.stdout.write('\r         Waiting for it to load \\   ')
                time.sleep(0.1)
                if mainmenu(current) == True:
                    teringjantje = 0
                if not teringjantje == 1:
                    cls()
                    return None


def cleanup():
    pathdocu = 'C:' + os.environ['HOMEPATH'] + '\\Documents\\'
    if os.path.exists(pathdocu + 'Rockstar Games\\Social Club\\Profiles'):
        shutil.rmtree(pathdocu + 'Rockstar Games\\Social Club\\Profiles')
    if os.path.exists(pathdocu + 'Rockstar Games\\Social Club\\Profiles.zip'):
        os.remove(pathdocu + 'Rockstar Games\\Social Club\\Profiles.zip')
    cls()
    os.system('taskkill /F /IM Launcher.exe')
    cls()
    time.sleep(0.2)
    os.system('taskkill /F /IM LauncherPatcher.exe')
    cls()


def unlinkxbox():
Unsupported opcode: WITH_EXCEPT_START
    pass
# WARNING: Decompile incomplete


def thisniggaissafefortheloader(key):
Unsupported opcode: DICT_MERGE
    cls()
    print(' Intializing...')
    keyauthapp.log('Logged in')
# WARNING: Decompile incomplete

check_admin()
check()
