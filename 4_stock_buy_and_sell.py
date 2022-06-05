from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    max_profit = 0
    least_most = prices[0]
    for i in range(1,len(prices)):
        if prices[i] < least_most:
            least_most = prices[i]
        else:
            max_profit = max(max_profit, prices[i]-least_most)
    return max_profit