import shutil
import sys
import time
import zipfile
import os
import re
from re import *
import glob
status = "Microsoft Windows [Version 0.1]\n(c) 2018 Jarvis Group. All rights reserved.\n"
print(status)
def main():
    get_path = os.path.realpath(os.getcwd())
    get_command = input(get_path+">")
    split = get_command.split()
    #get_input_command = get_command
    if len(split) == 0:
        pass
    elif get_command == "cd":
        print(get_path)
        print()
    elif split[0] == "cd" and len(split) > 1:
        get_input_command = split[1]
        os.getcwd()
        change_path = os.chdir(get_input_command)
        get_path = os.path.realpath(os.getcwd())
        print()
    elif get_command == "cd/":
        change_path = os.chdir("/")
        get_path = os.path.realpath(os.getcwd())
        print()
    elif get_command == "cd..":
        os.getcwd()
        change_path = os.chdir('..')
        get_path = os.path.realpath(os.getcwd())
        print()
    elif get_command == "c:" or get_command == "d:":
        os.getcwd()
        change_path = os.chdir(get_command)
        get_path = os.path.realpath(os.getcwd())
        print()
    elif get_command == "cat >" and len(split) > 1:
        os.getcwd()
        make_file = split[2]
        if(os.path.isfile(split[2])) == True:
            print("File Already exist")
        else:
            f = open(make_file,"w")
            f.close()
            print()
    elif str(split) > str(2):
        if split[0] == "mkdir":
            os.getcwd()
            os.mkdir(split[1])
            get_path = os.path.realpath(os.getcwd())
            print()
        elif split[0] == "rmdir":
            os.getcwd()
            try:
                get_path = os.path.realpath(os.getcwd())
                remove = os.rmdir(split[1])
                print()
            except OSError as e:
                print(e)
        elif split[0] == "rm":
            os.getcwd()
            try:
                os.remove(split[1])
                get_path = os.path.realpath(os.getcwd())
                print()
            except OSError as e:
                print(e)
while True:
    main()
