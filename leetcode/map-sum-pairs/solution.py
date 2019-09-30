class MapSum:
    def __init__(self):
        self.values = []
    """
    O(N)
    """

    def insert(self, key, val):
        index = self.lower_bound(key)

        if index < len(self.values) and self.values[index][0] == key:
            self.values[index] = [key, val]
        else:
            self.values.insert(index, [key, val])
        print(key, self.values)

    # O(N)
    def sum(self, prefix):
        from_index = self.lower_bound(prefix)
        to_index = self.upper_bound(prefix)
        if from_index < 0 or to_index < 0:
            return 0

        result = 0
        for [i, val] in self.values[from_index: to_index]:
            if i.startswith(prefix):
                result += val
        return result

    def lower_bound(self, value):
        for i in range(0, len(self.values)):
            if self.values[i][0].startswith(value):
                return i
            elif value < self.values[i][0]:
                return  i + 1
        return len(self.values)

    def upper_bound(self, value):
        for i in range(len(self.values) - 1, -1, -1):
            if self.values[i][0].startswith(value):
                return i + 1
            elif value > self.values[i][0]:
                return i + 1

        print("upper: 0")
        return len(self.values)


sol = MapSum()
sol.insert("a", 3)
print(sol.sum("ap"))
sol.insert("b", 2)
print(sol.sum("a"))

print('-' * 30)

sol = MapSum()
sol.insert("apple", 3)
print(sol.sum("ap"))
sol.insert("app", 2)
print(sol.sum("ap"))

