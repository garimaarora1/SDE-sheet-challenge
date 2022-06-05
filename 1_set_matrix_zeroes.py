from os import *
from sys import *
from collections import *
from math import *

from typing import List

def setZeros(a: List[List[int]]) -> None:
    r=c=False
    for i in range(len(a)):
        for j in range(len(a[0])):
            if a[i][j]==0:
                a[0][j]=a[i][0]=0
                if i==0:
                    r=True
                if j==0:
                    c=True
    for i in range(1,len(a)):
        for j in range(1,len(a[0])):
            if a[0][j]==0 or a[i][0]==0:
                a[i][j]=0
    if r:
        for j in range(len(a[0])):
            a[0][j]=0
    if c:
        for i in range(len(a)):
            a[i][0]=0