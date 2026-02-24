import math
class Solution:
    def isPrime(self, n):
        # code here
        count=0
        if n<=1:
            return False
        for i in range(2,int(math.sqrt(n)+1)):
            if n%i==0:
                count+=1
        if count==0:
            return True
        else:
            return False
