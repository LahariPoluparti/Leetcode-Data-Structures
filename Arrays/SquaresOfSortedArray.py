class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        nums = []

        i = 0
        j = 0

        while j < len(A) and A[j] < 0:
            j += 1
        i = j - 1

        # both positive and negative
        while j < len(A) and i >= 0:
            if A[j] ** 2 < A[i] ** 2:
                nums.append(A[j] ** 2)
                j += 1
            else:
                nums.append(A[i] ** 2)
                i -= 1

        # all negative
        while i >= 0:
            nums.append(A[i] ** 2)
            i -= 1

        # all positive
        while j < len(A):
            nums.append(A[j] ** 2)
            j += 1

        return nums



