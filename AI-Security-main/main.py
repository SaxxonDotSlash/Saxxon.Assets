import subprocess

#Variables
q = "q"
ipaddress = 'placeholder'
nmap_ver_correct = 'NMAP'


#Functions
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

def recon():
    recon_sel = input("Reconnaisance \n1: NMAP \n0: Main Menu \n")
    if recon_sel == 1:
        nmap_simple()
        main()
    if recon_sel == 0:
        main()

def exploitation():
    exp_sel = input("Exploitation \n0: Main Menu \n")
    if exp_sel == 0:
        main()

def maintaining_access():
    ma_sel = input("Maintaining Access \n0: Main Menu")
    if ma_sel == 0:
        main()

def reporting():
    report_sel = input("Reporting \n0: Main Menu")
    if report_sel == 0:
        main()

def debug():
    deb_sel = int(input('DEBUG: \n1: Set IP \n2: Ping \n3: Package Manager \n0: Back to Menu'))
    if deb_sel == 1:
        get_ip()
        main()
    elif deb_sel == 2:
        ping()
        main()
    elif deb_sel == 3:
        pkg_mnger()
        main()
    elif deb_sel == 0:
        main()

def main():
    main_sel = input('Welcome to the AI SECURITY Testing Application! \nPlease select an option \n1: Reconnaissance \n2: Exploitation \n3: Maintaining Access \n4: Reporting \n0: Debug \nq: Quit \n')
    #reconnaissance
    if int(main_sel) == 1:
        recon()
        main()
    #Exploitation
    elif int(main_sel) == 2:
        exploitation()
        main()
    #Maintaining access
    elif int(main_sel) == 3:
        maintaining_access()
        main()
    #Reporting
    elif int(main_sel) == 4:
        reporting()
        main()
    #Debug
    elif int(main_sel) == 0:
        debug()
        main()
    elif main_sel in ["q"]:
        print("Quitting AI Security Testing Application")

def start():
    get_ip()
    main()

start()