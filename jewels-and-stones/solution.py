class Solution:
    def numJewelsInStones(self, J, S):
        jewels = sorted(J)
        stones = sorted(S)
        len_stones = len(stones)

        count = 0
        index_stones = 0

        for jewel in jewels:
            while index_stones < len_stones and stones[index_stones] < jewel:
                index_stones += 1
            while index_stones < len_stones and jewel == stones[index_stones]:
                count += 1
                index_stones += 1
        return count


sol = Solution()
print(sol.numJewelsInStones("aA", "aAAbbbb"))
print(sol.numJewelsInStones("z", "ZZ"))
print(sol.numJewelsInStones("bcd", "cba"))
print('-' * 5)
print(sol.numJewelsInStones("bce", "eea"))
