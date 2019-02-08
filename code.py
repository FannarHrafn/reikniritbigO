import itertools
import string

def hanoi(n,A,B,C):
    if n==1:
        print ("Faera disk %s fra %s til %s" %(n,A,B))
    else:
        hanoi(n-1,A,C,B)
        print ("Faera disk %s fra %s til %s" %(n,A,B))
        hanoi(n-1,C,B,A)

hanoi(3,"A","B","C")

def combine(n):
    return list(map("".join,itertools.combinations('abcdefghijklnmopqrstuvwxyz',n)))
print combine(3)
print len(combine(3))
