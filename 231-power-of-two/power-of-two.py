class Solution(object):
    import math
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n and not (n & n - 1)
                
        