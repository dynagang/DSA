class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
      
        # Sort the array to group similar values together
        nums.sort()
        
        subsequences = 1  # At least one subsequence needed
        min_val = nums[0]  # Track minimum of current subsequence
        
        # Iterate through sorted array
        for i in range(1, len(nums)):
            # If current element can't fit in current subsequence
            if nums[i] - min_val > k:
                # Start a new subsequence
                subsequences += 1
                min_val = nums[i]  # Reset minimum for new subsequence
        
        return subsequences
