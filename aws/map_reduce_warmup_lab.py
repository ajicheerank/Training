import re
import string
import collections as c
import numpy as np

def mapper(document):
    doc = open(document, "rt")    
    txt = doc.read()
    words  = re.split(r'\W+', txt)
    words = [word.lower() for word in words]
    words_np = [word for word in words if word not  in string.punctuation]
    words_clean = [(word,1) for word in words_np if word not in {'a','in','s','and','or','but','on','at','of','is','the', 'it'}]
    return words_clean

def reducer(lst):
    collector = c.defaultdict(list)
    for word, val in lst:
        collector[word].append(val)
    return collector.items()

def word_count(documents):
    lst = [] 
    for doc in documents:        
        lst = lst + (mapper(doc)) 
    lst.sort()    
    return reducer(lst)

def reduce_with_f(f,key,val):
    yield (key,f(val))
    
def f_reducer(agg_f,lst):
    for word, val in lst:
        sum_l = reduce_with_f(agg_f, word,val)        
        for i in sum_l:
            print(i)
    
if __name__ == '__main__':     
    red_list = word_count(["alice.txt","PG.txt"])
    f_reducer (np.sum, red_list)
