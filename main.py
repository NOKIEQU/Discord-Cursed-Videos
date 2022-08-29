from fileinput import filename
import string
import mmap

print("1: MP4")
print("2: WEBM")

option = input("Select Option: ")

print("Make sure the script and the file is in the same folder!")
file = input("Select file name (without extension): ")
           

def ReadFile(filename):
    if not "." in filename:
        print("OK giv me a minute")

        with open(filename+".mp4", "rb") as f:
            s = f.read()
            hex = b'\x6c\x6d\x76\x68\x64'  #lmhvd b'\x6c\x6d\x76\x68\x64'
            hex_length = 5
            if s.find(hex):
              print(hex[hex_length])
            else: 
                print("no")

    else:
        print("Your file contains extension. Aborting")

def CheckOption(option, filename):
    if option == 1:
        ReadFile(filename)
    else:
        ReadFile(filename)

   

CheckOption(option, file)

