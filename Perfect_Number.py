n = 8
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        count = 0
        temp = n
        if (-2**(31) <= n <= 0):
            count = 0
        elif (n >= 1):
            while (2**count != n):
                if (temp % 2 != 0):
                    break
                elif (temp == 1 or temp == 1.0):
                    break
                else:
                    temp = temp / 2
                    count += 1
        return 2**count == n
print(Solution().isPowerOfTwo(n))