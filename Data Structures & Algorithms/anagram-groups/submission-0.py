class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i,st in enumerate(strs):
            res.setdefault("".join(sorted(st)), []).append(st)

        return list(res.values())