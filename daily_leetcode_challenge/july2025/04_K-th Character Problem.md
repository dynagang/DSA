# K-th Character Problem - Complete Solution Guide

## Problem Statement

Given an integer `k` and an array of operations, we start with a string containing only the character 'a'. We apply operations cyclically:
- **Operation 0**: Copy the current string and append it to itself
- **Operation 1**: Copy the current string, increment each character by 1 (a→b, b→c, ..., z→a), and append it

Find the k-th character (1-indexed) in the final string.

## Problem Analysis

### Example Walkthrough
```
operations = [0, 1, 0, 1, 0, 1, 0], k = 64

Initial: "a"
Step 1 (op[0]=0): "a" + "a" = "aa"
Step 2 (op[1]=1): "aa" + "bb" = "aabb" 
Step 3 (op[2]=0): "aabb" + "aabb" = "aabbaabb"
Step 4 (op[3]=1): "aabbaabb" + "bbccbbcc" = "aabbaabbbbccbbcc"
...and so on
```

The string grows exponentially: 1 → 2 → 4 → 8 → 16 → 32 → 64 → 128...

---

## Solution 1: Brute Force Approach

### Code
```python
def kthCharacter_bruteforce(self, k: int, operations: List[int]) -> str:
    """
    Brute Force: Build the entire string step by step
    Time: O(2^n) where n is number of operations needed
    Space: O(2^n) to store the string
    """
    word = "a"
    op_idx = 0
    
    # Keep building until we have at least k characters
    while len(word) < k:
        if operations[op_idx] == 1:
            # Increment each character
            next_part = ""
            for ch in word:
                next_char = chr((ord(ch) - ord('a') + 1) % 26 + ord('a'))
                next_part += next_char
        else:
            # Copy as-is
            next_part = word
        
        word += next_part
        op_idx = (op_idx + 1) % len(operations)
    
    return word[k-1]
```

### Analysis
- **Time Complexity**: O(2^n) - exponential growth
- **Space Complexity**: O(2^n) - stores entire string
- **Problem**: Too slow for large k values (TLE for k > 1000)

---

## Solution 2: Recursive Binary Tree Approach

### Key Insight
The string grows in a **binary tree pattern**. Each position can be traced back to its origin through recursive calls.

### Visualization
```
                    Level 0: "a"
                       |
                   operation[0]
                       |
                   Level 1: "??"
                   /         \
              original    transformed
                 |             |
             operation[1]      |
                 |             |
             Level 2: "????"
             /    |    |    \
            ??    ??   ??    ??
```

### Code
```python
def kthCharacter_recursive(self, k: int, operations: List[int]) -> str:
    """
    Recursive approach: Work backwards from position k
    Time: O(log k)
    Space: O(log k) for recursion stack
    """
    def find_operations_path(pos, operations):
        """Find which operations affected this position"""
        if pos == 0:
            return []  # Base case: first character 'a'
        
        # Find the step where this position was created
        length = 1
        step = 0
        
        # Find minimum length that contains our position
        while length <= pos:
            length *= 2
            step += 1
        
        # Previous length (before last doubling)
        prev_length = length // 2
        
        # Which operation created this step?
        op_idx = (step - 1) % len(operations)
        operation = operations[op_idx]
        
        if pos < prev_length:
            # Position is in left half (original)
            return find_operations_path(pos, operations)
        else:
            # Position is in right half (transformed)
            original_pos = pos - prev_length
            path = find_operations_path(original_pos, operations)
            path.append(operation)
            return path
    
    # Get the path of operations that affected position k-1 (0-indexed)
    operations_path = find_operations_path(k-1, operations)
    
    # Apply operations to 'a'
    increments = sum(operations_path)  # Count how many times we increment
    
    return chr((ord('a') + increments) % 26)
```

### Step-by-Step Trace for k=64, operations=[0,1,0,1,0,1,0]

```
Position 63 (k-1):

Step 1: pos=63
        length=64, prev_length=32, step=6
        op_idx=(6-1)%7=5, operation=operations[5]=1
        63 ≥ 32? YES → right half
        original_pos = 63-32 = 31
        Add operation 1 to path

Step 2: pos=31  
        length=32, prev_length=16, step=5
        op_idx=(5-1)%7=4, operation=operations[4]=0
        31 ≥ 16? YES → right half
        original_pos = 31-16 = 15
        Add operation 0 to path

Step 3: pos=15
        length=16, prev_length=8, step=4  
        op_idx=(4-1)%7=3, operation=operations[3]=1
        15 ≥ 8? YES → right half
        original_pos = 15-8 = 7
        Add operation 1 to path

Step 4: pos=7
        length=8, prev_length=4, step=3
        op_idx=(3-1)%7=2, operation=operations[2]=0  
        7 ≥ 4? YES → right half
        original_pos = 7-4 = 3
        Add operation 0 to path

Step 5: pos=3
        length=4, prev_length=2, step=2
        op_idx=(2-1)%7=1, operation=operations[1]=1
        3 ≥ 2? YES → right half  
        original_pos = 3-2 = 1
        Add operation 1 to path

Step 6: pos=1
        length=2, prev_length=1, step=1
        op_idx=(1-1)%7=0, operation=operations[0]=0
        1 ≥ 1? YES → right half
        original_pos = 1-1 = 0  
        Add operation 0 to path

Step 7: pos=0 → Base case, return []

Operations path: [0, 1, 0, 1, 0, 1]
Increments = sum([0,1,0,1,0,1]) = 3
Result = chr(ord('a') + 3) = 'd'
```

