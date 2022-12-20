import subprocess
import os

def check_for_packages(package):
    cmd = (package+" --version" or package+" -v").split(" ")
    sp = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
    rc = sp.wait()
    if(rc==1):
        print(">> you have to install {}".format(cmd[0]))
        os.system("pause")
    else:
        print(">> {} already exist in your machine".format(cmd[0]))

check_for_packages("node")