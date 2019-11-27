#!/usr/bin/env python3

# Created by: DJ Watson
# Created on: November 2019
# This program calculates the volume of a rectangular prism


def calculate(length, width, height):
    # calculates the volume
    # process
    area = length * width * height
    # output
    print("")
    print("VOLUME: {}cm³".format(area))


def main():
    lencheck = input("length of cube (cm): ")
    widcheck = input("width of cube (cm): ")
    heicheck = input("height of cube (cm): ")
    try:
        lenint = int(lencheck)
        widint = int(widcheck)
        heigint = int(heicheck)
        calculate(lenint, widint, heigint)
    except ValueError:
        print("invalid input")


if __name__ == "__main__":
    main()
