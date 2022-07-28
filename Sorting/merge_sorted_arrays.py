"""
    PROMPT:
            You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
            representing the number of elements in nums1 and nums2 respectively.

            Merge nums1 and nums2 into a single array sorted in non-decreasing order.

            The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
            To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
            and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
            
            Time Complexity:    O(m+n)
            Space Complexity:   O(m)
"""

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        temp = nums1[:m]
        i = j = k = 0
        while (i<m) and (j<n):
            if temp[i] <= nums2[j]:
                nums1[k] = temp[i]
                i += 1
                k += 1
            else:
                nums1[k] = nums2[j]
                j += 1
                k += 1
            
        while (i<m):
            nums1[k] = temp[i]
            i += 1
            k += 1
            
        while (j<n):
            nums1[k] = nums2[j]
            j += 1
            k += 1
