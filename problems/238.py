class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        outputArray = []
        counter = 0
        while counter < (len(nums)):
            total = 1
            for i in range (len(nums)):
                if i != counter:
                    total*= nums[i]
            outputArray.append(total)
            counter += 1

        return outputArray
               """

        length = len(nums)

        #becauses python has no type, create array of 0's of wanted length.
        L, R, answer = [0]*length, [0]*length, [0]*length

        #since no element to the left of index 0, first index is 1
        L[0] = 1
        for i in range(1, length):
            L[i] = nums[i-1]*L[i-1]

        #since no element to the right last index is 1.
        R[length-1] = 1
        for i in reversed(range(length-1)):
            R[i] = nums[i+1]*R[i+1]

        #put in answer
        for i in range(length):
            answer[i] = L[i]*R[i]

        return answer
    #O(1)- constant time, grow to a finite number.
    #O(N)- linear run time, grows linearly with input size n.
    #time complexity: 2 for loops through n, 2n == O(n)
    #space complexity: O(n) the algorithm space grows linearly with input size n.