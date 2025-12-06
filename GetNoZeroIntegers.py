x = 18
class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        temp = x
        summ = 0
        while (temp != 0):
            y = temp % 10
            temp = temp // 10
            summ += y
        if (x % summ == 0):
            return summ
        else:
            return -1
print(Solution().sumOfTheDigitsOfHarshadNumber(x))
