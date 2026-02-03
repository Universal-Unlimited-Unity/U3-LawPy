import spacy

def exist(doc, i):
  if i < len(doc):
    return True
  return False

x = ["is","are","mean","refers","include","includes","constitutes","constitute","deemed","regarded","considered","understood","defined","called","known","represents","denotes","designates"]
r = {'keywords': 1, 'DET + NOUN + ADP + NOUN': 2, 'N + ADP + N': 3, 'DET + NOUN': 4, 'ADJ + NOUN': 5, 'NOUN': 6}
def term(doc: spacy.tokens.doc.Doc):
  print(doc)
  i = 0
  l = {}
  while i < len(doc):
    if exist(doc, i+1) and doc[i+1].text in x:
      l[doc[i].text] = 'keywords'
      i+=2
      continue

    if doc[i].pos_ == 'DET' and (exist(doc, i+1) and exist(doc, i+2) and exist(doc, i+3)) and doc[i+1].pos_ == 'NOUN' and doc[i+2].pos_ == 'ADP' and doc[i+3].pos_ == 'NOUN':
      l[doc[i+1].text + ' ' + doc[i+2].text + ' ' + doc[i+3].text] = 'DET + NOUN + ADP + NOUN'
      i+=4
      continue

    if doc[i].pos_ == 'NOUN' and (exist(doc, i+1) and exist(doc, i+2)) and doc[i+1].pos_ == 'ADP' and doc[i+2].pos_ == 'NOUN':
      l[doc[i].text + ' ' + doc[i+1].text + ' ' + doc[i+2].text] = 'N + ADP + N'
      i+=3
      continue

    if (doc[i].pos_ == 'DET' and exist(doc, i+1)) and doc[i+1].pos_ == 'NOUN':
      l[doc[i+1].text] = 'DET + NOUN'
      i+=2
      continue

    if doc[i].pos_ == 'NOUN':
      l[doc[i].text] = 'NOUN'
      i+=1
      continue
    if doc[i].pos_ == 'ADJ' and exist(doc, i+1) and doc[i+1].pos_ == 'NOUN':
      l[doc[i].text + ' ' + doc[i+1].text] = 'ADJ + NOUN'
      i+=2
      continue
    i+=1
  print(l)
  for key, value in l.items():
    l[key] = r[value]
  min_key = min(l, key=l.get)
  print(min_key)
  return l