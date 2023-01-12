#!/usr/bin/python3

import csv
import copy
import json
import os
import subprocess
import pandas as pd
import traceback
import sys
import time
import re
import random
# from traceback_with_variables import activate_by_import
# import traceback_with_variables
import pprint
import importlib
import tabulate

pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)
pd.set_option("display.max_colwidth", None)


def more(d: dict) -> None:
    for k,v in d.items():
        if d[k] == d:
            # don't print out yourself
            continue
        elif k == '__builtins__':
            # too much noise, don't care to print
            continue

        print(f"{k:20} ==> {v}")
        _ = input()

locs = locals()
globs = globals()

q = lambda: quit()
l = lambda: more(locs)
g = lambda: more(globs)




def EXAG():
    stuff = globals()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stuff)

def EXAL():
    stuff = globals()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(stuff)

def EXA(STUFF):
    STUFF = STUFF._asdict()
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(dict(STUFF))

def EXAR(STUFF):
    STUFF = STUFF._asdict()
    pp = pprint.pformat(dict(STUFF), indent=4, compact=False)
    return pp

def RLOAD(X):
    importlib.reload(X)

def MAIL(MSG, SUB, TO, FILE=None):

    MSG = f"""
<html>
<head>
</head>
<body>
<pre style="white-space: pre">
{MSG}
</pre>
</body>
"""

    if FILE:
      COMMAND = f"/usr/bin/mail -a 'Content-Type: text/html; charset=UTF-8' -A {FILE} -s '{SUB}' {TO} << EOF\n{MSG}\nEOF"
    else:
      COMMAND = f"/usr/bin/mail -a 'Content-Type: text/html; charset=UTF-8' -s '{SUB}' {TO} << EOF\n{MSG}\nEOF"

  
    try:
        RESULT = subprocess.run(COMMAND, input=None, stderr=subprocess.PIPE, stdout=subprocess.PIPE, timeout=10, encoding='utf-8', shell=True)

        if RESULT:
            if RESULT.returncode == 0:
                return True
            else:
                return False
        else:
            return False
    except:
        pass



def SLEEP_AND_NETCAT(HOSTNAME, LOGNAME):

    while not re.match(
        r".*succeeded.*", os.popen(f"nc -vv -w5 {HOSTNAME} 22 2>&1 ").read().rstrip()
    ):
        TIME = os.popen("date").read()
        MSG = f"\n  SLEEP_AND_NETCAT() -> TCP port 22(ssh), NOT UP yet on: {HOSTNAME} at {TIME}"
        print(MSG)
        stringAppendToFile(MSG, "main", LOGNAME)

        print(f"SNOOZE 30: {HOSTNAME}")
        SNOOZE(30)

    return None, None

def SLEEP_AND_NETCAT2(HOSTNAME, LOGNAME):

    COMMAND = f"nc -vv -w5 {HOSTNAME} 22 "

    def RUNNIT(COMMAND):

        RESULT = subprocess.run(COMMAND, input=None, stderr=subprocess.PIPE, stdout=subprocess.PIPE, timeout=10, encoding='utf-8', shell=True)

        if RESULT:

            if RESULT.returncode == 0:

                TIME = os.popen("date").read()
                MSG = f"\n  SLEEP_AND_NETCAT2(): returned SUCCESSFUL {RESULT.returncode=} {HOSTNAME} at {TIME}"
                MSG += f"\n  {RESULT.stdout=} {RESULT.stderr=}"
                print(MSG)
                stringAppendToFile(MSG, "main", LOGNAME)

                return RESULT.stdout, RESULT.stderr

            else:

                TIME = os.popen("date").read()
                MSG = f"\n  SLEEP_AND_NETCAT2(): returned {RESULT.returncode=} {HOSTNAME} at {TIME}"
                MSG += f"\n  {RESULT.stdout=} {RESULT.stderr=}"
                print(MSG)
                stringAppendToFile(MSG, "main", LOGNAME)

                return RESULT.stdout, RESULT.stderr


    STDOUT, STDERR = RUNNIT(COMMAND)

    return STDOUT, STDERR



def SNOOZE(x):

    print(f"  SNOOZE for {x} total seconds!")
    z = range(x, 1, -1)
    for i in z:
        m = RAND_CH()
        #MSG = f"{m} {i}"
        MSG = f"{m}"
        #printf(MSG)
        if i % 4 == 0:
            print(MSG, end=" ", flush=True)
        elif i % 1 == 0:
            print('.', end=" ", flush=True)

        time.sleep(1)



def freshDir(OUT_DIR):

    if os.path.exists(OUT_DIR) and os.path.isdir(OUT_DIR):
        #os.system("rm -rf ./" + OUT_DIR )

        ##  commenting both these out bc they are rm -rf'ing my output files!!
        ##  and I can't remember why I did this in the first place!
        ##
        ##  subprocess.run(['rm','-rf', OUT_DIR],check=True, stdout=subprocess.PIPE, universal_newlines=True)

        ##  subprocess.run(['mkdir', OUT_DIR],check=True, stdout=subprocess.PIPE, universal_newlines=True)
        pass
    else:
        subprocess.run(['mkdir', OUT_DIR],check=True, stdout=subprocess.PIPE, universal_newlines=True)
        #os.mkdir(OUT_DIR)

def PRINT_FMT_MSG(MSG, NO=None):
    LIST = MSG.split("\n")

    # if it begins with more than one space, make it two
    LIST = [re.sub(r"^\s+", "  ", item) for item in LIST]

    # if it begins with not space, add two spaces
    LIST = [re.sub(r"^(\S+)", r"  \1", item) for item in LIST]

    # if it ends with more than one space, make it two
    LIST = [re.sub(r"\s+$", "  ", item) for item in LIST]

    # if it ends with not space, add two spaces
    LIST = [re.sub(r"(\S+)$", r"  ", item) for item in LIST]

    MAX_PAD = max([len(i) for i in LIST])

    #MSG += "\n".join([f"|{line:{MAX_PAD}}|" for line in LIST])
    if len(LIST) > 1:
        MSG += "\n".join([f"{line:{MAX_PAD}}" for line in LIST])

    if NO:
        pass
    else:
        print(MSG)

    return MSG, MAX_PAD, LIST

def MAX_PAD(LIST):
    MAX = max([len(i) for i in LIST])
    return(MAX)

