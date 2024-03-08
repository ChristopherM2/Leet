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
            row[0] = 1
            row[-1] = 1
            # print(out, i+1, i+1-1)
            for j in range(1, i+1 - 1):
                row[j] = out[i-1][j] + out[i-1][j-1]
            out[i] = row

            
        return out