class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = {}
        for st in strs:
            count = str(sorted(st))
            if count in D:
                D[count].append(st)
            else:
                D[count] = [st]
        return list(D.values())