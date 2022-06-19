
from myClass import *

nulllist = []


list00 = ["about","empty","zebra"]
w00 = Wordlist(list00, "w01list")
w00.printwords(16)

list01 = ["about","baker","couch","deuce","empty"]
w01 = Wordlist(list01, "w02list")
w01.printwords(16)


'''
w02 = Wordlist(nulllist,"open test word list")
w02.readwordfile("five_letter.txt")
w02.printwords(16)
'''

w10 = Wordlist(w01.commonwords(w00.words),"common")
print(w10.title)
w10.printwords(16)

w11 = Wordlist(w01.uniquewords(w00.words),"unique w01 from w00 ")
w11.printwords(16)

w12 = Wordlist(w00.uniquewords(w01.words),"unique 00 from w01")
w12.printwords(16)