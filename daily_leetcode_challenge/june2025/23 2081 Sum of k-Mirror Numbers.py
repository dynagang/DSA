
# solution 1 : brute force approach , (Time Limit Exceeded for large inputs)
class Solution1:

    def is_palindrome(self,k:int,num:int) -> bool:
        """
        check a number is palindrome or not for the given base k
        time complexity = O(log(num) base of log is k. )
        """
        num_copy = num 
        reverse_num = 0
        while num:
            rem = num % k
            reverse_num = reverse_num*k + rem
            num //= k
        return num_copy == reverse_num  


    def kMirror(self, k: int, n: int) -> int:
        """
        brute force:
        consider the palindrome numbers from 1 , and
        check base k is also palindrome then update sum. also reduce n upto 1.
        palindrome check is log(num) base 10 + log(num) base k.
        while n > 0 will run X times .X is the number of candidates
        checked to find n valid k-mirror numbers.
        X >> n, because very few numbers are k-mirrors
        time complexity = O(X(log_10(X)+log_k(X)))
        space = O(1)
        """
        mirror_sum = 0
        num = 1
        while n > 0 :
            # check palindrome for base 10 
            if self.is_palindrome(10,num) and self.is_palindrome(k,num):
                    mirror_sum += num
                    n -= 1
            num += 1
        return mirror_sum
    
# solution 2 : optimized approach using python generator for base 10 palindrome numbers.
class Solution2:

    def is_palindrome(self, k: int, num: int) -> bool:
        """
        Check if a number is a palindrome in base k.
        Time complexity: O(log_k(num))
        """
        num_copy = num
        reverse_num = 0
        while num:
            rem = num % k
            reverse_num = reverse_num * k + rem
            num //= k
        return num_copy == reverse_num  

    def generate_base10_palindromes(self):
        """
        Generator that yields base-10 palindromic numbers in strictly increasing numeric order.

        A palindromic number reads the same forwards and backwards in base-10 (e.g., 121, 12321).

        Strategy:
        - For each digit length `L`, construct palindromes by generating all possible "half parts"
        (the first ⌈L/2⌉ digits) and mirroring them to form the full number.
        - For even `L`: mirror the entire half (e.g., '123' → '123321').
        - For odd `L`: mirror the half excluding its last digit (e.g., '123' → '12321').

        Yields:
        - Single-digit palindromes: 1, 2, ..., 9
        - Two-digit palindromes: 11, 22, ..., 99
        - Three-digit palindromes: 101, 111, ..., 999
        - And so on, indefinitely.

        Properties:
        - Produces palindromes in strictly increasing order without duplicates.
        - Avoids checking non-palindromes for efficiency.
        Time complexity: O(L) per palindrome, where L is the number of digits, due to string
            construction and conversion.
        Space complexity: O(1) for generator state; O(L) temporary space for string operations
            per yielded number.
        """
        length = 1
        while True:
            # Half-length loop
            for half in range(10**((length - 1) // 2), 10**((length + 1) // 2)):
                s = str(half)
                if length % 2 == 0:
                    full = s + s[::-1]       # Even-length
                else:
                    full = s + s[-2::-1]     # Odd-length
                yield int(full)
            length += 1


    def kMirror(self, k: int, n: int) -> int:
        """
        Time Complexity:
        Let:
        - `n` = number of k-mirror numbers to find
        - `X` = number of base-10 palindromes generated to
        find `n` valid k-mirror numbers
        This solution only checks numbers that are already palindromes
        in base-10,which reduces the candidate space significantly 
        compared to brute-force.
        For each candidate:
        - Checking base-k palindrome takes O(log_k num)
        So total time complexity:
            ✅ O(X * log_k num) ≈ O(X * log_k X)
        Where:
        - `X` is usually slightly greater than `n`
        - Much smaller than brute-force (which checks every integer)
        """
        mirror_sum = 0
        count = 0
        for num in self.generate_base10_palindromes():
            if self.is_palindrome(k, num):
                mirror_sum += num
                count += 1
                if count == n:
                    break
        return mirror_sum







"""
❌ Naive Check (Inefficient)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

n = 0
found = 0
while found < 20:
    if is_palindrome(n):
        print(n, end=" ")
        found += 1
    n += 1

* **Drawback**: Time complexity is `O(x)` for finding `n` palindromes.
* `x >> n` → wasteful for large values of `n`.


✅ Optimized Solution: Palindrome Construction Using Generators

 Strategy: Build palindromes from half-string digits.

Let "i" be the half of the palindrome:
    - Odd-length:   s + s[-2::-1]
    - Even-length:  s + s[::-1]


This gives **guaranteed palindromes**, in increasing order, without checking each number.
"""

# 📦 Code Implementation

# 🔁 Full Palindrome Generator (Odd + Even Interleaved)

def digit_length_palindrome_generator():
    i = 1
    while True:
        s = str(i)
        yield int(s + s[-2::-1])  # Odd-length
        yield int(s + s[::-1])    # Even-length
        i += 1


# Example Usage

print("Palindrome Generator Using Digit Length")
count = 0
for n in digit_length_palindrome_generator():
    print(n, end=" ")
    count += 1
    if count == 22: break


# 🔁  Odd-Length Palindromes Only

def odd_length_palindrome_generator():
    i = 1
    while True:
        s = str(i)
        yield int(s + s[-2::-1])
        i += 1


print("First 21 Odd-Length Palindromes")
for i, n in enumerate(odd_length_palindrome_generator()):
    print(n, end=" ")
    if i == 21: break


# 🔁 Even-Length Palindromes Only

def even_length_palindrome_generator():
    i = 1
    while True:
        s = str(i)
        yield int(s + s[::-1])
        i += 1

print("First 21 Even-Length Palindromes")
for i, n in enumerate(even_length_palindrome_generator()):
    print(n, end=" ")
    if i == 21: break


# 🔁 Increasing Order Palindrome Generator by Digit Length

def generate_base10_palindromes():
    length = 1
    while True:
        start = 10 ** ((length - 1) // 2)
        end = 10 ** ((length + 1) // 2)
        for half in range(start, end):
            s = str(half)
            if length % 2 == 0:
                yield int(s + s[::-1])
            else:
                yield int(s + s[-2::-1])
        length += 1


