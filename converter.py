#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 
#  MIT License
#
#  Copyright (c) 2017 Hampus Tågerud
#  
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files
#  (the "Software"), to deal in the Software without restriction, 
#  including without limitation the rights to use, copy, modify, merge,
#  publish, distribute, sublicense, and/or sell copies of the Software,
#  and to permit persons to whom the Software is furnished to do so,
#  subject to the following conditions:
#  
#  The above copyright notice and this permission notice shall be included 
#  in all copies or substantial portions of the Software.
#  
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS 
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF 
#  MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
#  IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#  CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, 
#  TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
#  SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

from __future__ import print_function
import sys 

class Color:
    hex = ""
    red = 0
    green = 0
    blue = 0
    alpha = 1

    def __init__(self, color):
        if color.startswith("#"):
            self.hex = color.upper()

            if len(color) < 6:
                temp = "#"
                for i in range(1, len(color)):
                    temp += color[i]
                    temp += color[i]
                color = temp

            value = int(color.lstrip("#"), 16)
            if len(color) > 7:
                self.red = (value >> 24) & 0xFF
                self.green = (value >> 16) & 0xFF
                self.blue = (value >> 8) & 0xFF
                self.alpha = value & 0xFF
            else:
                self.red = (value >> 16) & 0xFF
                self.green = (value >> 8) & 0xFF
                self.blue = value & 0xFF

    def __repr__(self):
        return ("Hex: %s, rgba(%s, %s, %s, %s)" % 
                (self.hex, self.red, self.green, self.blue, self.alpha))
    __str__ = __repr__

def main():
    global colors
    colors = {}

    if len(sys.argv) > 1: 
        for i in range(1, len(sys.argv)):
            readFile(sys.argv[i])

    command = ""
    while command.lower() != "exit" and command.lower() != "q":
        command = input("> ").strip()
        
        if len(command) > 0:
            parts = command.split(" ")

            if parts[0] == "?":
                printHelp()
            elif parts[0].lower() == "file" and len(parts) > 1:
                for i in range(1, len(parts)):
                    readFile(parts[i])
            elif parts[0].lower() == "print":
                if len(parts) > 1:
                    printColors(parts[1])
                else:
                    printColors()
            elif parts[0].lower() == "color":
                evaluate("".join(parts[i] for i in range(1, len(parts))))
            elif parts[0].lower() != "exit" and parts[0].lower() != "q": 
                print("%s is not a valid command, use '?' for help" % command)

def printColors(filename = ""):
    global colors
    format = input("Specify format "
            "(Name=$N, Red=$R, Green=$G, Blue=$B, Alpha=$A, Hex=$H): ")

    try:
        if len(filename) > 0:
            f = open(filename, "w")
        else:
            f = None

        for key in colors.keys():
            temp = format
            temp = (temp.replace("$N", str(key))
                        .replace("$R", str(colors[key].red))
                        .replace("$G", str(colors[key].green))
                        .replace("$B", str(colors[key].blue))
                        .replace("$A", str(colors[key].alpha))
                        .replace("$H", str(colors[key].hex))
            )

            if f is None:
                print(temp)
            else:
                print(temp, file=f)
    except IOError:
        print("Could not save %s" % filename)

    if f is not None:
        f.close()

def readFile(filename):
    try:
        with open(filename) as f:
            lines = f.read().splitlines()
            for line in lines:
                evaluate(line)
    except FileNotFoundError:
        print("%s is not a valid file" % filename)

def evaluate(string):
    if string.startswith("#") or len(string) == 0:
        return
    
    global colors
    parts = string.split(":")
    
    if len(parts) == 2 and isHex(parts[1]):
        colors[parts[0].strip()] = Color(parts[1].strip())
    else:
        print("%s is not a valid color" % string)

def isHex(string):
    ranges = [(48, 57), (65, 70)]
    for char in string.strip():
        if (char != "#" and not 
            any(lower <= ord(char) <= upper for (lower, upper) in ranges)):
            return False
    return True

def printHelp():
    print("\t?\tPrint this help")
    print("\tq\tExit")
    print("\texit\tExit")
    print("\tcolor [name:hex]\tAdd color with specified name and value")
    print("\tprint [filename]\tPrint all colors, to file if filename is provided")
    print("\tfile [filenames]\t "
          "Load a files with given filenames, separated by spaces")

if __name__ == "__main__":
    try:
        input = raw_input
    except NameError:
        pass

    main()

