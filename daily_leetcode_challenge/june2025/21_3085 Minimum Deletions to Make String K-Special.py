from collections import Counter
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        """
            identify the relation for min.
            count all characters frequency .
            freq = Counter(word)

            aabcaba k = 0
            
            a:4 b:2 c:1

            1 2 4 

            task is it find the character which present in the answer with minimum count, 
            that is not deleted in the actual string .
            here (k=0)
            if c = 1 then all other are 1 so  4 deletion
            if b = 2 then all other are 2 so 3 deletion -> delete 2 a and 1 c
            if a = 4 then all other are 4 so 3 deletion -> delete 2 b and 1 c
             
            try brute force 
        """
        freq = Counter(word)
        min_delete_cnt = float('inf')
        # the one character cnt will not change in answer and that will be the min in answer
        # for the min delete
        for unchanged_ch,unchanged_cnt in freq.items():
            delete_cnt = 0
            for ch,cnt in freq.items():
                if ch == unchanged_ch : continue
                if cnt < unchanged_cnt:
                    delete_cnt += cnt
                elif cnt > (unchanged_cnt + k):
                    delete_cnt += cnt - unchanged_cnt - k
            min_delete_cnt = min(min_delete_cnt,delete_cnt)
        return min_delete_cnt

"""
speedy solution : same logic
class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        A = Counter(word).values()
        res = inf
        
        for x in A:
            cur = 0
            for a in A:
                cur += a if a < x else max(0, a - (x + k))
            res = min(res, cur)
        
        return res

"""
