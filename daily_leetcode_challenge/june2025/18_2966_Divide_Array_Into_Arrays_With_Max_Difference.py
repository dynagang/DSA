# 2966_Divide_Array_Into_Arrays_With_Max_Difference.py
# solution 1:
class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        """
        from output of example1 its clear that the array is sorted .
        but not same for example3.
        example3
        nums = [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11], k = 14
        op = [[2,2,12],[4,8,5],[5,9,7],[7,8,5],[5,9,10],[11,12,2]]
        lets sort nums
        [4,2,9,8,2,12,7,12,10,5,8,5,5,7,9,2,5,11],
        -> [2,2,2 4,5,5, 5,5,7 7,8,8 9,9,10  11,12,12]
            max_diff -> [0 1 2 1 1 1] so any pairs in each [0:3] will less than k=14
        return possible list of lists.

        complexity :
        t =  O(nlogn) + O(n/3)
        if consider the result array s = O(n)
        """
        nums.sort()
        n = len(nums)
        is_valid_group = True
 
        for i in range(0,n,3):
            if abs(nums[i]-nums[i+2]) > k:
                is_valid_group = False
                break

        if not is_valid_group: 
            return []

        return [nums[i:i+3] for i in range(0,n,3)]
    
# solution 2: more readable
# this solution is same as solution1 but more readable.

class Solution2:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        res = []
        for i in range(0, n, 3):
            a, b, c = nums[i], nums[i+1], nums[i+2]
            if c - a > k:
                return []
            res.append([a, b, c])
        return res
