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

def main():
    if len(sys.argv) > 1: 
        for i in range(1, len(sys.argv)):
            readFile(sys.argv[i])

    command = ""
    while command != "exit" and command != "q":
        command = input("> ").strip()
        
        if len(command) > 0:
            parts = command.split(" ")

            if parts[0] == "?":
                printHelp()
            elif parts[0] == "file" and len(parts) > 1:
                for i in range(1, len(parts)):
                    readFile(parts[i])

def readFile(filename):
    try:
        with open(filename) as f:
            lines = f.read().splitlines()
            for line in lines:
                evaluate(line)
    except FileNotFoundError:
        print(filename + " is not a valid file")

def evaluate(string):
    print(string)

def printHelp():
    print("\t?\tPrint this help")
    print("\tq\tExit")
    print("\texit\tExit")
    print("\tfile [filenames]\t Load a files with given filenames, separated by spaces")

if __name__ == "__main__":
    main()

