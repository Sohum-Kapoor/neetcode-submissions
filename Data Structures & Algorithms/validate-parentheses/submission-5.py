class Solution:
    def isValid(self, s: str) -> bool:
        pair = {'(' : ')', '{' : '}', '[' : ']'}
        L = [s[0]]
        s = s[1:]
        for ch in s:
            if ch in pair.values():
                if len(L) == 0 or L[-1] not in pair or pair[L[-1]] != ch:
                    return False
                L.pop()
            else:
                L.append(ch)
        return len(L) == 0