class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        def helper(list1, start1, end1, list2, start2, end2, k):
            l1 = end1 - start1 + 1
            l2 = end2 - start2 + 1
            if l1 < l2:
                list1, list2, l1, l2, start1, start2, end1, end2 = list2, list1, l2, l1, start2, start1, end2, end1
            if l2 == 0:
                return list1[start1+k-1]
            if k == 1:
                return min(list1[start1], list2[start2])
            deta = min(k//2, l2)
            num1 = list1[start1+deta-1]
            num2 = list2[start2+deta-1]
            if num1 > num2:
                return helper(list1, start1, end1, list2, start2+deta, end2, k-deta)
            else:
                return helper(list1, start1+deta, end1, list2, start2, end2, k-deta)
        l1 = len(nums1)
        l2 = len(nums2)
        return (helper(nums1, 0, l1-1, nums2,0, l2-1, (l1+l2+1)//2) + helper(nums1,0, l1-1, nums2,0,l2-1, (l1+l2+2)//2)) / 2