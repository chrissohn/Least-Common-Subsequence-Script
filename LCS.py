#!/usr/bin/python

from __future__ import print_function
import sys 
from itertools import combinations

f = open(sys.argv[1], 'rb')
lines = f.readlines()
i=0
for line in lines:#to get number of lists that need to be instantiated for seqList
    i+=1
seqList = [[None,None]] * i#list of lists of string name and string for input into LCS function 
i=0
for line in lines:
    lines1 = line.split()
    if len(lines1) != 3:
        print("Invalid Input. Exiting.")
        exit()
    seqList[i] = [lines1[0]]#adding the string name as the first index of the list
    seqList[i].append(lines1[2])#adding the string as the second index of the list
    i+=1
combos = list(combinations(seqList,2))#combinations function to compare every different combination of strings

def LCS(X, Y):
    d=0
    lenX = len(X)
    lenY = len(Y)
    b = [ [0 for _ in range(1,n+1)] for _ in range(1,lenX+1)]#to create b, which will be used to print the LCS
    c = [ [0 for _ in range(0,n+1)] for _ in range(0,lenY+1)]#to create c, which is used to find the length of the LCS
    for i in range(0,m+1):#have all the array indices of c = 0 to find out the length of LCS 
        c[i][0] = 0
    for j in range(0,n+1):
        c[0][j] = 0
    for i in range(0,m):#the for loop is to assign values to b for printing the LCS and incrementing c for length of LCS
        for j in range(0, n):
            d+=1#used to keep track of comparisons 
            if X[i] == Y[j]:
                c[i][j] = c[i-1][j-1]+1
                d+=1
                b[i-1][j-1] = "diagonal"
            elif c[i-1][j] >= c[i][j-1]:
                d+=1
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = "up"
            else:
                d+=1
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = "left"
    return(c,b,d)

def printLCS(b,X,i,j):#accepting the input of array b, string X, X.length, and Y.length
    if i == -1 or j == -1:
        return
    if b[i-1][j-1] == "diagonal":
        printLCS(b,X,i-1,j-1)
        print(X[i], end="")
    elif b[i-1][j-1] == "up":
        printLCS(b,X,i-1,j)
    else:
        printLCS(b,X,i,j-1)
i=0

for item in combos:#to print out the relative statistics and required output of the program with combos from combinations
    X = item[0][1]
    Y = item[1][1]
    c,b,d = LCS(X,Y)
    print("Longest common subsequence between " + item[0][0] + " and " + item[1][0])
    printLCS(b,X,len(X)-1,len(Y)-1)
    print("")
    print("LCS length: " + str(c[len(X)-1][len(Y)-1]))#length of LCS 
    print("Number of comparisons: " + str(d))
    if i != len(combos)-1:
        print("")
    i+=1
