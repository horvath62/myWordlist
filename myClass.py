class Wordlist:
  def __init__(self, words, title ):
      self.words = words
      self.title = title

  def readwordfile(self, filename):
      try:
          with open(filename, "r") as fh:
              self.words = fh.read().splitlines()
              fh.close()
          return 1
      except IOError:
          print("IOError: ",filename," File does not appear to exist.")
          return 0

  def commonwords(self, wordlist):
      commonlist = []
      for w in self.words:
          for x in wordlist:
              if w == x:
                  commonlist.append(w)
      return commonlist

  def uniquewords(self, wordlist):
      uniquelist = []
      for w in self.words:
          common = False
          for x in wordlist:
              if w == x:
                  common = True
          if common == False:
              uniquelist.append(w)
      return uniquelist

  def getWordcount(self):
      return len(self.words)

  def addword(self, word):
      self.words.append(word)

  def printwords(self, numcols):
      print("##########")
      print(self.title, " ", len(self.words), " Words" )
      i=0

      for w in self.words:
          print(w, " ", end="")
          i = i + 1
          if i % numcols == 0:
            print("")

      print("")


