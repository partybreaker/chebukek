import os, sys
import subprocess
from subprocess import check_output


def logo():
    logo = '''


_________ .__          ___.           __           __    
\_   ___ \|  |__   ____\_ |__ ___.__.|  | __ ____ |  | __
/    \  \/|  |  \_/ __ \| __ <   |  ||  |/ // __ \|  |/ /
\     \___|   Y  \  ___/| \_\ \___  ||    <\  ___/|    < 
 \______  /___|  /\___  >___  / ____||__|_ \\___  >__|_ |
        \/     \/     \/    \/\/          \/    \/     \/

'''
    return logo


def main():
    # os.system('cls')
    print(logo())


if __name__ == "__main__":
    main()