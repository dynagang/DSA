# 3330. Find the Original Typed String I
from collections import Counter
class Solution:
    def possibleStringCount(self, word: str) -> int:
        """

        input : "abbcccc"
        from direct observation .
        entire string 1.
        repeated characters.
        bb two times =>  1 more possible
        cccc four times => 3 more possibles
        1 + 1 + 3 => 5 
        space = O(n) time = O(n + n)
        failed for "ere"  => same character can present in different position.
        so instead of freq use previous element and if same increase count.
        on changing add  count .

        """
        # failed for "ere"
        # result = 1 # the given string itself.
        # freq = Counter(word)
        # for _,count in freq.items():
        #     result += count - 1 if count > 1 else 0         
        # return result 

        # time O(n)  space O(1)
        result = 1
        count  =  0
        for i in range(1,len(word),1):
            if word[i] == word[i-1]:
                count += 1  
            else :
                result += count 
                count = 0

        return result + count  
            
