class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in nums2:
            for j in range(0, m):

                if m > len(nums1) - 1:
                    break

                if i < nums1[j]:
                    while (j < m):
                        nums1[m] = nums1[m - 1]
                        m -= 1

                    nums1[m] = i
                    n -= 1
                    j += 1
                    m = len(nums1) - n
                    break

        num = len(nums2)
        index = num - n
        if n != 0:
            nums1[m:] = nums2[index:]
