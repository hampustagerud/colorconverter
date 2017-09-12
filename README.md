# ColorConverter
Small python application for breaking down hex colors to components and then being able to print the list using a format specified by the user.

## Colors
Colors are written with following syntax: 

```
Name:Hex
```

Name can be any string while Hex must be a string starting with "#". The rest of the letters must be 0-F and the value can be using 3, 4, 6 or 8 bytes (#000 (rgb), #0000 (rgba), #000000 (rgb), #00000000 (rgba)). If no alpha channel is supplied, the value is set to 255 by default.

Name and Hex must be seperated by a colon (':') but any whitespace added for readability should be stripped.

## Application
Application is written with Python3 ~and currently not backwards compatible with Python2 :(~ but should work fine with Python2 now :)

```
Commands:
? - Prints help text
q - Exit application
exit - Exit application
color [name:hex] - Add color with specified name and hex value
print [filename] - Print list of all colors using a specified format, prints to file if filename is provided
file [filenames] - Loads one or more text files with colors
```

## Files
Files are simple textfiles using following format:
```
# Comments goes here
[Name:Hex]

# Examples
Black:#000000
White:#FFF
Green:#00FF00FF
```

## Future
- [ ] Comment code
- [ ] Ability to use RGB(A) for constructing Color objects
- [x] Python2 compability

## License

MIT License

Copyright (c) 2017 Hampus Tågerud

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
