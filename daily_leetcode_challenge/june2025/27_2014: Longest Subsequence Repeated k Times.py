'''
# LeetCode Problem 2014: Longest Subsequence Repeated k Times
Hard

You are given a string s of length n, and an integer k. You are tasked to find the longest subsequence repeated k times in string s.

A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.

A subsequence seq is repeated k times in the string s if seq * k is a subsequence of s, where seq * k represents a string constructed by concatenating seq k times.

For example, "bba" is repeated 2 times in the string "bababcba", because the string "bbabba", constructed by concatenating "bba" 2 times, is a subsequence of the string "bababcba".
Return the longest subsequence repeated k times in string s. If multiple such subsequences are found, return the lexicographically largest one. If there is no such subsequence, return an empty string.

 

Example 1:

example 1
Input: s = "letsleetcode", k = 2
Output: "let"
Explanation: There are two longest subsequences repeated 2 times: "let" and "ete".
"let" is the lexicographically largest one.
Example 2:

Input: s = "bb", k = 2
Output: "b"
Explanation: The longest subsequence repeated 2 times is "b".


'''

from collections import deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        """
        Find the longest subsequence `t` such that `t` repeated `k` times
        is still a subsequence of the input string `s`.

        Strategy:
        1. A character must appear at least `k` times to be used in the answer.
        2. Collect all such characters as `valid_chars`.
        3. Use BFS to explore all combinations of valid characters in increasing length order.
        4. For each candidate subsequence `t`, check if `t * k` is a subsequence of `s`.
        5. Always keep track of the last valid subsequence found.
        6. BFS ensures we get the longest and lexicographically smallest such subsequence.


        time : 
        O(A^L * n)
        A is the number of valid characters (≤ 26)
        L = max length of the result subsequence ≈ n // k
        n is the length of input string
​
        space:
        BFS queue can hold O(A^L) strings
        Each string is of length ≤ L
        So total space: O(A^L * L)

        """

        # Step 1: Count frequency of each character in `s`
        char_counts = [0] * 26
        for ch in s:
            char_counts[ord(ch) - ord('a')] += 1

        # Step 2: Filter characters that appear at least `k` times
        valid_chars = [chr(i + ord('a')) for i in range(26) if char_counts[i] >= k]

        # Step 3: Helper function to check if a candidate repeated `k` times is a subsequence of `s`
        def is_valid(candidate: str) -> bool:
            """
            Check if `candidate * k` is a subsequence of `s`
            """
            target = candidate
            need = k  # how many times we need to match `target`
            i = 0     # index for candidate
            for ch in s:
                if ch == target[i]:
                    i += 1
                    if i == len(target):
                        need -= 1
                        if need == 0:
                            return True
                        i = 0  # reset to start of candidate again
            return False

        # Step 4: BFS to generate valid subsequences in lexicographical order
        ans = ""
        queue = deque([""])  # start with empty string
        while queue:
            curr = queue.popleft()

            # Prune: if current candidate's repeated length exceeds s, we can stop
            if len(curr) * k > len(s):
                continue  # don't break; other shorter branches may still be valid

            for ch in valid_chars:
                new_candidate = curr + ch
                if is_valid(new_candidate):
                    queue.append(new_candidate)
                    ans = new_candidate  # always update to the latest valid one

        return ans
