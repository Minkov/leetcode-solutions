from queue import PriorityQueue
class Solution:
    def partition(self, froms, tos, total_size):
        queue = PriorityQueue()
        for letter in froms.keys():
            queue.put([froms[letter], letter])

        partitions = [-1] * total_size
        while not queue.empty():
            [_, letter] = queue.get()
            queue.task_done()
            letter_to_fill = letter
            from_index = froms[letter]
            to_index = tos[letter]
            if partitions[from_index] != -1:
                letter_to_fill = partitions[from_index]
            for i in range(from_index, to_index + 1):
                partitions[i] = letter_to_fill
        return partitions

    def partitionLabels(self, S):
        len_s = len(S)
        froms = dict()
        tos = dict()
        for i in range(len_s):
            letter = S[i]
            if S[i] not in froms:
                froms[letter] = i
                tos[letter] = i
            else:
                tos[letter] = i
        partitions = self.partition(froms, tos, len_s)

        index = 1
        last_letter = partitions[0]
        partitions_sizes = [1]

        while index < len(partitions):
            while index < len(partitions) and partitions[index] == last_letter:
                index += 1
                partitions_sizes[-1] += 1
            if index >= len(partitions):
                break
            last_letter = partitions[index]
            partitions_sizes.append(0)
        return partitions_sizes

sol = Solution()
print(sol.partitionLabels("ababcbacadefegdehijhklij"))
print(sol.partitionLabels('a'))
