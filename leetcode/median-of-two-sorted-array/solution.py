class Solution:
    def merge(self, nums1, nums2):
        index_nums1 = 0
        index_nums2 = 0
        result = []

        while index_nums1 < len(nums1) and index_nums2 < len(nums2):
            num1 = nums1[index_nums1]
            num2 = nums2[index_nums2]
            if num1 < num2:
                result.append(num1)
                index_nums1 += 1
            else:
                result.append(num2)
                index_nums2 += 1
        while index_nums1 < len(nums1):
            result.append(nums1[index_nums1])
            index_nums1 += 1
        while index_nums2 < len(nums2):
            result.append(nums2[index_nums2])
            index_nums2 += 1
        return result

    def findMedianSortedArrays(self, nums1, nums2):
        merged = self.merge(nums1, nums2)
        print(merged)
        if len(merged) is 0:
            return 0.0
        middle_index = len(merged) // 2
        if len(merged) % 2 is 0:
            return (merged[middle_index] + merged[middle_index 2- 1]) / 2.0

        return merged[middle_index] * 1.0

sol = Solution()

print(sol.findMedianSortedArrays( [1, 3], [2]))
print(sol.findMedianSortedArrays( [1, 2], [3, 4]))
