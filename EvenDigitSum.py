num = 1000
class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        a = 0
        b = 0
        c = 0
        d = 0
        sum = 0
        if (num < 10):
            for i in range(1, num + 1):
                if (i % 2 == 0):
                    count += 1
        elif (10 <= num < 100):
            for i in range(1, num + 1):
                a = i // 10
                b = i % 10
                sum = a + b
                if (sum % 2 == 0):
                    count += 1
        elif (100 <= num < 1000):
            for i in range(1, num + 1):
                a = i // 100
                b = i // 10 % 10
                c = i % 10
                sum = a + b + c
                if (sum % 2 == 0):
                    count += 1
        elif (num == 1000):
            for i in range(1, 1000):
                a = i // 1000
                b = i // 100 % 10
                c = i % 100 // 10
                d = i % 10
                sum = a + b + c + d
                if (sum % 2 == 0):
                    count += 1
        return count
print(Solution().countEven(num))