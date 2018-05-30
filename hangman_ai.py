#!/usr/bin/python3
import re
import sys
from getopt import getopt
  
def find_separator_0(regexp, candidate_chars,old_candidates):
  regexp_comp = re.compile("^"+regexp.replace("_","["+("".join(candidate_chars))+"]")+"$")
  candidates = [w for w in old_candidates if (regexp_comp.match(w) != None)]
  candid_set = [set(w) for w in candidates]
  
  #print("candidates : ",candidates)
  if(len(candidates) == 1):
    for i in range(len(regexp)):
      if(regexp[i] == "_"):
        return (candidates[0][i],candidates)
  
  score = len(candidates)
  
  for c in candidate_chars:
    
    new_score = 0
    for s in candid_set:
      if c in s:
        new_score += 1
        
    new_score = abs(len(candidates)/2 - new_score)
    if new_score < score:
      score = new_score
      ret = c
  return (ret,candidates)

def find_separator_1(regexp, candidate_chars,old_candidates):
  regexp_comp = re.compile("^"+regexp.replace("_","["+("".join(candidate_chars))+"]")+"$")
  candidates = [w for w in old_candidates if (regexp_comp.match(w) != None)]
  candid_set = [set(w) for w in candidates]
  
  print("candidates : ",candidates)
  if(len(candidates) == 1):
    for i in range(len(regexp)):
      if(regexp[i] == "_"):
        return (candidates[0][i],candidates)
  
  score = 0
  
  for c in candidate_chars:
    
    new_score = 0
    for s in candid_set:
      if c in s:
        new_score += 1
        
    if new_score > score:
      score = new_score
      ret = c
  return (ret,candidates)


def update_regexp(regexp, c, w):
  ret = list(regexp)
  for i in range(len(w)):
    if w[i] == c:
      ret[i] = c
  return "".join(ret)

def process_word(word,word_list,separator):
  regexp = "_"*len(word)
  candidate_chars = set("abcdefghijklmnopqrstuvwxyz")
  candidates = word_list
  errors = 0
  
  #print("\n\nTesting ",word)
  
  while(regexp.find("_") >= 0):
    #print(regexp)
    (c,candidates) = separator(regexp,candidate_chars,candidates)
    #print("separator : ",c)
    new_regexp = update_regexp(regexp, c, word)
    candidate_chars.remove(c)
    if new_regexp == regexp:
      errors += 1
      candidates = [w for w in candidates if (w.find(c) == -1)]
    else:
      regexp = new_regexp
  return errors


def sort_by_hardness(filename,separator):
  f = open(filename+".txt","r")
  word_list = [w[:-1] for w in f]
  f.close()

  hardness = {}
  i = 0
  for w in word_list:
    i += 1
    if (i % 100 == 0):
      print(i)
    hardness[w] = process_word(w,word_list,separator)
  
  word_list.sort(key = lambda w : hardness[w])
  
  #for w in word_list:
    #print(w, hardness[w])
    
  f = open(filename+"_sorted_"+sys.argv[2]+".txt","w")
  for w in word_list:
    f.write(w+" : "+str(hardness[w])+"\n")
  f.close()
  
  
  
def interactive_guess(filename, separator):
  
  f = open(filename+".txt","r")
  word_list = [w[:-1] for w in f]
  f.close()
  
  regexp = input("Enter initial expression :")
  
  candidate_chars = set("abcdefghijklmnopqrstuvwxyz")
  candidates = word_list
  errors = 0
  
  #print("\n\nTesting ",word)
  
  while(regexp.find("_") >= 0):
    #print(regexp)
    (c,candidates) = separator(regexp,candidate_chars,candidates)
    #print("separator : ",c)
    print("My guess is :",c) 
    new_regexp = input("Enter updated expression :")
    candidate_chars.remove(c)
    if new_regexp == regexp:
      errors += 1
      candidates = [w for w in candidates if (w.find(c) == -1)]
    else:
      regexp = new_regexp
  
  print("Found \""+regexp+"\" with",errors,"errors !")


  
def main():
  separators = [find_separator_0,find_separator_1]
  
  filename = sys.argv[-1]
  (options,_) = getopt(sys.argv[1:-1],"is:")
  
  separator = find_separator_1
  for (opt,val) in options:
    if opt == "-s":
      separator = separators[int(val)]
        
  if(("-i","") in options):
    print("\nInteractive mode with separator",separator)
    interactive_guess(filename, separator)
  else:
    print("\nSorting mode on",filename+".txt","with separator",separator)
    sort_by_hardness(filename, separator)


main()
  



