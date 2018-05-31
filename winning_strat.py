#!/usr/bin/python3
import re

def optimal_subset(words,c):
  def subs(w):
    ret = []
    for i in range(len(w)):
      if w[i] == c:
        ret.append(c)
      else:
        ret.append(".")
    return "".join(ret)
        
  occurencies = {}
  for w in words:
    pattern = subs(w)
    occ = occurencies.setdefault(pattern,0)
    occurencies[pattern] = occ+1
    
  key = ""
  max_occ = 0
  for pattern in occurencies.keys():
    if occurencies[pattern] > max_occ:
      max_occ = occurencies[pattern]
      key = pattern
  
  reg = re.compile("^"+key.replace(".","[^"+c+"]")+"$")
  return [w for w in words if reg.match(w) != None]



def rec_explo(current_words,old_chars,error_depth):

  if error_depth == maximum_depth and len(current_words) > 1:
    #print("Success : ",old_chars,"does not separate a set of size",len(current_words))
    return
  
  possible_chars = set([])
  for w in current_words:
    possible_chars = possible_chars | set(w)
  possible_chars = possible_chars - set(old_chars)
  possible_chars = list(possible_chars)
  possible_chars.sort()
  
  for c in possible_chars:
    new_words = optimal_subset(current_words,c)
    if(len(current_words) > comprehensive_threshold and len(new_words) > efficiency_factor * len(current_words)):
      continue
    
    chars = old_chars.copy()
    chars.append(c)
    
    if(len(new_words) == 1):
      print("Failure : set separated with ",chars,"\nThe only word is : ",new_words[0])
      return []
        
    error = 0 if (c in new_words[0]) else 1
    
    if rec_explo(new_words,chars,error_depth+error) == []:
      return []
    
  return current_words

f = open("winning_set.txt","r")
words = [w[:-1] for w in f]
f.close()
  
init_length = 3
maximum_depth = 10

efficiency_factor = 0.85
comprehensive_threshold = 15

i = 0

current_words = [w for w in words if len(w) == init_length]

rec_explo(current_words,["o"],0)




