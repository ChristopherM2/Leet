from math import comb

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        out = [None for _ in range(n)]


        out[0] = [1]

        if n == 1:
            return out

        out[1] = [1,1]

        for i in range(2,n):
            row = [None for _ in range(i+1)]
            for j in range(0, i+1):
                row[j] = comb(i, j)
            out[i] = row

            
        return out