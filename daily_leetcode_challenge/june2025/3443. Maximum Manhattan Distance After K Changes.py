from collections import Counter
class Solution:
    """
    Manhattan Distance = |north - south| + |east - west|
    Each bad direction (i.e., one that cancels another) can be flipped 
    to a direction that increases the net difference.
    Every change can help increase either the |N-S| or |E-W| value by at most 2.
    max_possible_distance = original_distance + 2 * k
    At step i, you’ve only made i + 1 moves.
    So, Manhattan distance can’t exceed i + 1.
    at step i, max possible distance:
        min(original_distance + 2 * k, i + 1)
        At each step i, track direction counts:
        distance = |N - S| + |W - E|
        max_distance = max(max_distance, min(distance + 2 * k, i + 1))
    """
    def maxDistance(self, s: str, k: int) -> int:
        max_distance = 0
        d_count = Counter()
        for i,d in enumerate(s):
            d_count[d] += 1
            distance = abs(d_count["N"]-d_count["S"])+ abs(d_count["W"]-d_count["E"])
            max_distance = max(max_distance,min(distance + 2 * k , i + 1 ))
        
        return max_distance

            
