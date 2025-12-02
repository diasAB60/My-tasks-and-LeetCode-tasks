n = 10
class Solution:
    def totalMoney(self, n: int) -> int:
        total_money = 0
        week = 1
        dollar = 1
        for i in range(1, n + 1):
            total_money += dollar
            dollar += 1
            if (i % 7 == 0):
                week += 1
                dollar = week
        return total_money
print(Solution().totalMoney(n))