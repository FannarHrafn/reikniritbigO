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

def revcombine(n):
    return list(map("".join,itertools.combinations('abcdefghijklnmopqrstuvwxyz'[::-1],n)))

alist = revcombine(5)
def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            print(i)
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
bubbleSort(alist)
print(alist)
