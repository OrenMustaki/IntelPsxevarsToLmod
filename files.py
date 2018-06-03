#!/usr/bin/env python3
#
# Project : IntelPsxevarsToLmod
#
import os
import sys
import subprocess as sp

class Files:
    def __init__(self):
        self.files = {'gcc':'', 'env':''}
        for key, item in self.files.items():
            self.check(key)    

    def find(self, name, path):
        for root, dirs, files in os.walk(path):
            if name in files:
                return os.path.join(root, name)
        return False
   
    def check(self, file):
        self.files[file] = sp.getoutput(f'which {file}') 
        if not os.path.isfile(self.files[file]):
            print(f"Could not find a valid {file} command")
            exit()
        else:
            return self.files[file]

if __name__ == '__main__':
    f = Files()
    print(f)