def BIG_PRETTY_BOX(MSG):

    MSG = re.sub(r"^\s+", "  ", MSG )
    MSG = re.sub(r"^(\S)+", r"  \1", MSG)
    MSG = re.sub(r"\s+$", "  ", MSG)
    MSG = re.sub(r"(\S)+$", r"\1  ", MSG)


    LIST = MSG.split("\n")

    # if it begins with more than one space, make it two
    #for LINE in LIST:
    #    LINE = re.sub(r"^\s+", "  ", LINE )
    #    LINE = re.sub(r"^(\S)+", r"  \1", LINE)
    #    LINE = re.sub(r"\s+$", "  ", LINE)
    #    LINE = re.sub(r"(\S)+$", r"\1  ", LINE)

    MAX_PAD = max([len(i) for i in LIST])

    #MSG += "\n".join([f"|{line:{MAX_PAD}}|" for line in LIST])
    if len(LIST) > 1:
        MSG += "\n".join([f"{line:{MAX_PAD}}" for line in LIST])

    x = RAND_CH()

    QUAD = round(MAX_PAD / 4)
    QUAD_RAND_INT = random.randint(1, QUAD)
    NEG_QUAD_SPACE = QUAD - QUAD_RAND_INT or 1
    #NEG_QUAD_SPACE = NEG_QUAD_SPACE * 6

    EIGHT = round(MAX_PAD / 8)
    EIGHT_RAND_INT = random.randint(1, EIGHT)
    DIFF_EIGHT = EIGHT - EIGHT_RAND_INT


    E1 = EIGHT_RAND_INT
    E2 = DIFF_EIGHT


    THIRD = round(MAX_PAD / 3)
    THIRD_RAND_INT = random.randint(1, THIRD)
    DIFF_THIRD = THIRD - THIRD_RAND_INT

    RAND_INT = random.randint(1, MAX_PAD)
    DIFF_INT = MAX_PAD - RAND_INT  # DONT USE THIS, YOU'LL USE ALL THAT"S LEFT !
    DIFF_INT2 = round(DIFF_INT / 3)

    NL = "\n"
    #NEW_MSG2 = f"""
    #{x}{x}{' ' * int(MAX_PAD - 4)}{x}{x}
    #"""
    # NEW_MSG2 = ""
    # NEW_MSG2 += "\n".join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])
    #NEW_MSG2 += f"""
    #{x}{x}{' ' * int(MAX_PAD - 4)}{x}{x}
    #"""




    BOX9 = f"""
{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
{x}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""

    BOX10 = f"""
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
    BOX11 = f"""
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
    BOX13 = f"""
{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
{x}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
{NL.join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
{x}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
"""

    BOX18 = f"""
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
{NL.join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
"""

    LIST = [ BOX1, BOX2, BOX3, BOX4, BOX5, BOX6, BOX7, BOX8, BOX9, BOX10, BOX11, BOX12, BOX13, BOX14, BOX15, BOX16, BOX17, BOX18 ]
    MSG = random.choice(LIST)

    #MSG = BOX5
    #MSG = BOX18
    #MSG = PRINT_FMT_MSG(MSG)
    print(MSG)

    return(MSG)

def t(LOOPCOUNT):

    for i in range(1, LOOPCOUNT):
        x = RAND_CH()

        MSG = f"""

        {x}                                                        {x}
        {x} [ZZChitownMNO04] BEFORE: [Active ] ¿? AFTER: [Standby] {x}
        {x}                                                        {x}
        {x} [ZZChitownMNO05] BEFORE: [Standby] ?¿ AFTER: [Active ] {x}
        {x}                                                        {x}

        """
        x = RAND_CH()
        print(PRETTY_BOX(f"This is iteration {i}",9,1))
        MSG = PRETTY_BOX(MSG,9,1)
        print(PRETTY_BOX(MSG,9,1))
        # print(PRETTY_BOX(PRETTY_BOX(MSG)))
        # print(PRETTY_BOX(PRETTY_BOX(PRETTY_BOX(MSG))))
        print('just say when')
        x = input()
        #SNOOZE(10)


def PRETTY_BOX(MSG,COMPLEXITY,QUIET=None):

    def THE_THING(MSG):
        # beginning of line subs
        #MSG = re.sub(r"^\s+", "", MSG )  # strip all leading white
        #MSG = re.sub(r"^", "  ", MSG )
        #MSG = re.sub(r"^(\S)+", r"  \1", MSG)


        # end of line subs
        #MSG = re.sub(r"\s+$", "", MSG )  # strip all trailing white
        #MSG = re.sub(r"$", "  ", MSG)
        #MSG = re.sub(r"(\S)+$", r"\1  ", MSG)


        LIST = MSG.split("\n")

        LIST = [ re.sub(r"^\s+", "", i) for i in LIST ]
        LIST = [ re.sub(r"\s+$", "", i) for i in LIST ]
        LIST = [ re.sub(r"^\s+$", "", i) for i in LIST ]
        LIST = [ i for i in LIST if i ]

        BORDER_SPACE = random.randint(0, 9)

        OPT = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11 ]

        if BORDER_SPACE == OPT[0]:
            pass

        elif BORDER_SPACE == OPT[1]:

            LIST = [ re.sub(r"^", " ", i) for i in LIST ]
            LIST = [ re.sub(r"$", " ", i) for i in LIST ]

        elif BORDER_SPACE == OPT[2]:

            LIST = [ re.sub(r"^", "  ", i) for i in LIST ]
            LIST = [ re.sub(r"$", "  ", i) for i in LIST ]

        elif BORDER_SPACE == OPT[3]:

            LIST = [ re.sub(r"^", "    ", i) for i in LIST ]
            LIST = [ re.sub(r"$", "    ", i) for i in LIST ]

        elif BORDER_SPACE == OPT[4]:

            LIST = [ re.sub(r"^", " ", i) for i in LIST ]
            LIST = [ re.sub(r"$", "  ", i) for i in LIST ]

        elif BORDER_SPACE == OPT[5]:

            LIST = [ re.sub(r"^(\s+)", r" \1", i) for i in LIST ]
            LIST = [ re.sub(r"$", " ", i) for i in LIST ]

        elif BORDER_SPACE == OPT[6]:

            LIST = [ re.sub(r"^", "    ", i) for i in LIST ]
            LIST = [ re.sub(r"$", "", i) for i in LIST ]

        elif BORDER_SPACE == OPT[7]:

            LIST = [ re.sub(r"^", "", i) for i in LIST ]
            LIST = [ re.sub(r"$", "    ", i) for i in LIST ]

        elif BORDER_SPACE == OPT[8]:

            LIST = [ re.sub(r"^", "", i) for i in LIST ]
            LIST = [ re.sub(r"$", "   ", i) for i in LIST ]

        elif BORDER_SPACE == OPT[8]:

            LIST = [ re.sub(r"^", "", i) for i in LIST ]
            LIST = [ re.sub(r"$", "  ", i) for i in LIST ]

        elif BORDER_SPACE == OPT[7]:

            LIST = [ re.sub(r"^", "    ", i) for i in LIST ]
            LIST = [ re.sub(r"$", "", i) for i in LIST ]

        elif BORDER_SPACE == OPT[8]:

            LIST = [ re.sub(r"^", "    ", i) for i in LIST ]
            LIST = [ re.sub(r"$", " ", i) for i in LIST ]

        elif BORDER_SPACE == OPT[9]:

            LIST = [ re.sub(r"^", "     ", i) for i in LIST ]
            LIST = [ re.sub(r"$", "  ", i) for i in LIST ]


        VERT_SPACE = random.randint(0, 8)

        OPT = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]

        """

        if VERT_SPACE == OPT[0]:
            pass

        elif VERT_SPACE == OPT[1]:
            LIST = ['\n<11>'] + LIST[:] + ['\n<11>']

        elif VERT_SPACE == OPT[2]:

            LIST = ['\n<22>','\n<22>'] + LIST[:] + ['\n<22>','\n<22>']

        elif VERT_SPACE == OPT[3]:

            LIST = ['\n<23>','\n<23>','\n<23>'] + LIST[:] + ['\n<23>','\n<23>']

        elif VERT_SPACE == OPT[4]:

            LIST = ['\n<24>'] + LIST[:]

        elif VERT_SPACE == OPT[5]:

            LIST = ['\n<25>','\n<25>'] + LIST[:]

        elif VERT_SPACE == OPT[6]:

            LIST = ['\n<26>','\n<26>','\n<26>'] + LIST[:]

        elif VERT_SPACE == OPT[7]:

            LIST = ['\n<27>'] + LIST[:]

        elif VERT_SPACE == OPT[8]:

            LIST = LIST[:] + ['\n<28>']
        """


        # if it begins with more than one space, make it two
        #for LINE in LIST:
        #    LINE = re.sub(r"^\s+", "  ", LINE )
        #    LINE = re.sub(r"^(\S)+", r"  \1", LINE)
        #    LINE = re.sub(r"\s+$", "  ", LINE)
        #    LINE = re.sub(r"(\S)+$", r"\1  ", LINE)

        MAX_PAD = max([len(i) for i in LIST])
        #MAX_PAD += random.randint(0, 4)

        Z = RAND_CH()
        for i in range(0, random.randint(0, 4)):
            LIST.insert(0,Z)
            if random.randint(0, 99) % 2 == 0:
              LIST.append(Z)



        #MSG += "\n".join([f"|{line:{MAX_PAD}}|" for line in LIST])
        if len(LIST) > 0:
            #MSG += "\n".join([f"{line:{MAX_PAD}}" for line in LIST])
            for line in LIST:
                MSG += "\n".join(f"{line:{MAX_PAD}}")

        #breakpoint()


        x = RAND_CH()

        QUAD = round(MAX_PAD / 4)
        QUAD_RAND_INT = random.randint(1, QUAD)
        NEG_QUAD_SPACE = QUAD - QUAD_RAND_INT or 1
        #NEG_QUAD_SPACE = NEG_QUAD_SPACE * 6

        EIGHT = round(MAX_PAD / 8)
        EIGHT_RAND_INT = random.randint(1, EIGHT)
        DIFF_EIGHT = EIGHT - EIGHT_RAND_INT


        E1 = EIGHT_RAND_INT
        E2 = DIFF_EIGHT


        THIRD = round(MAX_PAD / 3)
        THIRD_RAND_INT = random.randint(1, THIRD)
        DIFF_THIRD = THIRD - THIRD_RAND_INT

        RAND_INT = random.randint(1, MAX_PAD)
        DIFF_INT = MAX_PAD - RAND_INT  # DONT USE THIS, YOU'LL USE ALL THAT"S LEFT !
        DIFF_INT2 = round(DIFF_INT / 3)

        NL = "\n"
        #NEW_MSG2 = f"""
        #{x}{x}{' ' * int(MAX_PAD - 4)}{x}{x}
        #"""
        # NEW_MSG2 = ""
        # NEW_MSG2 += "\n".join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])
        #NEW_MSG2 += f"""
        #{x}{x}{' ' * int(MAX_PAD - 4)}{x}{x}
        #"""


        # BOX1 = f"""(1){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX1 = f"""
{x *     3}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * 3}
"""
        # BOX1A = f"""(1a){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX1A = f"""
{x *     3}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * 3}
"""
        # BOX2 = f"""(2){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX2 = f"""
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * 3}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     3}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}
"""
        # BOX2A = f"""(2a){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX2A = f"""
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * 3}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     3}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}
"""

        # BOX3 = f"""(3){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX3 = f"""
{' '     * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}{x * RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     RAND_INT}{' ' * int(DIFF_INT2)}{x * int((DIFF_INT2))}{' ' * int(DIFF_INT2)}
"""

        # BOX4 = f"""(4){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX4 = f"""
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}
"""

        # BOX5 = f"""(5){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX5 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""


        # BOX6 = f"""(6){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX6 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
"""
        # BOX7 = f"""(7){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX7 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}
"""

        # BOX8 = f"""(8){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX8 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
"""
        # BOX9 = f"""(9){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX9 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""
        # BOX9A = f"""(9A){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX9A = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""

        # BOX10 = f"""(10){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX10 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 )}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 )}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        # BOX11 = f"""(11){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX11 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        # BOX12 = f"""(12){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX12 = f"""
{x *     THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x}{    ' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
"""
        # BOX12A = f"""(12a){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX12A = f"""
{x *     THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x}{    ' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
"""
        # BOX13 = f"""(13){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX13 = f"""
{x}{    ' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
"""
        # BOX13A = f"""(13a){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX13A = f"""
{x}{    ' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x * THIRD_RAND_INT}{' ' * int(DIFF_THIRD)}{x}
"""
        # BOX14 = f"""(14){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX14 = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""
        # BOX14A = f"""(14a){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX14A = f"""
{x *     int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x}{    ' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}{' ' * int(E2)}{x * int(E1)}
"""

        # BOX15 = f"""(15){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX15 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        # BOX15A = f"""(15a){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX15A = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        # BOX16 = f"""(16){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX16 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
{NL.    join([f"{x}{line:{int(MAX_PAD )}}{x}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}{x * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2 + 1)}{x * QUAD_RAND_INT}
"""
        # BOX17 = f"""(17){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX17 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
"""
        # BOX18 = f"""(18){MAX_PAD=} {QUAD=} {EIGHT=} {THIRD=} {x=}
        BOX18 = f"""
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
{NL.    join([f"{line:{int(MAX_PAD )}}" for line in LIST])}
{x *     QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{' ' * QUAD_RAND_INT}{' ' * QUAD_RAND_INT}{' ' * int(NEG_QUAD_SPACE * 2)}{x * QUAD_RAND_INT}
"""

        LIST = [ BOX1,BOX1A,    BOX2,BOX2A,    BOX3,  BOX4,  BOX5,  BOX6,    BOX8,  BOX9,
                 BOX10, BOX11, BOX12, BOX12A, BOX13, BOX13A,  BOX14, BOX14A,  BOX15,BOX15A,  BOX16,
                 BOX17, BOX18 ]

        #LIST = [ BOX1, BOX2, BOX3, BOX4, BOX5, BOX6, BOX7, BOX8, BOX9, BOX10, BOX11, BOX12, BOX13, BOX14, BOX15, BOX16, BOX17, BOX18 ]

        # LIST = [ BOX12 , BOX10 ]
        OUT = random.choice(LIST)
        return OUT

    LUCKY = random.randint(1, 7)

    if LUCKY == 1 or COMPLEXITY == 1:
        FIRST = THE_THING(MSG)

        if QUIET:
            return FIRST
        else:
            print(FIRST)
            return

    elif LUCKY == 2 or COMPLEXITY == 2:
        FIRST = THE_THING(MSG)
        TWO = THE_THING(FIRST)
        #F = 1
        if QUIET:
            return TWO
        else:
            print(TWO)
            return



    elif LUCKY == 3 or COMPLEXITY == 3:
        FIRST = THE_THING(MSG)
        TWO = THE_THING(FIRST)
        THREE = THE_THING(TWO)
        #F = 1
        if QUIET:
            return THREE
        else:
            print(THREE)
            return

    elif LUCKY == 4 or COMPLEXITY == 4:
        FIRST = THE_THING(MSG)
        TWO = THE_THING(FIRST)
        THREE = THE_THING(TWO)
        FOUR = THE_THING(THREE)
        #F = 1
        if QUIET:
            return FOUR
        else:
            print(FOUR)
            return

    elif LUCKY >= 5:
        MSG = THE_THING(MSG)
        MSG = THE_THING(MSG)
        MSG = THE_THING(MSG)
        MSG = THE_THING(MSG)

        #MSG = THE_THING(MSG)
        #F = 1
        if QUIET:
            return MSG
        else:
            print(MSG)
            return


        #MSG = BOX5
        #MSG = BOX9A
        #MSG = PRINT_FMT_MSG(MSG)
        # BOX2 = PRETTY_BOX(MSG)
        # BOX3 = PRETTY_BOX(BOX2)
        # MSG = PRETTY_BOX(BOX3)
    #if QUIET and F:
    #    F = 0
    #    return(PRETTY_BOX(OUT))
    #else:
    #    F = 0
    #    print(PRETTY_BOX(OUT))



def PPRINT(JSON_OBJ):
    pp = pprint.PrettyPrinter(indent=4, compact=True)
    pp.pprint(JSON_OBJ)


def PRETTY(PAD):

    x = RAND_CH()

    #PAT = f"{'♡' * int(PAD)}"
    PAT = x * PAD
    return PAT

# def RAND_CH(COLOR=None):
#
#     mylist = [
#             'Ω','∑','ф','Ш','ǒ','∆','∝','ǯ','λ',
#             'έ','√','♢','♣','♠','☼','ﬁ','©','¬',
#             '¢','æ','¿','¡','½','⑃','⑀','℗','≈',
#             '∀','∞','⊙','♫','¹','ý','ė','õ','ï',
#             'φ','Ϟ','ж','Д','δ','Љ','Ψ','š','Λ','Μ','ŧ',
#             'ש','Π','ẘ','ḿ','ق','†','₩','⁸','▢','∴','▣',
#             '▦','▧','▩','▭','□','␣','₽','☺','◐','◑','◊',
#             '▽','♪','ﬀ','☆']
#
#     CH = random.choice(mylist)
#
#     return str(CH)

def RAND_CH(COLOR=None):

    #COLOR = 1

    # HEADER = '\033[95m'
    # OKBLUE = '\033[94m'
    # OKCYAN = '\033[96m'
    # OKGREEN = '\033[92m'
    # WARNING = '\033[93m'
    # FAIL = '\033[91m'
    # ENDC = '\033[0m'
    # BOLD = '\033[1m'
    # UNDERLINE = '\033[4m'

    color = [
    '\033[95m',
    '\033[94m',
    '\033[96m',
    '\033[92m',
    '\033[93m',
    '\033[91m',
    '\033[0m',
    '\033[1m',
    '\033[4m',
    ]


    mylist = [
            'Ω','∑','ф','Ш','ǒ','∆','∝','ǯ','λ','ô','ŕ','÷',
            'έ','√','♢','♣','♠','☼',' ','ﬁ','©','¬','¬','ĳ',
            '¢','æ','¿','¡','½','⑃','⑀','℗','≈','«','»','³',
            '∀','∞','⊙',' ','♫','¹','ý','ė','õ','ï','ö','ř',
            'φ','Ϟ','ж','Д','δ','Љ','Ψ','š','Λ','Μ','ŧ','°',
            'ש','Π',' ','ẘ','ḿ','ق','†','₩','⁸','▢','∴','▣',
            '▦','▧','▩','▭','□','␣','₽',' ','◐','◑','◊','¬',
            '▽','♪','ﬀ','☆','°','©','¥','¯','¢','Ï','ć','ċ',
            '£','ƣ','Œ','œ','Φ','џ','Ḻ','ל','ζ','ς','ѫ','ج',
            'ד','ж','پ','љ','ƶ','я','x','Г','π','ΐ','ξ','â',
            '¶','ẘ','ẙ','⇒','≤','‴','•','₇','۰','Ζ','گ','Ħ',
            'ы','Л','ע','ח','ט','י','ґ','כ','ר','ą','ץ','ط',
            'آ','ї','ס','Ĺ','ϛ','ή','ך','ם','ג','Γ','γ','φ',
            'ⅷ','Ⅰ','Á','Ⅰ','Ⅱ','Ⅲ','Ⅳ','Ⅴ','Ⅵ','Ⅶ','Ⅷ','Ⅸ',
            '◑','۰','۱','۲','۳','۴','۵','۶','۷','۸','۹','б',
            '※','ⁿ','ŀ','ĵ','İ','т','⅓','⅕','⅔','⅖','∾','∧',
            '∨','┌','┘','∃','Ǯ','п','‖',
            ]

    CH = random.choice(mylist)
    color = random.choice(color)

    if COLOR:
      CH = color + CH
      return str(CH)
    else:
      pass


    return str(CH)


def GEN_ERR_MSG(HOSTNAME, EXCEPT):

    TYPE, VALUE, TB = sys.exc_info()

    FORMAT_EXC = traceback.format_exc()
    FORMAT_TB = traceback.format_tb(TB)
    FORMAT_ST = traceback.format_stack()

    LINE = f"☆☆ {EXCEPT} OCCURRED ON: {HOSTNAME} ☆☆\n"
    PAD = len(LINE) - 1
    LINE2 = f"☆☆{' ' * int(PAD - 4)}☆☆\n"
    LINE3 = f"{'☆' * int(PAD)}\n"

    MSG = "\n"
    MSG += LINE3
    MSG += LINE2
    MSG += LINE
    MSG += LINE2
    MSG += LINE3

    FORMAT_EXC = re.sub(r"\s+"," ", FORMAT_EXC)
    FORMAT_EXC = re.sub(r"Traceback","\n  Traceback", FORMAT_EXC)
    FORMAT_EXC = re.sub(r"File \"","\n\n    File \"", FORMAT_EXC)
    FORMAT_EXC = re.sub(r"\s(\S+[^)]:)",r"\n\n\1", FORMAT_EXC)

    LIST2 = str(FORMAT_EXC).split('\n')
    PAD = max([len(i) for i in LIST2])

    SEP = PRETTY(PAD)
    LIST2.append(SEP)
    LIST2.insert(0,SEP)


    # FORMAT_TB = re.sub(r"\s+"," ", FORMAT_TB)
    # FORMAT_TB = re.sub(r"Traceback","\n  Traceback", FORMAT_TB)
    # FORMAT_TB = re.sub(r"File","\n\n    File", FORMAT_TB)
    # FORMAT_TB = re.sub(r"\s(\S+Error)",r"\n\n\1", FORMAT_TB)

    # TRACEBACK = ""
    # for item in FORMAT_TB:
    #     TRACEBACK += str(item) + " "

    # TRACEBACK = re.sub(r"\s+"," ", TRACEBACK)
    # TRACEBACK = re.sub(r"Traceback","\n  Traceback", TRACEBACK)
    # TRACEBACK = re.sub(r"File","\n\n    File", TRACEBACK)
    # TRACEBACK = re.sub(r"\s(\S+[^)]:)",r"\n\n\1", TRACEBACK)

    # LIST3 = TRACEBACK.split('\n')
    # PAD = max([len(i) for i in LIST3])

    # SEP = PRETTY(PAD)
    # LIST3.append(SEP)


    TRACEBACK = ""
    for item in FORMAT_ST:
        TRACEBACK += str(item) + " "

    TRACEBACK = re.sub(r"\s+"," ", TRACEBACK)
    TRACEBACK = re.sub(r"Traceback","\n  Traceback", TRACEBACK)
    TRACEBACK = re.sub(r"File \"","\n\n    File \"", TRACEBACK)
    TRACEBACK = re.sub(r"\s(\S+Error)",r"\n\n\1", TRACEBACK)

    LIST4 = TRACEBACK.split('\n')
    PAD = max([len(i) for i in LIST4])

    #SEP = f"{'¤' * int(PAD)}"
    SEP = PRETTY(PAD)
    LIST4.append(SEP)


    MSG += "\n".join(LIST2)
    # MSG += "\n".join(LIST3)
    MSG += "\n".join(LIST4)

    return MSG

def PRETTY_GEN_ERR_MSG(HOSTNAME, EXCEPT):


    TYPE, VALUE, TB = sys.exc_info()

    FORMAT_EXC = traceback.format_exc()
    FORMAT_TB = traceback.format_tb(TB)
    FORMAT_ST = traceback.format_stack()

    x = RAND_CH()

    LINE = f"{x}{x} {EXCEPT} OCCURRED ON: {HOSTNAME} {x}{x}"
    PAD = len(LINE)
    LINE2 = f"{x}{x}{' ' * int(PAD - 4)}{x}{x}"
    LINE3 = x * PAD

    TOP_L = []
    TOP_L.append(LINE3)
    TOP_L.append(LINE2)
    TOP_L.append(LINE)
    TOP_L.append(LINE2)
    TOP_L.append(LINE3)


    TRACEBACK = ""
    for item in FORMAT_ST:
        TRACEBACK += str(item) + " "

    TRACEBACK = re.sub(r"\s+"," ", TRACEBACK)
    TRACEBACK = re.sub(r"Traceback","\n  Traceback", TRACEBACK)
    TRACEBACK = re.sub(r"File \"","\n\n    File \"", TRACEBACK)
    TRACEBACK = re.sub(r"\s(\S+[^)]:)",r"\n\n \1", TRACEBACK)

    LIST4 = TRACEBACK.split('\n')
    PAD = max([len(i) for i in LIST4])

    #BAR = f"{'¤' * int(PAD)}"
    BAR = PRETTY(PAD)
    LIST4 = LIST4[1:]
    LIST4.insert(0,BAR)
    LIST4.insert(0,"")
    LIST4.insert(0,"")

    FORMAT_EXC = re.sub(r"\s+"," ", FORMAT_EXC)
    FORMAT_EXC = re.sub(r"Traceback","\n  Traceback", FORMAT_EXC)
    FORMAT_EXC = re.sub(r"File \"","\n\n    File \"", FORMAT_EXC)
    FORMAT_EXC = re.sub(r"\s(\S+[^)]:)",r"\n\n \1", FORMAT_EXC)

    LIST2 = str(FORMAT_EXC).split('\n')
    #PAD = max([len(i) for i in LIST2])

    #BAR = PRETTY(PAD)
    LIST2.append("")
    LIST2.append(BAR)
    #LIST2.insert(0,BAR)

    TOP_L.append(LIST4)
    TOP_L.append(LIST2)

    PRETTY_OUT = pprint.pformat(TOP_L, indent=4, depth=4, width=140)


    #MSG += "\n".join(LIST2)
    ## MSG += "\n".join(LIST3)
    #MSG += "\n".join(LIST4)

    return PRETTY_OUT
    #return MSG

def HANDLE_IT(HOSTNAME, EXCEPT):

    MSG = PRETTY_GEN_ERR_MSG(HOSTNAME,EXCEPT)

    if os.path.exists('./logs/') and os.path.isdir('./logs/'):
        pass
    else:
        os.mkdir('./logs/')


    OUTFILE = str("./logs/" + HOSTNAME + "_" + EXCEPT + ".error")

    OUTFILE_OBJ_1 = open(OUTFILE, "w")
    OUTFILE_OBJ_1.write(MSG)
    OUTFILE_OBJ_1.close()

    print(MSG)


def HANDLE_IT_LOG(HOSTNAME, EXCEPT, LOGNAME):

    MSG = PRETTY_GEN_ERR_MSG(HOSTNAME,EXCEPT)


    stringAppendToFile(MSG, "main", LOGNAME)



def logStamp():

    DATESTAMP = os.popen("date \"+%Y%m%d_%H%M%S\"").read().rstrip()

    DIRNAME = f"logs_{DATESTAMP}"

    # LINES = os.popen("pass " + PASS_NAME).read().rstrip()
    # LINES = LINES.split()

    if os.path.exists('./logs/') and os.path.isdir('./logs/'):
        #pass
        CMD = f"mv ./logs/ ./logs_{DATESTAMP}"
        LINES = os.popen(CMD).read().rstrip()

        RESULT = int(os.popen("echo $?").read().rstrip())
        print(f"\nThe value of $?: <{RESULT}>\n")

        #breakpoint()

        if RESULT == 0:
            return DIRNAME
        else:
            print(f"ERROR encountered during CMD: {CMD}\nexiting ...\n")
            sys.exit()

    else:
        #os.mkdir('./logs/')
        pass

def genDiffs(SITE, BEFORE_DIR, AFTER_DIR):

    #DATESTAMP = os.popen("date \"+%Y%m%d_%H%M\"").read().rstrip()

    #DIRNAME = f"logs_{DATESTAMP}"

    # LINES = os.popen("pass " + PASS_NAME).read().rstrip()
    # LINES = LINES.split()

    if os.path.exists(BEFORE_DIR) and os.path.isdir(BEFORE_DIR) and os.path.exists(AFTER_DIR) and os.path.isdir(AFTER_DIR):
        #pass
        CMD = f"diff -C9 {BEFORE_DIR}/ {AFTER_DIR}/ > deploy_diff_{SITE}_{AFTER_DIR}.txt"

        LINES = os.popen(CMD).read().rstrip()

        RESULT = int(os.popen("echo $?").read().rstrip())
        print(f"\nThe value of $?: <{RESULT}>\n")

        #breakpoint()

        if RESULT == 0:
            print(f"SUCCESS, generated diff file: deploy_diff_{SITE}_{AFTER_DIR}.txt\n\n")
        else:
            print(f"ERROR encountered during CMD: {CMD}\nexiting ...\n")
            sys.exit()

    else:
        #os.mkdir('./logs/')
        pass

def bytesOutputToFile(OUTPUT, HOSTNAME, EXT):

    if os.path.exists('./logs/') and os.path.isdir('./logs/'):
        pass
    else:
        os.mkdir('./logs/')

    OUTFILE = str("./logs/" + HOSTNAME + "_" + EXT + ".txt")

    OUTFILE_OBJ_1 = open(OUTFILE, "wb")

    OUTFILE_OBJ_1.write(OUTPUT)


def objectOutputToFile(PY_OBJ, METHOD):
    """Takes an arbitrary Python object and outputs as converted json to file using jsonOutputToFile()"""

    if type(PY_OBJ) == str:

        PY_OBJ = json.dumps(PY_OBJ)
        jsonOutputToFile(PY_OBJ, f"str_{METHOD}")

    elif type(PY_OBJ) == dict:

        jsonOutputToFile(PY_OBJ, f"dict_{METHOD}")

    elif type(PY_OBJ) == list:

        jsonOutputToFile(PY_OBJ, f"list_{METHOD}")

def printJSON(NATIVE_OBJ):

    JSON = json.dumps(NATIVE_OBJ, indent=4)

    PRINT_FMT_MSG(JSON)



def jsonOutputToFile(OUTPUT, HOSTNAME):
    """Takes a json object and outputs to file"""

    freshDir("./logs/" )

    OUTFILE = str("./logs/" + HOSTNAME + ".json")

    f = open(OUTFILE, "w")

    #OUTPUT = json.load(OUTPUT)

    # OUTPUT must be json.load'd already ( aka PARSED )
    # json.dump(OUTPUT, f, indent=4, default=str)

    # trying to get pretty json output
    # json.dumps(OUTPUT, f, indent=4, default=str)

    # debug stuff below!!
    #print("The type of OUTPUT is: " + str(type(OUTPUT)) )
    # json.dump(OUTPUT, f, indent=4, default=str)
    f.write(OUTPUT)

    #json.dumps(f, default=str)
    #json.dumps(OUTPUT, default=str)

    f.close()

def stringOutputToFile_bakMN(OUTPUT, HOSTNAME, EXT):
    """Takes a string object and outputs to file"""

    freshDir("./logs/" )

    OUTFILE = str("./logs/" + HOSTNAME + "_" + EXT + ".txt")

    f = open(OUTFILE, "w")

    OUTPUT = str(OUTPUT)

    linesAsList = OUTPUT.split("\n")

    for LINE in linesAsList:
        LINE = LINE.rstrip()
        f.write(LINE + "\n")

    f.close()

def stringOutputToFile(*ARGS):
    """Takes a string object and outputs to file"""
    MODE = 'w'
    stringToFile(MODE, *ARGS)

def stringAppendToFile(*ARGS):
    MODE = 'a'
    OUTFILE = stringToFile(MODE, *ARGS)
    return OUTFILE


def stringToFile(MODE, *ARGS):
    """Takes a string object and outputs to file"""

    # X is either one of 'w' or 'a' for write or append

    # args: OUTPUT, HOSTNAME, EXT, SUBDIR=None
    #breakpoint()
    OUTPUT = ARGS[0]
    HOSTNAME = ARGS[1]
    EXT = ARGS[2]

    if len(ARGS) == 3:

        freshDir("./logs/" )

        OUTFILE = str("./logs/" + HOSTNAME + "_" + EXT + ".txt")

        f = open(OUTFILE, MODE)

        OUTPUT = str(OUTPUT)

        linesAsList = OUTPUT.split("\n")

        for LINE in linesAsList:
            LINE = LINE.rstrip()
            f.write(LINE + "\n")

        f.close()

        return OUTFILE

    elif len(ARGS) == 4:

        SUBDIR = ARGS[3]

        freshDir("./logs/" )

        LOGS = "./logs/" + SUBDIR

        freshDir(LOGS)

        LOGS = "./logs/DEBUG/"

        freshDir(LOGS)


        OUTFILE = str("./logs/" + SUBDIR + "/" + HOSTNAME + "_" + EXT + ".txt" )

        OUTFILE_OBJ_1 = open(OUTFILE , MODE)

        # OUTFILE_OBJ_1.write(OUTPUT)

        if isinstance(OUTPUT,str):
            OUTPUT = str.encode(OUTPUT)
            OUTPUT = OUTPUT.decode('utf-8', 'replace')
        else:
            OUTPUT = OUTPUT.decode('utf-8', 'replace')

        linesAsList = OUTPUT.split( '\n' )

        """
        for line in linesAsList:
            LINE = line + "\n"
            OUTFILE_OBJ_1.write(LINE)
        """
        for LINE in linesAsList:
            LINE = LINE.rstrip()
            OUTFILE_OBJ_1.write(LINE + "\n")

        OUTFILE_OBJ_1.close()

        #OUTFILE_OBJ_1.write(OUTPUT)


def stringAppendToFile_bakMN(OUTPUT, HOSTNAME, EXT, SUBDIR=None):
    """Takes a string object and outputs to file"""

    freshDir("./logs/" )

    OUTFILE = str("./logs/" + HOSTNAME + "_" + EXT + ".txt")

    f = open(OUTFILE, "a")

    OUTPUT = str(OUTPUT)

    linesAsList = OUTPUT.split("\n")

    for LINE in linesAsList:
        LINE = LINE.rstrip()
        f.write(LINE + "\n")

    f.close()



def breakUpJson(PY_OBJ, EXT, xpose=None):
    """Break up arbitrary nested json objects into smaller data frames and print to screen using dfDisplay()"""
    # breakpoint()

    NEW_OBJ = {}

    for count1, elem in enumerate(PY_OBJ):

        if type(elem) != dict and type(elem) != list:

            # print(
            #         f"\n[ NOT DICT OR LIST ]>> ELEM: << {elem} >> \nLENGTH: << {len(elem)} >> \nTYPE: << {type(elem)} >>\n"
            # )

            OBJ = PY_OBJ[elem]

        elif type(elem) == list:

            if type(PY_OBJ) == dict:

                # NEW_OBJ = copy.deepcopy(TEST)
                NEW_OBJ = copy.deepcopy(PY_OBJ[elem])

            elif type(PY_OBJ) == list:

                NEW_OBJ = copy.deepcopy(PY_OBJ[count1])

            for counter, x in enumerate(NEW_OBJ):
                # print(f"\nCOUNTER: {counter}\nX: {x}\nTYPE: {type(x)}\n\n\tVALUE: {PY_OBJ[x]}\n\tINSIDE TYPE: {type(PY_OBJ[x])}")

                try:

                    if type(NEW_OBJ[x]) == list and len(NEW_OBJ[x]) > 0:

                        print(f"\n=> {x}:")
                        NEW_OBJ_2 = copy.deepcopy(NEW_OBJ[x])
                        dfDisplay(NEW_OBJ_2, EXT + "_" + x, xpose)

                        NEW_OBJ[x] = None

                    elif type(NEW_OBJ[x]) == list and len(NEW_OBJ[x]) == 0:

                        NEW_OBJ[x] = None

                    elif type(NEW_OBJ[x]) == dict and len(NEW_OBJ[x]) > 0:

                        print(f"\n=> {x}:")
                        NEW_OBJ_2 = copy.deepcopy(NEW_OBJ[x])
                        dfDisplay(NEW_OBJ_2, EXT + "_" + x, xpose)

                        NEW_OBJ[x] = None

                    elif type(NEW_OBJ[x]) == dict and len(NEW_OBJ[x]) == 0:

                        NEW_OBJ[x] = None

                except KeyError:

                    if type(NEW_OBJ[counter]) == list and len(NEW_OBJ[counter]) > 0:

                        print(f"\n=> {counter}:")
                        NEW_OBJ_2 = copy.deepcopy(NEW_OBJ[counter])
                        dfDisplay(NEW_OBJ_2, EXT + "_" + counter, xpose)

                        NEW_OBJ[counter] = None

                    elif type(NEW_OBJ[counter]) == list and len(NEW_OBJ[counter]) == 0:

                        NEW_OBJ[counter] = None

                    elif type(NEW_OBJ[counter]) == dict and len(NEW_OBJ[counter]) > 0:

                        print(f"\n=> {counter}:")
                        NEW_OBJ_2 = copy.deepcopy(NEW_OBJ[counter])
                        dfDisplay(NEW_OBJ_2, EXT + "_" + counter, xpose)

                        NEW_OBJ[counter] = None

                    elif type(NEW_OBJ[counter]) == dict and len(NEW_OBJ[counter]) == 0:

                        NEW_OBJ[counter] = None

            # PY_OBJ = copy.deepcopy(PY_OBJ[count1])

            # print(
            #         f"\n[ LIST ]>> ELEM: << {elem} >> \nLENGTH: << {len(elem)} >> \nTYPE: << {type(elem)} >>\n"
            # )

        elif type(elem) == dict:

            # print(
            #         f"\n[ DICT ]>> ELEM: << {elem} >> \nLENGTH: << {len(elem)} >> \nTYPE: << {type(elem)} >>\n"
            # )

            # for k,v in elem.items():
            # print(
            #         f"\n(inside dict) KEY: {k}\nVALUE: {v}\nTYPE: {type(v)}\nLEN: {len(v)}\n"
            # )

            if type(PY_OBJ) == dict:

                # TEST = frozendict(PY_OBJ[elem])

                # NEW_OBJ = copy.deepcopy(TEST)
                NEW_OBJ = copy.deepcopy(PY_OBJ[elem])

            elif type(PY_OBJ) == list:

                NEW_OBJ = copy.deepcopy(PY_OBJ[count1])

                # PY_OBJ = copy.deepcopy(PY_OBJ)

            for counter, x in enumerate(NEW_OBJ):
                # print(f"\nCOUNTER: {counter}\nX: {x}\nTYPE: {type(x)}\n\n\tVALUE: {PY_OBJ[x]}\n\tINSIDE TYPE: {type(PY_OBJ[x])}")

                try:

                    if type(NEW_OBJ[x]) == list and len(NEW_OBJ[x]) > 0:

                        print(f"\n=> {x}:")
                        NEW_OBJ_2 = copy.deepcopy(NEW_OBJ[x])
                        dfDisplay(NEW_OBJ_2, EXT + "_" + x, xpose)

                        NEW_OBJ[x] = None

                    elif type(NEW_OBJ[x]) == list and len(NEW_OBJ[x]) == 0:

                        NEW_OBJ[x] = None

                    elif type(NEW_OBJ[x]) == dict and len(NEW_OBJ[x]) > 0:

                        print(f"\n=> {x}:")
                        NEW_OBJ_2 = copy.deepcopy(NEW_OBJ[x])
                        dfDisplay(NEW_OBJ_2, EXT + "_" + x, xpose)

                        NEW_OBJ[x] = None

                    elif type(NEW_OBJ[x]) == dict and len(NEW_OBJ[x]) == 0:

                        NEW_OBJ[x] = None

                except KeyError:

                    if type(NEW_OBJ[counter]) == list and len(NEW_OBJ[counter]) > 0:

                        print(f"\n=> {counter}:")
                        NEW_OBJ_2 = copy.deepcopy(NEW_OBJ[counter])
                        dfDisplay(NEW_OBJ_2, EXT + "_" + counter, xpose)

                        NEW_OBJ[counter] = None

                    elif type(NEW_OBJ[counter]) == list and len(NEW_OBJ[counter]) == 0:

                        NEW_OBJ[counter] = None

                    elif type(NEW_OBJ[counter]) == dict and len(NEW_OBJ[counter]) > 0:

                        print(f"\n=> {counter}:")
                        NEW_OBJ_2 = copy.deepcopy(NEW_OBJ[counter])
                        dfDisplay(NEW_OBJ_2, EXT + "_" + counter, xpose)

                        NEW_OBJ[counter] = None

                    elif type(NEW_OBJ[counter]) == dict and len(NEW_OBJ[counter]) == 0:

                        NEW_OBJ[counter] = None

            # Display whatever is remaining ( non lists )
            # when we found nested objects previously, we deepcopy'd them to new ones and set them to None in the master object
            REMAINDER_DICT = {}

            for x in NEW_OBJ:
                # print(f"\nCOUNTER: {counter}\nX: {x}\nTYPE: {type(x)}\n\n\tVALUE: {PY_OBJ[x]}\n\tINSIDE TYPE: {type(PY_OBJ[x])}")

                if NEW_OBJ[x] is not None:
                    # REMAINDER_DICT.setdefault(x, list(PY_OBJ[x]))
                    REMAINDER_DICT[x] = []
                    REMAINDER_DICT[x].append(NEW_OBJ[x])

            dfDisplay(REMAINDER_DICT, EXT, xpose)


def dfDisplay(PY_OBJ, METHOD, xpose=None, brief=None, filt_param=None):
    """Take arbitrary Python object and convert to Pandas DataFrame, wipe secret column text, and write that DataFrame to disk and print it to screen"""
    """
    print(
        f"\ndfDisplay func was called with METHOD: {METHOD} and filt_param: {filt_param} , ( from inside MN_API module )\n"
    )
    """
    # breakpoint()

    OUTFILE = str("./logs/dfDisplay_MN_API_" + METHOD + ".txt")
    CSVFILE = str("./logs/dfDisplay_MN_API_" + METHOD + ".csv")

    f = open(OUTFILE, "w")

    INFO = ""

    # print(f"\nPY_OBJ has type: {type(PY_OBJ)} and length: {len(PY_OBJ)}\n")
    #breakpoint()

    if type(PY_OBJ) is list and len(PY_OBJ) > 0:
        #df = ""
        for counter,item in enumerate(PY_OBJ):
            #breakpoint()
            # df = pd.json_normalize(i, max_level=2 )
            # for i in df.columns: df=df.explode(i)

            try:

                # now check the type of the element in that list
                if type(item) is dict:

                    #breakpoint()
                    # dfDisplay func was called with METHOD: subs and filt_param: None , ( from inside MN_API module )

                    # PY_OBJ has type: <class 'list'> and length: 972

                    # cannot concatenate object of type '<class 'dict'>'; only Series and DataFrame objs are valid

                    PY_OBJ[counter] = pd.json_normalize(item, max_level=2 )

                    #df = pd.json_normalize(i, max_level=2 )

                    #df = pd.concat(pd.json_normalize(i, max_level=2 ))


                    #df = pd.concat([i for i in PY_OBJ])

                    #df = pd.concat([pd.json_normalize(i) for i in PY_OBJ])
                    #df = pd.concat([pd.json_normalize(i) for i in PY_OBJ])

            except Exception as e:
                print(e)


        df = pd.concat([item for item in PY_OBJ])

        #breakpoint()
        # INFO = df.info()

        if xpose:
            df = df.transpose()
        else:
            pass

        try:
            # print(f"Looking for: {filt_param} inside df ..\n")

            if df[filt_param] is not None:
                print(f"\nFound! filt_param: {filt_param} inside df ..\n")
                RESULT_LIST = list(df[filt_param])
                print(f"\nReturning RESULT_LIST with {len(RESULT_LIST)} items!\n")

                # write filtered output to file first
                f.write("\n\n")
                f.write(str(df))
                f.write("\n\n")
                f.write(str(INFO))
                f.write("\n\n")

                # return back to calling func
                return RESULT_LIST
        except:
            # print("\nERROR: df\[filt_param\] was None\n")
            # sys.exit()
            """
            print(
                f"\nfilt_param: {filt_param} , might be ok! \nwarning: df\[filt_param\] was None\n"
            )
            """

            f.write("\n\n")
            f.write(str(df))
            f.write("\n\n")
            # f.write(str(INFO))
            # f.write("\n\n")

            #MSG = str(df)

            CSV_STR = df.to_csv(sep=',', index=False)
            CSV_LIST = CSV_STR.split('\n')
            CSV_OBJ = csv.reader(CSV_LIST)

            OUT_L = []

            ROW_OBJ = {}

            for i in CSV_OBJ:
                OUT_L.append(i)

            #print(tabulate.tabulate(OUT_L))
            MSG = tabulate.tabulate(OUT_L)

            # print(f"\n{df}\n")
            # breakpoint()
            MSG = PRETTY_BOX(MSG,2,1)
            print(MSG)


            # DF = pd.DataFrame(CSV_LIST)
            # JSON_STR = test.to_json(DF)
            # JSON_OBJ = json.loads(JSON_STR)
            # JSON_STR = json.dumps(JSON_OBJ, indent=2)



            # breakpoint()

            # # df = pd.concat([item for item in PY_OBJ])

            # # MAX_PAD = max([len(i) for i in LIST])



            # #for item in CSV_OBJ:

            #
            # #PPRINT(CSV_OBJ)



            # breakpoint()
            #MSG = pd.read_csv(CSV_STR)



            # print(f"\n{df}\n{INFO}\n")

            #print(f"\nWriting df1 to csv: {CSVFILE}\n\n")
            #df.to_csv(CSVFILE)

    elif type(PY_OBJ) is dict and len(PY_OBJ) > 0:

        try:

            #PY_OBJ = flatten(PY_OBJ, ".")

            #df = pd.DataFrame(data=PY_OBJ)
            #df = pd.json_normalize(PY_OBJ)
            df = pd.json_normalize(PY_OBJ, max_level=2 )

            # from pandas.io.json import json_normalize
            # import json
            # with open('data.json', 'r') as f: # 'data.json' is the name of the file
            #   data = f.readlines()
            #   pd.concat([json_normalize(json.loads(j)) for j in data])...

            # for i in df.columns: df=df.explode(i)

            # PY_DICT_OBJ = df.to_dict()

            # df = pd.json_normalize(PY_DICT_OBJ, "functions", ["functions"])

            # for i in df.columns: df=df.explode(i)


            #    (Pdb) p(df.columns)
            #    Index(['triggerid', 'expression', 'description', 'url', 'status', 'value',
            #           'priority', 'lastchange', 'comments', 'error', 'templateid', 'type',
            #           'state', 'flags', 'recovery_mode', 'recovery_expression',
            #           'correlation_mode', 'correlation_tag', 'manual_close', 'opdata',
            #           'functions'],
            #          dtype='object')
            #    (Pdb) for i in df.columns:
            #    *** SyntaxError: unexpected EOF while parsing
            #    (Pdb) for i in df.columns: df=df.explode(i)

            # for i in df.columns: df=df.explode(i)
            # breakpoint()

            # df = pd.json_normalize(df)

            # df2 = pd.json_normalize(df["functions"])
            # breakpoint()
            #breakpoint()
            # see if we can expand the groups column
            # df = df.groups.apply(pd.Series)
            # breakpoint()
            # SHAPE = df.shape
            # DTYPES = df.dtypes
            # INFO = df.info()
            #INFO2 = df2.info()

            # SHAPE = df_new.shape
            # DTYPES = df_new.dtypes

            # this is the magic sauce sometimes, maybe should add a switch for this

            if xpose:
                df = df.transpose()
            else:
                pass

            try:

                if df["secret"] is not None:

                    # scrub the psk from the output / log files
                    df["secret"] = "xxx"

            except KeyError:
                pass


            try:
                # print(f"Looking for: {filt_param} inside df ..\n")

                if df[filt_param] is not None:
                    print(f"\nFound! filt_param: {filt_param} inside df ..\n")
                    RESULT_LIST = list(df[filt_param])
                    print(f"\nReturning RESULT_LIST with {len(RESULT_LIST)} items!\n")

                    # write filtered output to file first
                    f.write("\n\n")
                    f.write(str(df))
                    f.write("\n\n")
                    f.write(str(INFO))
                    f.write("\n\n")

                    # return back to calling func
                    return RESULT_LIST
            except:
                # print("\nERROR: df\[filt_param\] was None\n")
                # sys.exit()
                """
                print(
                    f"\nfilt_param: {filt_param} , might be ok! \nwarning: df\[filt_param\] was None\n"
                )
                """

                f.write("\n\n")
                f.write(str(df))
                f.write("\n\n")
                f.write(str(INFO))
                f.write("\n\n")

                print(f"\n{df}\n{INFO}\n")

                print(f"\nWriting df1 to csv: {CSVFILE}\n\n")
                df.to_csv(CSVFILE)

        except ValueError as e:
            print(f"\nCouldn't create DataFrame from response, sorry, I tried.. \n")

