import os
import subprocess as sp

paths = {
    'notepad': "C:\\Windows\\System32\\notepad.exe",
    'whatsapp': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe",
    'edge':"https://www.msn.com/en-in//feed?ocid=wn_startbrowsing",
     'disc':"C:\\",
    'disd':"D:\\" ,
    'dise':"E:\\",
    'disf':"F:\\",
    'crome':"https://www.google.co.in//",
    'nptel':"https://swayam.gov.in//mycourses",
}


def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])

def open_diskd():
    os.startfile(paths['disd'])

def open_diskc():
    os.startfile(paths['disc'])

def open_diske():
    os.startfile(paths['dise'])

def open_diskf():
    os.startfile(paths['disf'])

def open_cmd():
    os.system('start cmd')


def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)


def open_calculator():
    sp.Popen(paths['calculator'])

def open_Edge():
    os.startfile(paths['edge'])

def open_chrome():
    os.startfile(paths['crome'])

def open_nptel():
    os.startfile(paths['nptel'])
