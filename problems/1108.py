class Solution(object):
    def defangIPaddr(self, address):
        """
        :type address: str
        :rtype: str
        """
        newString = []


        for i in range (len(address)):
            if address[i] == '.':
                newString.append('[.]')
            else:
                newString.append(address[i])

        string = "".join(newString)

        return string