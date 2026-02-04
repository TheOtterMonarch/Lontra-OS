import os
appdata = os.getenv('LOCALAPPDATA')
import pathlib
from pathlib import Path
import time
from time import sleep as wait
from getpass import getpass
import datetime
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

version = "v1.0"

path = ""

def check_password_file(appdata):
    global path
    path = Path(appdata) / "Lontra" / "OS" / "password.txt"

    if path.exists():
        passwordText = path.read_text(encoding="utf-8")
        return passwordText
    else:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.touch()
        return "𓃾"

def setup():
    basePath = Path(appdata) / "Lontra" / "root"
    appDataPath = Path(appdata) / "Lontra"
    if not os.path.isdir(basePath):
        if not os.path.isdir(appDataPath):
            os.mkdir(appDataPath)
        os.mkdir(basePath)
        if not os.path.isdir(Path(basePath) / "Desktop"):
            os.mkdir(Path(basePath) / "Desktop")
        if not os.path.isdir(Path(basePath) / "Documents"):
            os.mkdir(Path(basePath) / "Documents")
        if not os.path.isdir(Path(basePath) / "Apps"):
            os.mkdir(Path(basePath) / "Apps")
    if not os.path.isdir(Path(basePath) / "Apps" / "calculator.lapp"):
        if not os.path.isdir(Path(basePath) / "Apps"):
            os.mkdir(Path(basePath) / "Apps")
        with open(Path(basePath) / "Apps" / "calculator.lapp", "w") as f:
            f.write("""# This program creates a calculator in a command line interface

print("Welcome to the calculator!")
print()

while True: # Main loop
    num1 = float(input("Please input the first number for your calculation: ")) # Recieves and documents input for the first number
    num2 = float(input("Please input the second number for your calculation: ")) # Recieves and documents input for the second number
    
    print() # Prints an empty line
    
    print("Would you like to add these numbers together, subtract the second from the first, multiply them together, or divide the")
    operator = input("first by the second? Type A, S, M or D: ") # Recieves and documents input for which mathematical operator to use
    
    print() # Prints an empty line
    
    if operator == "A" or operator == "a": # This section performs and outputs the calculation
        print("The answer for your calculation is",num1+num2)
    elif operator == "S" or operator == "s":
        print("The answer for your calculation is",num1-num2)
    elif operator == "M" or operator == "m":
        print("The answer for your calculation is",num1*num2)
    elif operator == "D" or operator == "d":
        print("The answer for your calculation is",num1/num2)
    else: # This asks the user to try again if they did not give valid input
        print("Sorry, that didn't work. Please restart the program and try  again.")
        break
    
    print() # Prints an empty line
    
    print("Type Y if you would like to perform another calculation.")
    response = input("Otherwise, press Enter. ") # Allows the user to choose whether to restart the program 
    if response != "Y":
        break""")