### Analysis
- **Time Complexity**: O(log k)
- **Space Complexity**: O(log k) for recursion stack
- **Advantage**: Much faster than brute force

---

## Solution 3: Bit Manipulation Approach (Optimal)

### Key Insight
Position k-1 in binary representation directly tells us which operations affected it!

### Binary Position Analysis
```
k = 64 → k-1 = 63
63 in binary = 111111₂

Each bit position corresponds to an operation:
Bit 0 (2^0=1):   operations[0] = 0
Bit 1 (2^1=2):   operations[1] = 1  
Bit 2 (2^2=4):   operations[2] = 0
Bit 3 (2^3=8):   operations[3] = 1
Bit 4 (2^4=16):  operations[4] = 0
Bit 5 (2^5=32):  operations[5] = 1
```

### Code
```python
def kthCharacter(self, k: int, operations: List[int]) -> str:
    """
    Optimal bit manipulation approach
    Time: O(log k)
    Space: O(1)
    """
    k -= 1  # Convert to 0-indexed
    
    bits = k.bit_length()
    # Alternative way to find bits:
    # num = k
    # bits = 0
    # while num:
    #     num //= 2
    #     bits += 1
    
    res = 0
    for i in range(bits):
        if (k >> i) & 1:  # If i-th bit is set
            res += operations[i % len(operations)]
    
    return chr(ord('a') + (res % 26))
```

### Detailed Trace for k=64, operations=[0,1,0,1,0,1,0]

```
k = 64 → k-1 = 63
63 in binary = 111111₂ (6 bits)

For each bit position i from 0 to 5:
i=0: (63 >> 0) & 1 = 63 & 1 = 1 → bit is set
     operations[0 % 7] = operations[0] = 0
     res += 0

i=1: (63 >> 1) & 1 = 31 & 1 = 1 → bit is set  
     operations[1 % 7] = operations[1] = 1
     res += 1 → res = 1

i=2: (63 >> 2) & 1 = 15 & 1 = 1 → bit is set
     operations[2 % 7] = operations[2] = 0  
     res += 0 → res = 1

i=3: (63 >> 3) & 1 = 7 & 1 = 1 → bit is set
     operations[3 % 7] = operations[3] = 1
     res += 1 → res = 2

i=4: (63 >> 4) & 1 = 3 & 1 = 1 → bit is set
     operations[4 % 7] = operations[4] = 0
     res += 0 → res = 2  

i=5: (63 >> 5) & 1 = 1 & 1 = 1 → bit is set
     operations[5 % 7] = operations[5] = 1
     res += 1 → res = 3

Final result: chr(ord('a') + 3) = chr(97 + 3) = chr(100) = 'd'
```

### Why This Works
1. **Binary Representation**: Each bit in k-1 represents a "choice" made during string construction
2. **Operation Mapping**: Bit i corresponds to operations[i % len(operations)]
3. **Direct Calculation**: No recursion needed, just bit manipulation

### Analysis
- **Time Complexity**: O(log k)
- **Space Complexity**: O(1)
- **Advantage**: Most efficient, no recursion overhead

---

## Complete Implementation

```python
import math
from typing import List

class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        """
        Find the k-th character using bit manipulation
        """
        k -= 1  # Convert to 0-indexed
        
        bits = k.bit_length()
        res = 0
        
        for i in range(bits):
            if (k >> i) & 1:
                res += operations[i % len(operations)]
        
        return chr(ord('a') + (res % 26))
```

## Complexity Comparison

| Approach | Time | Space | Notes |
|----------|------|-------|-------|
| Brute Force | O(2^n) | O(2^n) | TLE for large k |
| Recursive | O(log k) | O(log k) | Good but uses stack |
| Bit Manipulation | O(log k) | O(1) | **Optimal** |

## Key Takeaways

1. **Pattern Recognition**: The exponential growth follows a binary tree pattern
2. **Backwards Thinking**: Instead of building forward, trace backwards from target
3. **Bit Manipulation**: Binary representation directly encodes the solution path
4. **Space Optimization**: Avoid storing intermediate results when possible

The bit manipulation approach is the most elegant because it recognizes that the problem structure directly maps to binary representation!
