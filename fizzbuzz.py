#!/usr/bin/env python3


def readfile():
    with open("numfile.txt") as data_file:
        filelist = data_file.read().splitlines()
    print(filelist)


def main():
    readfile()


if __name__ == "__main__":
    main()
