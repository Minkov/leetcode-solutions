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

    # O(N)
    def sum(self, prefix):
        from_index = self.lower_bound(prefix)
        to_index = self.upper_bound(prefix)
        print('*' * 10)
        print(from_index)
        print(to_index)
        print('*' * 10)
        if from_index < 0 or to_index < 0:
            return 0

        result = 0
        for [i, val] in self.values[from_index: to_index + 1]:
            result += val
        return result

    def lower_bound(self, value):
        """Find the index of the first element in sequence >= value"""
        elements = len(self.values)
        offset = 0
        middle = 0
        found = len(self.values)

        while elements > 0:
            middle = elements // 2
            if self.values[offset + middle][0] < value:
                offset = offset + middle + 1
                elements = elements - (middle + 1)
            else:
                found = offset + middle
                elements = middle
        return found

    def upper_bound(self, value):
        """Find the index of the first element in sequence > value"""
        elements = len(self.values)
        offset = 0
        middle = 0
        found = 0

        while elements > 0:
            middle = elements // 2
            if value < self.values[offset + middle][0]:
                elements = middle
            else:
                offset = offset + middle + 1
                found = offset
                elements = elements - (middle + 1)
        return found

    def lower_bound2(self, prefix):
        left = 0
        right = len(self.values)
        while left < right:
            mid = (left + right) // 2
            if self.values[mid][0] < prefix:
                left = mid + 1
            else:
                right = mid

        return right

    def upper_bound2(self, prefix):
        left = 0
        right = len(self.values)
        while left < right:
            mid = (left + right) // 2
            if self.values[mid][0] >= prefix:
                left = mid + 1
            else:
                right = mid

        return left


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

