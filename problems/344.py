class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """

        startPointer = 0
        endPointer = len(s)-1

        while (startPointer < endPointer):
            temp = s[startPointer]
            s[startPointer] = s[endPointer]
            s[endPointer] = temp
            startPointer += 1
            endPointer -= 1