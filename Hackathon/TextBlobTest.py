from textblob import TextBlob

def findAssociated(keyword, keywordType, words):
  # words is a list of Word objects with the word as a string, (x,y) of middle,
  # height, and width of text box
  keyCordsFound = []
  found = False
  for i in words:
    if i.text == keyword:
      keyCordsFound.append(i.cord)
      found = True
  if not found:
    return -1
  for i in keyCordsFound:
    dists = []
    for word in enumerate(words):
      dists.append((word.cord[0] - i[0])**2 + (word.cord[1] - i[1])**2)
    usedIn = []
    b = True
    while(b):
      minimum = 0
      for ind, dist in enumerate(dists):
        if dist < dists[minimum] and ind not in usedIn:
          minimum = ind
      blob = TextBlob(words[minimum].text)
      if(blob.tags[0][1] == keywordType[1]):
        return words[minimum]
      else:
        usedIn.append(minimum)
        if len(usedIn) >= len(words):
          b = False




'''
def makeSentences(words):
  #words is a list of Word objects with the word as a string, (x,y) of middle,
  #height, and width of text box
  linelist = []
  for i in words:
    line = []
    for j in words:
      if(i.cord[1] == j.cord[1]):
        line.append(j)
        words.remove(j)
    linelist.append(line)
  for index, element in enumerate(linelist):
    if i[0].cord[1] < min:
'''