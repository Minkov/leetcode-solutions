import string


class Solution:
    def convertToTitle(self, n: int) -> str:
        if n == 1:
            return 'A'
        n -= 1

        digits = list(string.ascii_uppercase)
        base = len(digits)

        result = []
        while n > 0:
            index = n % base
            digit = digits[index]
            result.append(digit)
            n //= base
        return result


# print(Solution().convertToTitle(1))
print(Solution().convertToTitle(28))
# print(Solution().convertToTitle(701))