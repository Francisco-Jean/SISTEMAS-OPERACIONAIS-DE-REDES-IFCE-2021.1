#!/usr/bin/python

import cgitb, cgi
from open import *
cgitb.enable()

print("Content-type:text/html\r\n\r\n")

if __name__ == '__main__':
    
    print(abrirArquivo('index.html'))