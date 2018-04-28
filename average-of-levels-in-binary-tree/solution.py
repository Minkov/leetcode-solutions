class Solution:
    def calc_average(self, node, depth, counts):
        if node is None:
            return
        if depth not in counts:
            counts[depth] = []
        counts[depth].append(depth)
        self.calc_average(node.left, depth + 1, counts)
        self.calc_average(node.right, depth + 1, counts)

    def averageOfLevels(self, root):
        counts = dict()
        self.calc_average(root, 0, counts)
        counts = [sum(level) / len(level) for _, level in counts.items()]
        return counts
