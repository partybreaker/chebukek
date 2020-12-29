import os, sys
import subprocess
from subprocess import check_output


OPTIONS = '''
1. Take screenshot
'''



def logo():
    logo = '''


_________ .__          ___.           __           __    
\_   ___ \|  |__   ____\_ |__ ___.__.|  | __ ____ |  | __
/    \  \/|  |  \_/ __ \| __ <   |  ||  |/ // __ \|  |/ /
\     \___|   Y  \  ___/| \_\ \___  ||    <\  ___/|    < 
 \______  /___|  /\___  >___  / ____||__|_ |\___  >__|_ |
        \/     \/     \/    \/\/          \/    \/     \/

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



def get_screenshot():
    subprocess.call(["sh", "./script/screenshot.sh"])
    print("Screenshot is taken")


cmds = {
    "1": get_screenshot
}

def main():
    # os.system('cls')
    print(logo())
    try:
        while True:
            choice = input('\n%s' % OPTIONS)
            if choice not in cmds:
                print('[!] Invalid Choice')
                continue
            cmds.get(choice)()
    except KeyboardInterrupt:
        print('[!] Ctrl + C detected\n[!] Exiting')
        sys.exit(0)
    except EOFError:
        print('[!] Ctrl + D detected\n[!] Exiting')
        sys.exit(0)


if __name__ == "__main__":
    main()