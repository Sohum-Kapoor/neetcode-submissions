class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        S = set()
        ptr1 = 0
        ptr2 = 0
        longest = 0
        while ptr2 != len(s):
            while s[ptr2] in S:
                S.remove(s[ptr1])
                ptr1 += 1
            S.add(s[ptr2])
            ptr2 += 1
            longest = max(longest, ptr2 - ptr1)
        return longest