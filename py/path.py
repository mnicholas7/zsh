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

    #     # ж χ ♪ ♫  
    #     # ♪ж♫
    # ♫
    # ♪  へ⌂ *  ≫
    # ♪    # ж χ ♪ ♫  
    #     #
    #     ♫♪♫♪♫♪♫
    # i     q   
    # sdfj 
    breakpoint()
    # PATH = [ i = i.rstrip() for i in PATH ]
    # [ print(i, "\n") for i in list(globals().items()) ]
    # [ print(i, " ♪ \n ♫ ж> ") for i in list(globals().items()) ]
    # [ print(i, " ж\n ♫ >> ") for i in list(globals().items()) 
    # [ print(" ♫ ≫ " + str(i) + " ≪ ж \n" ) for i in list(globals().items()) ]
    [ print(i, "\n> ") for i in list(globals().items()) ]
    [ print("\nж ", i) for i in list(globals().items()) ]
    [ print("\n",i) for i in list(globals().items()) ]




    #         gg My!

    print(f"""

    Current Path Before:
    """)
    for x,i in enumerate(PATH):
        print(f"{x:2}:{i}")

    # remove dups
    # PATH = set(PATH)
    # PATH = list(PATH)

    DIRS = [ 'aws','bin','jinja','jq','py','.local/bin' ]

    PAT = re.compile(f"{HOME}/({ '|'.join(DIRS) })\/?")

    #/home/nicholas/.local/lib/python3.8/site-packages

    NEW_PATH = []

    # for DIR in DIRS:
    #   PAT = re.compile(f"{HOME}\/{DIR}\/?")

    for x,z in enumerate(PATH):
        # print(f"▼ {PAT=} {x=} with {z=}")
        if re.match(PAT, z):
            # print(f"  ignoring .. {PAT=} which matched {z=}")
            pass
        else:
            if i not in NEW_PATH:
                print(f"  appending {z=}")
                NEW_PATH.append(z)
            else:
                print(f" already in path: {z=}")
                pass



    print(f"""

    Path After Prune:
    """)

    for a,b in enumerate(NEW_PATH):
        print(f"{a:2}:{b}")

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




