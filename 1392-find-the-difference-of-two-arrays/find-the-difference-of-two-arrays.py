from collections import Counter
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        n1 = Counter(nums1)
        n2 = Counter(nums2)
        res = []
        n1_li = []
        n2_li = []
        for i in n1.keys():
            if i not in nums2:
                n1_li.append(i)
        for i in n2.keys():
            if i not in nums1:
                n2_li.append(i)
        res.append(n1_li)
        res.append(n2_li)
        return res