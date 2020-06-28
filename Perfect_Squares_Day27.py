Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3 
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

Python3 code:

class Solution:
    def numSquares(self, n: int) -> int:
        i,k,squares = 1,1,[]
        while (k <= n):
            squares.append(k)
            i+= 1
            k = i ** 2
        
        #print(squares)
        dp = [float('inf') for _ in range(n+1)]
        #    0 1 2 3 4 5 6 .. 12
        # 1    1 2 3 4 5
        # 4          1 2 ..  3
        # 9    
        
        for s in squares:
            for i in range(1,n+1):
                if s <= i:
                    if i % s == 0:
                        can = i //s
                        dp[i] = min(can,dp[i])
                    else:
                        dp[i] = min(1+dp[i-s],dp[i])
                    
        return dp[n]
