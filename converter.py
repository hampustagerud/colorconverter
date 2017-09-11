# 
#  MIT License

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
                for key in colors.keys():
                    print("%s : %s" % (key, str(colors[key])))

def readFile(filename):
    try:
        with open(filename) as f:
            lines = f.read().splitlines()
            for line in lines:
                evaluate(line)
    except FileNotFoundError:
        print("%s is not a valid file" % filename)

def evaluate(string):
    print(string)

def printHelp():
    print("\t?\tPrint this help")
    print("\tq\tExit")
    print("\texit\tExit")
    print("\tprint\tPrint all colors")
    print("\tfile [filenames]\t Load a files with given filenames, separated by spaces")

if __name__ == "__main__":
    main()

