class Solution:
    def calc_distances(self, from_index, to_index, update, S, C):
        len_s = len(S)
        infinity = 1 << 15
        distances = [infinity] * len_s
        index = from_index
        while index != to_index and S[index] != C:
            index += update
        distances[index] = 0
        while index != to_index:
            if S[index] == C:
                distances[index] = 0
            else:
                distances[index] = distances[index - update] + 1
            index += update
        return distances

    def shortestToChar(self, S, C):
        len_s = len(S)
        right = self.calc_distances(0, len_s, +1, S, C)
        left = self.calc_distances(len_s - 1, -1, -1, S, C)
        result = []
        for i in range(len_s):
            result.append(min(left[i], right[i]))
        return result

sol = Solution()
print(sol.shortestToChar("loveleetcode", "e"))
