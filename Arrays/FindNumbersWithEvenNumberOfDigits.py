class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        length = 0

        for i in nums:
            temp = list(str(i))
            if len(temp) % 2 == 0:
                length += 1

        return length