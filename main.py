
from myClass import *

nulllist = []


list00 = ["about","empty","zebra"]
w00 = Wordlist(list00, "w01list")
w00.printwords(16,16)

list01 = ["about","baker","couch","deuce","empty"]
w01 = Wordlist(list01, "w02list")
w01.printwords(16,16)

w01.addword("abcde")

w01.writewordfile("testfile.txt")

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
w20k = Wordlist(w20k.trimwords(5),"20K wordlist trimmed to 5 letter words")
w20k.printwords(16, 64)

w58k = Wordlist(nulllist,"58K wordlist")
w58k.readwordfile("english_58k_words.txt")
w58k = Wordlist(w58k.trimwords(5),"58K wordlist trimmed to 5 letter words")
w58k.printwords(16, 64)

w350k = Wordlist(nulllist,"350K wordlist")
w350k.readwordfile("english_350k_words.txt")
w350k = Wordlist(w350k.trimwords(5),"350K wordlist trimmed to 5 letter words")
w350k.printwords(16, 64)

w60k = Wordlist(nulllist,"60K wordlist")
w60k.readwordfile("english_60k_words.txt")
w60k = Wordlist(w60k.trimwords(5),"60K wordlist trimmed to 5 letter words")
w60k.printwords(16, 64)

w71k = Wordlist(nulllist,"71K word list")
w71k.readwordfile("english_71k_words.txt")
w71k = Wordlist(w71k.trimwords(5),"71K wordlist trimmed to 5 letter words")
w71k.printwords(16, 64)

ww = Wordlist(nulllist,"wordle wordlist")
ww.readwordfile("wordlelist.txt")
ww.printwords(16,64)
ww = Wordlist(ww.makelowercase(),"wordle list lower case")
ww.printwords(16, 64)


print('########## COMPARES #############################################')

w71kmiss = Wordlist(ww.uniquewords(w71k.words),"wordle words missed from 71k ")
w71kmiss.printwords(16,32)

w350kmiss = Wordlist(ww.uniquewords(w350k.words),"wordle words missed from 350k ")
w350kmiss.printwords(16,32)


'''
wmerge = Wordlist(w58k.words,"merged")
wunique = Wordlist(w60k.uniquewords(w58k.words),"unique list")
for w in wunique.words:
    wmerge.addword(w)
wmerge.printwords(16,1000)

wsorted = Wordlist(sorted(wmerge.words),"merged and sorted")
wsorted.printwords(16,1000)

wsorted.writewordfile("sorted.txt")
'''
print('######## 350K compares ###############################################')
'''
w96 = Wordlist(w58k.uniquewords(w350k.words),"unique 58k from 350k")
w96.printwords(20,60)

w97 = Wordlist(w60k.uniquewords(w350k.words),"unique 60k from 350k")
w97.printwords(20,60)
'''



