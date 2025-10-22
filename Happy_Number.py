n = 7
class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0
        teams = n
        total_number = 0
        while (teams != 1):
            if (n % 2 == 0):
                matches = n // 2
                teams = n // 2
                n = matches
            elif (n % 2 != 0):
                matches = (n - 1) // 2
                teams = (n - 1)//2 + 1
                n = matches
            total_number += matches
            n = teams
        return total_number
print(Solution().numberOfMatches(n))