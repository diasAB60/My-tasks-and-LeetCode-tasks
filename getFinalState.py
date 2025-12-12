n = 115
class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = str(n)
        count = 0
        array = []
        digit = 0
        for i in range(len(s)):
            array.append(int(s[i]))

        nums = []
        min_freq = len(array)
        frequent_digit = max(array)

        for i in range(len(array)):
            for j in range(len(array)):
                if (i == j):
                    continue
                if (s[i] == s[j]):
                    count += 1
            if (count < min_freq):
                min_freq = count
                digit = int(s[i])
                if (digit <= frequent_digit):
                    frequent_digit = digit
                elif (digit >= frequent_digit):
                    frequent_digit = digit
            elif (count <= min_freq):
                min_freq = count
                digit = int(s[i])
                if (digit <= frequent_digit):
                    frequent_digit = digit
            count = 0
        return frequent_digit
print(Solution().getLeastFrequentDigit(n))