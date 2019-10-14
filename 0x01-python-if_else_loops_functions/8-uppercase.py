#!/usr/bin/python3
def uppercase(str):
    upper = 0
    for up in str:
        if ord(up) >= ord('a') and ord(up) <= ord('z'):
            upper = 32
        else:
            upper = 0
        print("{:c}".format(ord(up) - upper), end='')
    print("")
