class Solution:
    def swap(self, nums, i, j):
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp

    def removeDuplicates(self, nums):
        offset = len(nums)
        index = 1
        step = 1
        while index < offset:
            step += 1
            if nums[index] == nums[index - 1]:
                num = nums[index]
                nums.append(num)
                nums.pop(index)
                offset -= 1
            else:
                index += 1

        return offset


sol = Solution()

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(nums)
print(sol.removeDuplicates(nums))
print(nums)

nums = [1, 1, 2]
print(sol.removeDuplicates(nums))
print(nums)


nums = [1, 1, 1]
print(sol.removeDuplicates(nums))
print(nums)

nums = [-1, 0, 0, 0, 0, 3, 3]
print(sol.removeDuplicates(nums))
print(nums)
