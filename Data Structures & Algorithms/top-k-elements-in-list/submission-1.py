class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        D = {}
        for num in nums:
            if num in D:
                D[num] += 1
            else:
                D[num] = 1
        return [i[0] for i in sorted(D.items(), key = lambda item: item[1], reverse = True)[:k]]