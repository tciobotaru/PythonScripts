#!/usr/bin/python3.11

import argparse 
parser = argparse.ArgumentParser(description='Read a files extension')
parser.add_argument('filename',type=str, help='the file to read the extension from')
args=parser.parse_args()
index=args.filename.find(".")
extension=args.filename[index:]

if index<0 :
    print("Error no file extension")
else :
    print(extension)


