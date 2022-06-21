#  WORDLIST CLASS DEVELOPMENT AND TEST PROGRAM
from myClass import *

list00 = ["about","empty","zebra"]
w00 = Wordlist(list00, "w01list")
w00.printwords(16,16)

list01 = ["about","baker","couch","deuce","empty"]
w01 = Wordlist(list01, "w02list")
w01.printwords(16,16)
w01.addword("abcde")
#w01.writewordfile("testfile.txt")

'''
w02 = Wordlist([],"open test word list")
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

w20k = Wordlist([],"20K wordlist")
w20k.readwordfile("fiveletter_20k_english_20k_trimmed.txt")
w20k = Wordlist(w20k.trimwords(5),"20K wordlist trimmed to 5 letter words")
w20k.printwords(16, 64)
w20k.writewordfile("fiveletter_20k.txt")

w58k = Wordlist([],"58K wordlist")
w58k.readwordfile("english_58k_words.txt")
w58k = Wordlist(w58k.trimwords(5),"58K wordlist trimmed to 5 letter words")
w58k.printwords(16, 64)
w58k.writewordfile("fiveletter_58k.txt")

w350k = Wordlist([],"350K wordlist")
w350k.readwordfile("english_350k_words.txt")
w350k = Wordlist(w350k.trimwords(5),"350K wordlist trimmed to 5 letter words")
w350k.printwords(16, 64)
w350k.writewordfile("fiveletter_350k.txt")

w60k = Wordlist([],"60K wordlist")
w60k.readwordfile("english_60k_words.txt")
w60k = Wordlist(w60k.trimwords(5),"60K wordlist trimmed to 5 letter words")
w60k.printwords(16, 64)
w60k.writewordfile("fiveletter_60k.txt")

w71k = Wordlist([],"71K word list")
w71k.readwordfile("english_71k_words.txt")
w71k = Wordlist(w71k.trimwords(5),"71K wordlist trimmed to 5 letter words")
w71k.printwords(16, 64)
w71k.writewordfile("fiveletter_71k.txt")

ww = Wordlist([],"wordle wordlist")
ww.readwordfile("wordlelist.txt")
ww.printwords(16,64)
ww = Wordlist(ww.makelowercase(),"wordle list lower case")
ww.printwords(16, 64)


print('########## COMPARES #############################################')

w71kmiss = Wordlist(w20k.uniquewords(w71k.words),"71k words missing from 20k ")
w71kmiss.printwords(16,32)

w350kmiss = Wordlist(w20k.uniquewords(w350k.words),"350k words missing from 20k ")
w350kmiss.printwords(16,32)


'''
# MERGING TWO WORD LISTS
wmerge = Wordlist(w58k.words,"merged")
wunique = Wordlist(w60k.uniquewords(w58k.words),"unique list")
for w in wunique.words:
    wmerge.addword(w)
wmerge.printwords(16,1000)

wsorted = Wordlist(sorted(wmerge.words),"merged and sorted")
wsorted.printwords(16,1000)

wsorted.writewordfile("sorted.txt")
'''
