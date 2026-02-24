class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        n=0
        y=x
        if x<0:
            return False
        else:
            while x>0:
                d=x%10
                n=n*10+d
                x=x//10
            if n==y:
                return True
            return False
