class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i,num in enumerate(nums):
            other = target - num
            # we want 7 3+4 4 -7 = 
            if other in dic:
                return [dic[other], i]
            dic[num] = i
        return []