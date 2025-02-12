# My solution:
# Brute-Force substring searching algorithm was used. Can be optimized for a exact case.
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        idx = 0
        while True:
            if len(part) > len(s) or len(part) == 0:
                return s

            if s[idx:idx + len(part)] == part:
                s = s[:idx] + s[idx + len(part):]
                idx = max(0, idx - len(part) - 1)
            else:
                idx += 1
            
            if idx > len(s) - len(part):
                return s

# Simple solution:
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part,"",1)
        return s