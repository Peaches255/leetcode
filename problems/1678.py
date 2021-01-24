class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        array = list(command)

        interpretString = ""
        for index in range(len(array)):
            print array[index]
            if array[index] =='G':
                interpretString += 'G'
            elif array[index] == '(' and array[index+1] == ')':
                interpretString += 'o'
            elif array[index] == '(' and array[index+1] == 'a':
                interpretString += "al"
            else:
                continue

        return interpretString
    
