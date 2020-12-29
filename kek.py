import os, sys, platform
import subprocess
from subprocess import check_output


OPTIONS = '''
1. Take screenshot
2. Schedule screenshot
3. Check host
4. Exit
'''



def logo():
    logo = '''


           
    _________ .__          ___.           __           __                   .  . 
    \_   ___ \|  |__   ____\_ |__ ___.__.|  | __ ____ |  | __              .,(/#*,./(,*  
    /    \  \/|  |  \_/ __ \| __ <   |  ||  |/ // __ \|  |/ /             .*./*  ,,.,,,*,..*,,*
    \     \___|   Y  \  ___/| \_\ \___  ||    <\  ___/|    <               .,.*,***,,*,**,.,/((,.,,,,,    
     \______  /___|  /\___  >___  / ____||__|_ |\___  >__|_ |              ..,,***,. .*......,,,*.,*,***/**#((/*(
            \/     \/     \/    \/\/          \/    \/     \/               ,.,,/,*/,,,,.*.....,....,*/,/*,,*#%#.
                                                                              .,,./,*,*,,,,,*,,**,*,,,***(%@(   
                                                                                   ,/(#%((,#*(*#(##(#%&(.   

'''
    return logo

def menu():
    while True:
        try:
            choice = str(input('\n[?] DO YOU WANT TO CONTINUE? \n')).lower()
            if choice[0] == 'y':
                return
            if choice[0] == 'n':
                sys.exit(0)
                break
        except ValueError:
            sys.exit(0)


def checkHost():
    if os.name == "posix":
        print('\n [+] Ok \n')
        print('OS - {}, kernel version - {}'.format(platform.system(), platform.release()))
    else:
        print('[!] HUITA')
        sys.exit(0)



def cmd_takeScreenshot():
    subprocess.call(["sh", "./script/screenshot.sh"])
    print("Screenshot is taken")


def cmd_screenshotTaskScheduler():
    pass


cmd = {
    "1" : cmd_takeScreenshot,
    "2" : cmd_screenshotTaskScheduler,
    "3" : checkHost,
    "4" : lambda: sys.exit(0),
}

def main():
    # os.system('cls')
    print(logo())
    try:
        while True:
            choice = input('\n%s' % OPTIONS)
            if choice not in cmd:
                print('[!] Invalid Choice')
                continue
            cmd.get(choice)()
    except KeyboardInterrupt:
        print('[!] Ctrl + C detected\n[!] Exiting')
        sys.exit(0)
    except EOFError:
        print('[!] Ctrl + D detected\n[!] Exiting')
        sys.exit(0)


if __name__ == "__main__":
    main()