
# 2200. Find All K-Distant Indices in an Array

class Solution1:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
            brute force.
            1. we need indices of key in nums. key_idx = []
            2. for each index check condition |i-key_idx[]| <= k.
            3. if works then add all statisfying key_idx's to result.
            tc = O(n*m) where n = len(nums) and m = len(key_idx)
            sc = O(m) (avoiding result array)
        """
        key_idx = []
        for i, num in enumerate(nums):
            if num == key:
                key_idx.append(i)

        result = []
        for i, num in enumerate(nums):
            for idx in key_idx:
                if abs(i-idx) <= k:
                    result.append(i)
                    break

        return result
    
# solution 2 : optimized approach using two pointers.
class Solution2:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        """
            optimized using 2 pointer approach
            For each key match at index j, you directly 
            include [j-k, j+k] into the result (bounded)
            tc = O(n)
            sc = O(1) (avoiding result array)
        """

        result = []
        n = len(nums)
        right = -1 # so for next key position can may have minimum left = right + 1 . 
        for j in range(n):
            if nums[j] == key :
                # left = j-k , it may be go out of left. 
                # left = max(0,j-k) also add duplicate i if key are adjacents. 
                # so index for left start from the next of right of previous key.
                left = max(right+1,j-k)
                # right = j + k , it may go beyond right . last index = n -1. 
                right = min(n-1,j+k)
                # all indices from left to right satisfy |i-j|<= k
                for i in range(left,right+1):
                    result.append(i)
                
        return result

        
