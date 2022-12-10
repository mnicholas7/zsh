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

    #print(f"""

    #Current Path Before:
    #""")
    #for x,i in enumerate(PATH):
    #    print(f"{x:2}:{i}")

    # remove dups
    # PATH = set(PATH)
    # PATH = list(PATH)

    DIRS = [ 'aws','bin','jinja','jq','py' ]

    PAT = re.compile(f"{HOME}/({ '|'.join(DIRS) })\/?")

    NEW_PATH = []

    # for DIR in DIRS:
    #   PAT = re.compile(f"{HOME}\/{DIR}\/?")

    for x,i in enumerate(PATH):
        # print(f"▼ {PAT=} {x=} with {i=}")
        if re.match(PAT, i):
            # print(f"  ignoring .. {PAT=} which matched {i=}")
            pass
        else:
            if i not in NEW_PATH:
                #print(f"  appending {i=}")
                NEW_PATH.append(i)
            else:
                #print(f" already in path: {i=}")
                pass



    # print(f"""

    # Path After Prune:
    # """)
    # for x,i in enumerate(NEW_PATH):
    #     print(f"{x:2}:{i}")


    for DIR in DIRS:
        NEW_PATH.append(f"{HOME}/{DIR}")




    # os.environ['PATH'] = ":".join(NEW_PATH)
    if mode:
        pass
        print(f"""

        Final Path:
        """)
        for x,i in enumerate(NEW_PATH):
            print(f"{x:2}:{i}")
    else:
        print(":".join(NEW_PATH))

if __name__ == '__main__':
     
    try:
        if sys.argv[1]:
            main(sys.argv[1])
    except IndexError:
        main()




