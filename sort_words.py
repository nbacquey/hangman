f = open("words.txt","r")

word_list = [w[:-1] for w in f]

f.close()

set_by_size = [[] for i in range(30)]
word_by_size = [[] for i in range(30)]

for w in word_list:
  set_by_size[len(w)].append(set(w))
  word_by_size[len(w)].append(w)
  
occ_by_size = [{'nb':0} for i in range(30)]

for i in range(30):
  for s in set_by_size[i]:
    for c in s:
      occ = (occ_by_size[i]).setdefault(c,0)
      (occ_by_size[i])[c] = occ+1
    ((occ_by_size[i])['nb']) += 1
    
freq_by_size = [{} for i in range(30)]

for i in range(30):
  for c in occ_by_size[i].keys():
    if c != 'nb':
      freq_by_size[i][c] = occ_by_size[i][c] / occ_by_size[i]['nb']
      
score_by_size = [{} for i in range(30)]

for i in range(30):
  for w in word_by_size[i]:
    score = 1
    for c in set(w):
      if 'aeiouy'.find(c) == -1:
        score *= freq_by_size[i][c]
    score_by_size[i][w] = score
    
  
for i in range(30):
  word_by_size[i].sort(key = lambda x : score_by_size[len(x)][x])
  
  

  

  
      