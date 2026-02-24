from os import *
from sys import *
from collections import *
from math import *

def countDigit(n: int) -> int:
   # Write your code here.
   count=0
   if n==0:
      return 1
   while n>0:
      count+=1
      n=n//10
   return count
