#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    ac = len(argv) - 1
    count = 1

    if ac:
        print("{} arguments:".format(ac))
    else:
        print("{} arguments.".format(ac))

    for i in argv[1:]:
        print("{:d}: {}".format(count, i))
        count += 1
