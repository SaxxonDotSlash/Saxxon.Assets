###NO LONGER USED IN main.py 
###ALL FUNCTIONS MOVED TO SAME FILES



#import modules
import subprocess


#Variables
ipaddress = 'placeholder'
nmap_ver_correct = 'NMAP'


#functions
def get_ip():
    ipaddress = int(input("What is the target IP? "))


def ping():
    subprocess.run(['ping ', ipaddress])


def nmap_simple():
    print(['nmap ', ipaddress])

def pkg_mnger():
    nmap_chk = subprocess.run(['dpkg-query ', '-W ', '-f=\'${Status} ', '${Version}\n\' ', 'nmap'])
    #Command for pkg check
    #dpkg-query -W -f='${Status} ${Version}\n' nmap

    if nmap_chk == nmap_ver_correct:
        print("NMAP is installed correctly.")
    else:
        print("NMAP not installed or needs to be updated. \n")
        nmap_install = input("Would you like to install NMAP right now? (y/n) \n")
        if nmap_install == "y":
            subprocess.run(['sudo ', 'apt-get ', 'install ', 'nmap'])
            print("NMAP has been successfully installed!")