class RangeModule:
    def __init__(self):
        self.values = []

    def addRange(self, left: int, right: int) -> None:
        while len(self.values) < right:
            self.values.append(False)
        for i in range(left, right):
            self.values[i] = True

    def queryRange(self, left: int, right: int) -> bool:
        if not self.values or len(self.values) < right:
            return False
        for i in range(left, right):
            if not self.values[i]:
                return False
        return True

    def removeRange(self, left: int, right: int) -> None:
        n = min(len(self.values), right)
        for i in range(left, n):
            self.values[i] = False

# Your RangeModule object will be instantiated and called as such:
obj = RangeModule()
print(obj.addRange(10, 20))
print(obj.removeRange(14, 16))
print(obj.queryRange(10, 14))
print(obj.queryRange(13, 15))
print(obj.queryRange(16, 17))
