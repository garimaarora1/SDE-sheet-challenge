from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(nums, n) :

    maxi=nums[0]
    s=0
    for i in range(n):
        s+=nums[i]
        maxi=max(s,maxi)
        if s<0:
            s=0
    return max(maxi,0)

#taking inpit using fast I/O
def takeInput() :
	
    n =  int(input())

    if(n == 0) :
        return list(), n

    arr = list(map(int, stdin.readline().strip().split(" ")))

    return arr, n


#main
arr, n = takeInput()
print(maxSubarraySum(arr, n))
