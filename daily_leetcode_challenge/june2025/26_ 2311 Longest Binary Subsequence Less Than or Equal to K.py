# 2311 Longest Binary Subsequence Less Than or Equal to K.py 
# pattern: Bit Manipulation + Greedy

s = "1001010"
# total zeros = 0000 (4 )
# find the maximum number of ones in result , result <= k
# from last for each one caculate number 
# 1 => 1 << 0  ,  10 =>  1 << 1  , 100 => 1 << 2
print(1<<1) # 2  index 1
print(1<<2) # 4  index 2
print(1<<3) # 8  index 3
# when current number exceeds k, returns total zeros and ones used 
# start from least significant .
result = s.count('0')
current = 0
n = len(s)
k = 5
for i in range(len(s)-1,-1,-1):
    if s[i] == '1':
        current += 1 << (n-1-i)
        if current > k:
            break
        result += 1

print("result" ,result) 

# time = O(n)  space = O(1)


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        result = s.count('0')
        current = 0
        n = len(s)
        for i in range(len(s)-1,-1,-1):
            if s[i] == '1':
                current += 1 << (n-1-i)
                if current > k:
                    break
                result += 1
        
        return result 
        
        
