# 2040. Kth Smallest Product of Two Sorted Arrays
class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        """
        brute force:
            in constraints given that  nums1 and nums2 are sorted.
            for nums1[i] negative then travel reverse in nums2
            for getting min product.
            otherwise forward traversal .
            calculate product k times. kth product will be answer

            failed:
            nums1 = [-2,-1,0,1,2]
            nums2 =[-3,-1,2,4,5] will not work when nums2 
            contain negative , and also not handled 0
        """
        # length_n2 = len(nums2)
        # for n1 in nums1:
        #     if n1 < 0 :
        #         for i in range(length_n2-1,-1,-1):
        #             if k == 1: 
        #                 return n1*nums2[i]
        #             k -= 1 
        #     else:
        #         for n2 in nums2:
        #             if k == 1:
        #                 return n1 * n2
        #             k -= 1
        """
        brute force 2 :
        generate all possible products and sort .
        TLE.
        tc = O(N∗M∗Log(N∗M))
        """
        # products = []
        # for n1 in nums1:
        #     for n2 in nums2:
        #         products.append(n1*n2)
        
        # products.sort()
        # return products[k-1]

        """
        optimal approach: binary search.
        (pattern : binray search on answer 
         level: hard.
        )
        Step 1: Understand the Search Space
        Possible products can range from -10^10 to 10^10 
        (because elements are up to ±1e5).

        Instead of generating all products, binary search the product values.

        Step 2: Binary Search on Product Value
        We do binary search on the value space [-1e10, 1e10] to find the
        smallest value x such that there are at least k products ≤ x.

        Step 3: countLE(x) — Count Products ≤ x
        For each element a in nums1, determine how many elements 
        b in nums2 produce a * b ≤ x.
        This depends on the sign of a:

        Case A: a > 0
        a * b is increasing as b increases.
        Use binary search on nums2 to find largest j 
        such that a * nums2[j] ≤ x.

        Case B: a < 0
        a * b is decreasing as b increases.
        Use binary search on nums2 to find smallest j 
        such that a * nums2[j] ≤ x.

        Case C: a == 0
        All products are 0.
        If x >= 0: add len(nums2) (all products are ≤ x)
        If x < 0: add 0

        This is a classic "binary search on answer" pattern.

        """
        def countLessOrEqualTo(targetProduct: int) -> int:
            count = 0
            for num in nums1:
                if num < 0:
                    # Binary search nums2 from right to left
                    left, right = 0, len(nums2) - 1
                    while left <= right:
                        mid = (left + right) // 2
                        if num * nums2[mid] <= targetProduct:
                            right = mid - 1
                        else:
                            left = mid + 1
                    count += len(nums2) - left  # all j >= left satisfy
                elif num > 0:
                    # Binary search nums2 from left to right
                    left, right = 0, len(nums2) - 1
                    while left <= right:
                        mid = (left + right) // 2
                        if num * nums2[mid] <= targetProduct:
                            left = mid + 1
                        else:
                            right = mid - 1
                    count += left  # all j < left satisfy
                else:  # num == 0
                    if targetProduct >= 0:
                        count += len(nums2)  # all zeros result in 0 <= x
                    # else: zero products > targetProduct if targetProduct < 0 → no contribution
            return count

        # Binary search over possible product values
        low, high = -10**10, 10**10
        result = 0
        while low <= high:
            mid = (low + high) // 2
            if countLessOrEqualTo(mid) >= k:
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
  
'''
cpp code that pass all test cases.
class Solution {
public:
    long long countLessOrEqualTo(const vector<int>& nums1, const vector<int>& nums2, long long target) {
        long long count = 0;
        for (int a : nums1) {
            if (a > 0) {
                // Find number of b such that a * b <= target
                long long left = 0, right = nums2.size() - 1, pos = -1;
                while (left <= right) {
                    long long mid = (left + right) / 2;
                    if ((long long)a * nums2[mid] <= target) {
                        pos = mid;
                        left = mid + 1;
                    } else {
                        right = mid - 1;
                    }
                }
                if (pos != -1)
                    count += pos + 1;
            } else if (a < 0) {
                // Since a < 0, nums2[mid] should be large enough
                long long left = 0, right = nums2.size() - 1, pos = nums2.size();
                while (left <= right) {
                    long long mid = (left + right) / 2;
                    if ((long long)a * nums2[mid] <= target) {
                        pos = mid;
                        right = mid - 1;
                    } else {
                        left = mid + 1;
                    }
                }
                count += nums2.size() - pos;
            } else {
                if (target >= 0) {
                    count += nums2.size();  // 0 * b <= target if target >= 0
                }
                // else: 0 * b > target when target < 0 → no contribution
            }
        }
        return count;
    }

    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {

        long long low = -1e10, high = 1e10, ans = 0;
        while (low <= high) {
            long long mid = (low + high) / 2;
            if (countLessOrEqualTo(nums1, nums2, mid) >= k) {
                ans = mid;
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return ans;
    }
};


'''
