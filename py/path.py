#!/usr/bin/python3

import sys
import os
import subprocess
import re


def main(mode=None):
    #WSL_USER = subprocess.run(["whoami"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True )

    HOME = os.environ.get('HOME')
    USER = os.environ.get('USER')
    PATH = os.environ.get('PATH')

    PATH = PATH.split(':')

    breakpoint()

    print(f"""

    Current Path Before:
    """)
    for count,item in enumerate(PATH):
        print(f"{count:2}:{item}")

    breakpoint()
    

    # remove dups
    # PATH = set(PATH)
    # PATH = list(PATH)

    #DIRS = [ 'aws','bin','jinja','jq','py','.local/bin' ]
    DIRS = [ 'aws','bin','jinja','jq','py' ]

    PAT = re.compile(f"{HOME}/({ '|'.join(DIRS) })\/?")

    #/home/nicholas/.local/lib/python3.8/site-packages

    NEW_PATH = []

    # for DIR in DIRS:
    #   PAT = re.compile(f"{HOME}\/{DIR}\/?")

    breakpoint()
    for counter,z in enumerate(PATH):
        print(f"▼ {PAT=} {counter=} with {z=}")
        breakpoint()
        if re.match(PAT, z):
            breakpoint()
            print(f"  MATCHED SO SKIP .. {PAT=} which matched {z=}")
        else:
            breakpoint()
            if z not in NEW_PATH:
                print(f"  PATH ADD: {counter=} {z=}")
                breakpoint()
                NEW_PATH.append(z)
            else:
                print(f" DO NOTHING: already in path: {z=}")
                breakpoint()



    breakpoint()
    print("Path After")

    for f,g in enumerate(NEW_PATH):
        print(f"{f:2}:{g}")
        breakpoint()


    # for DIR in DIRS:
    #     NEW_PATH.append(f"{HOME}/{DIR}")




    # os.environ['PATH'] = ":".join(NEW_PATH)
    # if mode:
    #     print(f"""

    #     Final Path:
    #     """)
    #     for x,i in enumerate(NEW_PATH):
    #         print(f"{x:2}:{i}")
    # else:
    #     print(":".join(NEW_PATH))

if __name__ == '__main__':
     
    # try:
    #     if sys.argv[1]:
    #         main(sys.argv[1])
    # except IndexError:
    main()




