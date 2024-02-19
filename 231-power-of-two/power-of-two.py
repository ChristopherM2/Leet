class Solution(object):
    import math
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<0):
            return False
        high = int(math.ceil(math.sqrt(n)))+1
        for i in range(high):
            if 2**i == n:
                return True
        return False
                
        