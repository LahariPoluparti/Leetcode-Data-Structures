class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        if len(arr) == 1:
            return arr

        # finding the number of duplicated zeros
        num_dup = 0
        length = len(arr) - 1

        for i in range(len(arr)):
            if i > length - num_dup:
                break

            if arr[i] == 0:
                if i == length - num_dup:
                    arr[length] = 0
                    length -= 1
                    break
                num_dup += 1

        last = length - num_dup

        for i in range(last, -1, -1):
            if arr[i] == 0:
                arr[i + num_dup] = arr[i]
                num_dup -= 1
                arr[i + num_dup] = arr[i]
            else:
                arr[i + num_dup] = arr[i]

        return arr


