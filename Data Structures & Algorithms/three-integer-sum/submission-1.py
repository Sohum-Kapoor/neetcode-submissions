class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        D = {}
        for num in nums:
            if num in D:
                D[num] += 1
            else:
                D[num] = 1
        triplets = []
        for key1 in D:
            for key2 in D:
                key3 = 0 - key1 - key2
                if key3 in D:
                    if key1 == key2 and D[key1] <= 1 or key1 == key3 and D[key1] <= 1 or key2 == key3 and D[key2] <= 1 or key1 == key2 and key2 == key3 and D[0] < 3 or sorted([key1, key2, key3]) in triplets:
                        continue
                    triplets.append(sorted([key1,key2,key3]))
        return triplets