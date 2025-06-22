
# 2138. Divide a String Into Groups of Size k

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        n = len(s)
        for i in range(0,n,k):
            result.append(s[i:i+k])
        if n % k :
            last_string = result[-1] + fill*(k-n%k)
            result[-1] = last_string
        return result
"""

short :
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        res = []  # grouped string
        n = len(s)
        curr = 0  # starting index of each group
        # split string
        while curr < n:
            res.append(s[curr : curr + k])
            curr += k
        # try to fill in the last group
        res[-1] += fill * (k - len(res[-1]))
        return res
"""
