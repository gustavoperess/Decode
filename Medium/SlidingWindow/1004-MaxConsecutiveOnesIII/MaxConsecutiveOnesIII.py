from typing import List



class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, count = 0, 0
        n = len(nums)
        ans = 0
        for r in range(n):
            if nums[r] == 0:
                count += 1
            while count > k:
                if nums[l] == 0:
                    count -= 1 
                l += 1
      
            ans = max(ans, r - l + 1)

        return ans
    
        
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count, ans = 0,0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                ans = max(ans, count)
            else:
                count = 0
        print(ans)
        return ans



result = Solution()
#result.longestOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3)
#result.longestOnes(nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2)
result.findMaxConsecutiveOnes(nums = [1,1,0,1,1,1])