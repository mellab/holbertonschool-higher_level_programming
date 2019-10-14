#!/usr/bin/python3
for j in range(0, 10):
    for k in range(j + 1, 10):
        if j == 8 and k == 9:
            print("89")
        elif j != k:
            print("{:d}{:d}".format(j, k), end=", ")
