import math


def hashing_func(key, m):
  k = sum([ord(items) for items in list(key)])
  A = 0.6180339887
  h = math.floor(m * ((k *A) % 1))
  return h

def insert(hash_table, key, value):
    hash_key = hashing_func(key,len(hash_table))
    data= [value]
    if(len(hash_table[hash_key]) == 0):
      hash_table[hash_key] = data
    else:
      hash_table[hash_key].append(value)

def search(hash_table, key):
    hash_key = hashing_func(key,len(hash_table)) 
    if(len(hash_table[hash_key]))==0:
      print("\nNot found \n")
    else:
      print("\nFound")


hash_table = [[] for _ in range(10)]
f = open("data.txt", "r")
for x in f:
  key, value = x.split()
  insert(hash_table, key, value)
  
print(hash_table)
search(hash_table, "kushalbhandari")
search(hash_table, "adrianawise")
search(hash_table, "johndoe")
search(hash_table, "random")








 
