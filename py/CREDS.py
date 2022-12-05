#!/usr/bin/python3
"""
Michael Nicholas' Credentials module which uses the pass utility,
  pass is a very simple password store that keeps passwords inside gpg2(1) encrypted files
"""
import os
import subprocess
import sys
from MN_API import PRINT_FMT_MSG, RAND_CH
import re


def ERROR():

    x = RAND_CH()

    MSG = f"""

    [ Unauthorized ]

    [ Please send a message to Michael Nicholas on teams ,.. ]

    [ This attempt has been logged {x} ]

    """

    MSG = PRINT_FMT_MSG(MSG)

    #sys.exit(1)


def main(PASS_NAME):
    
    # LINES = os.popen(f"cat ~/.{PASS_NAME}").read().rstrip()

    # if not (re.match(f"^cat:", LINES:
    #     LINES = LINES.split()

    #     # x = []

    #     # for line in LINES:
    #     #     line = line.rstrip()
    #     #     x.append(line)
    #     x = [ str.rstrip(line) for line in LINES ]

    #     #breakpoint()

    #     USERNAME = x[0]
    #     PASS = x[1]

    # else:
    #     LINES = os.popen("pass " + PASS_NAME).read().rstrip()

    #     if LINES:
    #         LINES = LINES.split()

    #         x = []

    #         # for line in LINES:
    #         #     line = line.rstrip()
    #         #     x.append(line)
    #         x = [ str.rstrip(line) for line in LINES ]

    #         USERNAME = x[0]
    #         PASS = x[1]

    #     else:
    #         ERROR()

    #return USERNAME, PASS
    
    # list of strings representing the command
    
    try:
        # stdout = subprocess.PIPE lets you redirect the output
        #FILE = f"~/.{PASS_NAME} &> /dev/null"
        #FILE = f"~/.{PASS_NAME}"
        #args = ['cat', '~/.', PASS_NAME ]
        #LINES = subprocess.Popen(args, stdout=subprocess.PIPE)
        #LINES = os.popen(args, stdout=subprocess.PIPE)
        LINES = os.popen(f"cat ~/.{PASS_NAME}").read().rstrip()
        #LINES = subprocess.Popen(args)
        #breakpoint()
        try:
            #LINES = LINES.stdout.readlines()
            LINES = LINES.split()

            if LINES:
                x = [ str.rstrip(line) for line in LINES ]
                USERNAME = x[0]
                PASS = x[1]
                return USERNAME, PASS
            else:
                #sys.exit(f"\nNo dice on credentials..\n")
                #pass
                raise FileNotFoundError
        except UnboundLocalError:
            raise FileNotFoundError
            #pass


    except FileNotFoundError:
        try:
            # args = ['pass', PASS_NAME]
            # LINES = subprocess.Popen(args, stdout=subprocess.PIPE)
            # LINES = LINES.stdout.readlines()

            LINES = os.popen("pass " + PASS_NAME).read().rstrip()

            try:
                LINES = LINES.split()

                if len(LINES) >= 2:
                    USERNAME = LINES[0]
                    PASS = LINES[1]
                    return USERNAME, PASS
                else:
                    #sys.exit(f"\nNo dice on credentials..\n")
                    sys.exit(ERROR())

            except UnboundLocalError:
                raise FileNotFoundError

        except FileNotFoundError:
            #sys.exit(f"\nNo dice on credentials..\n")
            sys.exit(ERROR())

    #FILE = f"{PASS_NAME}"
    
    # list of strings representing the command
    #    args = ['pass', PASS_NAME]
    #    
    #    try:
    #        # stdout = subprocess.PIPE lets you redirect the output
    #        res = subprocess.Popen(args, stdout=subprocess.PIPE)
    #    except FileNotFoundError:
    #        exit()
    #
    # except OSError:
    #     print("error: popen")
    #     exit(-1) # if the subprocess call failed, there's not much point in continuing
    # except Exception:
    #     HANDLE_IT("Exception", "test")
    #     exit(-1) # if the subprocess call failed, there's not much point in continuing
    
    # res.wait() # wait for process to finish; this also sets the returncode variable inside 'res'
    # if res.returncode != 0:
    #     print("  os.wait:exit status != 0\n")
    #     exit(-1)

    # else:
    #     print ("os.wait:({},{})".format(res.pid, res.returncode))
    
    # access the output from stdout
    # result = res.stdout.read()
    # print ("after read: {}".format(result))
    # 
    # print ("exiting")


if __name__ == "__main__":

    if len(sys.argv) == 2:

        PASS_NAME = sys.argv[1]
        main(PASS_NAME)
        sys.exit()

    else:
        print(
            """

        Usage:
          CREDS.py <pass name>

        This script uses the Linux 'pass' utility to keep secrets encrypted on disk.

        The <pass name> is the name of a password file already set up in the 'pass' 
        utility.

        The first line and second line of that pass output are returned from the func.



        """
        )
        sys.exit()

    main()
