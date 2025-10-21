left = 47
right = 85
class Solution:
    def selfDividingNumbers(self, left, right):
        a = 0
        b = 0
        c = 0
        d = 0        
        result = []
        for i in range(left, right + 1):
            a = i // 1000 
            b = i // 100 % 10
            c = i // 10 % 10
            d = i % 10
            if (a == 0 and b == 0 and c == 0 and d > 0):
                if (i % d == 0):                        
                    result.append(i)
            elif (a == 0 and b == 0 and c > 0 and d > 0):
                if (i % c == 0 and i % d == 0):
                    result.append(i)
            elif (a == 0 and b > 0 and c > 0 and d > 0):
                if (i % b == 0 and i % c == 0 and i % d == 0):
                    result.append(i)
            elif (a > 0 and b > 0 and c > 0 and d > 0):
                if (i % a == 0 and i % b == 0 and i % c == 0 and i % d == 0):
                    result.append(i)
        return result
print(Solution().selfDividingNumbers(left, right))