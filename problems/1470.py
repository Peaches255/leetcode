class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        alternateArray = [None]*len(nums)
        firstHalf = []
        for i in range(0, n):
            firstHalf.append(nums[i])

        secondHalf = []
        for i in range(n, 2*n):
            secondHalf.append(nums[i])

        firstHalfIndex = 0
        secondHalfIndex = 0

        for index in range(0,2*n):
            if index % 2 == 0:
                alternateArray[index] = firstHalf[firstHalfIndex]
                firstHalfIndex += 1
            else:
                alternateArray[index] = secondHalf[secondHalfIndex]
                secondHalfIndex += 1

        return alternateArray
