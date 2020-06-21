Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""
 

Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.

Python3 program:

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        D = [ord(c) - ord('a') for c in S]
        P = 26
        MOD = 2 ** 32
        
        def rolling_hash(L):
            # initial window
            h = 0
            for c in D[:L]: h = (h * P + c) % MOD
            seen = {h}
            
            PP = P ** L % MOD
            # sliding window
            for r, c in enumerate(D[L:], L):
                # update window
                #  shift left    emit the old left    adding the new right    
                h = (h * P    -   D[r - L] * PP     +   c) % MOD
                if h in seen: return r - L + 1  # return start index for the duplicated window
                seen.add(h)
            return None
        
        # use binary search to find the max length of duplicated windows
        l, h = 0, len(S)
        while l < h:
            m = (l + h) // 2
            if rolling_hash(m): l = m + 1
            else: h = m
        start = rolling_hash(l-1)
        return S[start: start + l - 1]
