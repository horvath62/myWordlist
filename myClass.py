class Wordlist:
  def __init__(self, words, title ):
      self.words = words
      self.title = title



  def getWordcount(self):
      return len(self.words)

  def getWordTitle(self):
      return len(self.title)

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


