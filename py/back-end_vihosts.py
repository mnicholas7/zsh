#!/usr/bin/python3

# import pprint

import os
import re
from tabletext import to_text


def main():
    
    # first thing is to set up temp output file handle!
    DATESTAMP = os.popen('date "+%Y%m%d_%H%M"').read().rstrip()

    USER = os.popen('whoami').read().rstrip()

    TMP_OUTPUT_FILE = str( f"/home/{USER}/hosts/hosts_{DATESTAMP}" )

    TMP_OUTPUT_FILE_OBJ_1 = open(TMP_OUTPUT_FILE, "w")

    # Now read in MSFT hosts file which was just edited manually in vim ( from .sh )
    # based on the read in logic that will determine the output written to the tmp file, 
    # which will ultimately be mv'd to /etc/hosts!

    MSFT_HOSTS_IN = open("/mnt/c/Windows/System32/drivers/etc/hosts", "r")

    for line in MSFT_HOSTS_IN:

        line = line.rstrip()

        if re.match("^[#\s]+$", line):

            # print()
            # TMP_OUTPUT_FILE_OBJ_1.write('\n')
            pass

        elif re.match("^(\s)+$", line):

            pass

        elif re.match("$", line):

            pass

        elif line.startswith("#"):

            line = re.sub("\s+", " ", line)
            line = re.sub("^[#\s]+", "############ ", line)
            print("\n" + line)
            TMP_OUTPUT_FILE_OBJ_1.write("\n" + line + "\n")

        elif line.find("#"):

            line = line.split(sep="#", maxsplit=1)

            if len(line) > 1:

                line[1] = re.sub("\s+", " ", line[1])

                # print(line[0])
                left = line[0]

                fields = left.split()
                # print(repr(fields))

                for field in fields:

                    print("{0:25} ".format(field), end="")
                    TMP_OUTPUT_FILE_OBJ_1.write("{0:25} ".format(field))

                print("#" + line[1])
                TMP_OUTPUT_FILE_OBJ_1.write("#" + line[1] + "\n")
                # print()

                # print("YES: " + line[0] + "#" + line[1])

            else:

                together = " ".join(line)
                fields = together.split()

                for field in fields:

                    print("{0:25} ".format(field), end="")
                    TMP_OUTPUT_FILE_OBJ_1.write("{0:25} ".format(field))

                print()
                TMP_OUTPUT_FILE_OBJ_1.write("\n")

        else:

            # line = str(line)
            fields = line.split()

            for field in fields:

                print("{0:25} ".format(field), end="")
                TMP_OUTPUT_FILE_OBJ_1.write("{0:25} ".format(field))

            print()
            TMP_OUTPUT_FILE_OBJ_1.write("\n")

            # print("NO:  " + line[0])

    MSFT_HOSTS_IN.close()
    TMP_OUTPUT_FILE_OBJ_1.close()

    # Verify contents and size before copy

    BEFORE = os.popen("ls -l /etc/hosts").read()
    BEFORE = str.strip(str(BEFORE))

    BEFORE_MD5 = os.popen("md5sum /etc/hosts").read()
    BEFORE_WC = os.popen("wc /etc/hosts").read()

    BEFORE_MD5 = str.strip(str(BEFORE_MD5))
    BEFORE_WC = str.strip(str(BEFORE_WC))

    # Verify contents and size of TMP file before copy
    AFTER = os.popen("ls -l " + TMP_OUTPUT_FILE).read()
    AFTER = str.strip(str(AFTER))

    AFTER_MD5 = os.popen("md5sum " + TMP_OUTPUT_FILE).read()
    AFTER_WC = os.popen("wc " + TMP_OUTPUT_FILE).read()

    AFTER_MD5 = str.strip(str(AFTER_MD5))
    AFTER_WC = str.strip(str(AFTER_WC))

    A = [
        ["State", "Command", "Output"],
        ["BEFORE: ", "ls", BEFORE],
        ["AFTER: ", "ls", AFTER],
        ["", "", ""],
        ["BEFORE: ", "md5", BEFORE_MD5],
        ["AFTER: ", "md5", AFTER_MD5],
        ["", "", ""],
        ["BEFORE: ", "wc", BEFORE_WC],
        ["AFTER: ", "wc", AFTER_WC],
    ]

    print()
    print(to_text(A))
    print()

    DIFF = os.popen("diff -C3 /etc/hosts " + TMP_OUTPUT_FILE ).read()
    print()
    print(str(DIFF))
    print()

    # perform the cp!
    RESULT = os.system("sudo cp " + TMP_OUTPUT_FILE + " /etc/hosts")

    print()

    if RESULT == 0:

        print("     > sudo cp SUCCEEDED !")
        print()

        AFTER_MD52 = os.popen("md5sum /etc/hosts").read()
        print("     > " + str(AFTER_MD52))

    else:

        print("     > sudo cp FAILED !")
        print()

        AFTER_MD52 = os.popen("md5sum /etc/hosts").read()
        print("     > " + str(AFTER_MD52))


if __name__ == "__main__":
    main()
