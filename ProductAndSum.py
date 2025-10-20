n = int(input())
class Solution:
    def subtractProductAndSum(self, n):
        pro = 1
        summ = 0
        subs = 0
        while (n != 0):
            a = n % 10
            n = n // 10
            pro *= a
            summ += a
        subs = pro - summ
        return subs
print(Solution().subtractProductAndSum(n))  