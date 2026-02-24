class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        n1=0
        n=abs(x)
        while n!=0:
            d=n%10
            n1=n1*10+d
            n=n//10
        if x<0:
            n1*=-1
        if n1<-2**31 or n1>(2**31)-1:
            return 0
        return n1
