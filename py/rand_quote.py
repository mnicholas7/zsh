#!/usr/bin/python3

from string import *
import random
import inspect

class r:
    """
    __all__ = ['ascii_letters', 'ascii_lowercase', 'ascii_uppercase', 'cap...
    ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    hexdigits = '0123456789abcdefABCDEF'
    octdigits = '01234567'
    printable = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU...
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    whitespace = ' \t\n\r\x0b\x0c'
    """
    def gen1(LEN):
        return(''.join(random.choices(ascii_lowercase + digits, k=LEN)))

    def gen2(LEN):
        return(''.join(random.choices(ascii_lowercase + digits + '_', k=LEN)))

    def gen3(LEN):
        return(''.join(random.choices(ascii_lowercase + ascii_uppercase + '_$', k=LEN)))

    def gen4(LEN):
        return( ''.join(random.choices(ascii_lowercase + ascii_uppercase + digits + '_$', k=LEN)))

    def s3(LEN):
        SEED = ''.join(random.choices(ascii_lowercase + digits + '-', k=LEN))
        SEED = list(SEED)
        SEED[0] = ''.join(random.choices(ascii_lowercase + digits))
        SEED[-1] = ''.join(random.choices(ascii_lowercase + digits))
        SEED = ''.join(SEED)
        return(SEED)

    def rq():
        f = open("~/py/quotes.txt", "r")
        QUOTES_LIST = f.readlines()
        print(random.choice(QUOTES_LIST))




# source = inspect.getsource(r)
# print(source)

def main():
    r.rq()


if __name__ == "__main__":
    main()


