class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        d = Counter(nums)
        while k>0:
            res.append(max(d, key=d.get))
            d.pop(res[-1])
            k-=1
        return res