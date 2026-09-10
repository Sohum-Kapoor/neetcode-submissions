class Solution:
    def isPalindrome(self, s: str) -> bool:
        accept = "abcdefghijklmnopqrstuvwxyz1234567890"
        s = s.lower()
        for ch in s:
            if ch not in accept:
                s = s.replace(ch, "")
        return s == s[::-1]