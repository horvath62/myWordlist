
from myClass import *

nulllist = []

'''
list00 = ["about","empty","zebra"]
w00 = Wordlist(list00, "w01list")
w00.printwords(16)

list01 = ["about","baker","couch","deuce","empty"]
w01 = Wordlist(list01, "w02list")
w01.printwords(16)
'''
'''
w02 = Wordlist(nulllist,"open test word list")
w02.readwordfile("five_letter.txt")
w02.printwords(16)
'''
'''
w10 = Wordlist(w01.commonwords(w00.words),"common")
print(w10.title)
w10.printwords(16)

w11 = Wordlist(w01.uniquewords(w00.words),"unique w01 from w00 ")
w11.printwords(16)

w12 = Wordlist(w00.uniquewords(w01.words),"unique 00 from w01")
w12.printwords(16)
'''

w20k = Wordlist(nulllist,"20K wordlist")
w20k.readwordfile("english_20k_words.txt")
#w20k.printwords(16,64)
w20kt = Wordlist(w20k.trimwords(5),"20K wordlist trimmed to 5 letter words")
w20kt.printwords(16, 64)

w58k = Wordlist(nulllist,"58K wordlist")
w58k.readwordfile("english_58k_words.txt")
#w58k.printwords(16,64)
w58kt = Wordlist(w58k.trimwords(5),"58K wordlist trimmed to 5 letter words")
w58kt.printwords(16, 64)

w350k = Wordlist(nulllist,"350K wordlist")
w350k.readwordfile("english_350k_words.txt")
#w350k.printwords(16,64)
w350kt = Wordlist(w350k.trimwords(5),"350K wordlist trimmed to 5 letter words")
w350kt.printwords(16, 64)


w60k = Wordlist(nulllist,"60K wordlist")
w60k.readwordfile("english_60k_words.txt")
#w60k.printwords(16,64)
w60kt = Wordlist(w60k.trimwords(5),"60K wordlist trimmed to 5 letter words")
w60kt.printwords(16, 64)

print('########## COMPARES #############################################')

w91 = Wordlist(w58kt.commonwords(w60kt.words),"common 58k & 60k")
w91.printwords(16,32)

w92 = Wordlist(w58kt.uniquewords(w60kt.words),"unique 58k from 60k ")
w92.printwords(16,32)

w93 = Wordlist(w60kt.uniquewords(w58kt.words),"unique 60k from 58k")
w93.printwords(16,32)

print('######## 350K compares ###############################################')

w96 = Wordlist(w58kt.uniquewords(w350kt.words),"unique 58k from 350k")
w96.printwords(20,60)

w97 = Wordlist(w60kt.uniquewords(w350kt.words),"unique 60k from 350k")
w97.printwords(20,60)

