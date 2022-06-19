
from myClass import *

nulllist = []

w01 = Wordlist(nulllist,"20K word list")
w01.printwords(10)
w01.addword("new")
w01.printwords(10)

print(w01.getWordTitle())
print(w01.getWordcount())