def _cipher(start: str) -> str:
    result = []
    for c in start:
        if 'a' <= c <= 'z':
            result.append(chr((ord(c) - ord('a') + 1) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') + 1) % 26 + ord('A')))
        elif '0' <= c <= '9':
            result.append(chr((ord(c) - ord('0') + 1) % 10 + ord('0')))
        else:
            result.append(c)
    return ''.join(result)


def _decipher(start: str) -> str:
    result = []
    for c in start:
        if 'a' <= c <= 'z':
            result.append(chr((ord(c) - ord('a') - 1) % 26 + ord('a')))
        elif 'A' <= c <= 'Z':
            result.append(chr((ord(c) - ord('A') - 1) % 26 + ord('A')))
        elif '0' <= c <= '9':
            result.append(chr((ord(c) - ord('0') - 1) % 10 + ord('0')))
        else:
            result.append(c)
    return ''.join(result)

setup()
    
if check_password_file(appdata) == "𓃾" or check_password_file(appdata) == "":
    inputPassword1 = input("Please choose your password: ")
    inputPassword2 = input("Confirm password: ")
    if inputPassword1 == inputPassword2:
        with open(path, "w") as f:
            encryptedPassword = _cipher(inputPassword1)
            f.write(encryptedPassword)
else:
    while True:
        encryptedPassword = ""
        with open(path, "r") as f:
            correctPassword = f.read()
            decryptedPassword = _decipher(correctPassword)
        inputPassword = getpass("Enter password: ")
        if inputPassword != decryptedPassword:
            print(Fore.RED + "Password Incorrect. Please try again.")
            print()
        else:
            break

rootPath = Path(appdata) / "Lontra"
localPath = "root"
pathName = "root"
print()
print("Welcome to...")
wait(1)
print(Back.GREEN + Fore.BLACK + r"""
╔════════════════╗
║    Lontra OS   ║
╚════════════════╝
""")
wait(0.5)



# MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
# MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
# MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
# MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN MAIN
while True:
    currentPath = Path(rootPath) / localPath
    print()
    cmdStr = input(Fore.CYAN + pathName + "> " + Fore.WHITE)
    cmd = cmdStr.split(' ', 1)[0]

    # help
    if cmd == "help":
        print("You are using Lontra OS " + version + ". You can use the following commands: \n\nhelp - Lists all commands\n\nabout - Provides information about Lontra OS\n\nls - Lists all files and folders in the current directory\n\ncd - Navigates to a directory\n\nmk - Creates a new file or folder\n\nrm - Deletes a file or folder\n\nedit - Edits the contents of a file\n\napps - Lists all apps installed on the system\n\nrun - Runs an app from the Apps folder")

    # list
    elif cmd == "ls":
        if os.listdir(Path(rootPath) / localPath):
            print(os.listdir(Path(rootPath) / localPath))
        else:
            print(Fore.RED + "This directory is empty!")

    # cd
    elif cmd == "cd":
        if len(cmdStr.split()) == 1:
            print(Fore.RED + "You must provide a directory!")
        else:
            if os.path.isdir(Path(rootPath) / localPath / cmdStr.split(' ', 1)[1]):
                if cmdStr.split(' ', 1)[1] == "..":
                    localPath = "root"
                    pathName = str(localPath)
                else:
                    localPath = Path(localPath) / cmdStr.split(' ', 1)[1]
                    pathName = str(localPath)
            else:
                print(Fore.RED + "Invalid directory!")

    # mk
    elif cmd == "mk":
        if len(cmdStr.split()) == 1:
            print(Fore.RED + "You must provide a name!")
        else:
            path2Add = Path(currentPath) / cmdStr.split(' ', 1)[1]
            if path2Add.suffix:
                path2Add.parent.mkdir(parents=True, exist_ok=True)
                if not path2Add.exists():
                    path2Add.touch()
                    print(Fore.GREEN + "Successfully created file!")
            else:
                os.makedirs(path2Add)
                print(Fore.GREEN + "Successfully created folder!")
    
    # rm
    elif cmd == "rm":
        if cmdStr.split() == 1:
            path2Use = Path(currentPath) / cmdStr.split(' ', 1)[1]
            if os.path.exists(path2Use):
                if path2Use.suffix:
                    os.remove(path2Use)
                    print(Fore.GREEN + "Successfully deleted file!")
                else:
                    try:
                        os.rmdir(path2Use)
                        print(Fore.GREEN + "Successfully deleted folder!")
                    except:
                        print(Fore.RED + "This folder is not empty. Please delete all files inside the folder before deleting.")
            else:
                print(Fore.RED + "Path not found!")
        else:
            print(Fore.RED + "Path not found!")
    
    # about
    elif cmd == "about":
        print("\nLontra OS " + version + "\n\nLontra OS is a lightweight, open-source operating system.\nIt runs as an app, however, it has an independent file system.\nIt was designed for people who want to use a different operating system, but don't want to uninstall their current one.")
    
    # version
    elif cmd == "version":
        print(version)
    
    # edit
    elif cmd == "edit":
        if len(cmdStr.split()) != 1:
            path2Use = Path(currentPath) / cmdStr.split(' ', 1)[1]
            if os.path.exists(path2Use) and path2Use.suffix:
                with open(path2Use) as f:
                    print("Current file contents:\n" + f.read() + "\n\n")
                    print("Enter new content (finish with a single '.' on a line, or finish now to cancel):")
                    inputReceived = ""
                    fullInput = ""
                    while not inputReceived == ".":
                        inputReceived = input()
                        if inputReceived != ".":
                            fullInput = fullInput + inputReceived + "\n"
                    if fullInput == "":
                        print(Fore.GREEN + "Edit cancelled.")
                    else:
                        with open(path2Use, "w") as f:
                            f.write(fullInput)
                            print(Fore.GREEN + "Changes made!")
            else:
                print(Fore.RED + "Invalid path!")
        else:
            print(Fore.RED + "Please provide a file to edit!")
        
    # apps
    elif cmd == "apps":
        if not os.listdir(Path(rootPath) / "root" / "Apps"):
            print(Fore.RED + "No apps installed!")
        else:
            print(os.listdir(Path(rootPath) / "root" / "Apps"))
    
    # run
    elif cmd == "run":
        if len(cmdStr.split()) != 1:
            appPath = Path(rootPath) / "root" / "Apps" / cmdStr.split(' ', 1)[1]
            if os.path.exists(appPath):
                with open(appPath) as f:
                    appCode = f.read()
                try:
                    exec(appCode)
                except:
                    print(Fore.RED + "\n\nSorry, something went wrong. The app has crashed!")
            else:
                print(Fore.RED + "Invalid app!")
        else:
            print(Fore.RED + "Please provide an app to run!")
    
    # Unknown command
    else:

        print(Fore.RED + "Unknown command!")
