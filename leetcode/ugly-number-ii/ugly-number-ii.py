from heapq import heappop, heappush


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = []
        h = [1]
        used = set()
        for _ in range(n):
            x = heappop(h)
            while x in used:
                x = heappop(h)
            ugly.append(x)
            used.add(x)
            heappush(h, x * 2)
            heappush(h, x * 3)
            heappush(h, x * 5)
        return ugly[n-1]


print(Solution().nthUglyNumber(10))
print(Solution().nthUglyNumber(1))
print(Solution().nthUglyNumber(2))
print(Solution().nthUglyNumber(3))