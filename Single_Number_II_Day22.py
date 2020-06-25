Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99

Python3 program:

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # count = Counter(nums)
        # for k,v in count.items():
        #     if v == 1:
        #         return k
        
        one, two = 0,0
        for x in nums:
            # three = three ^ (one & two & x)
            two = two ^ (one & x)
            one = one ^ x
            not_three= ~(two & one)
            
            one, two = not_three & one, not_three & two
            
        return one
