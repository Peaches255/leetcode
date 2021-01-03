class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        #find the max number of candy
        # for each element add extraCandies
        maxNumberOfCandy = 0
        for kid in candies:
            maxNumberOfCandy = max(kid, maxNumberOfCandy)

        output_list = [None]*len(candies)
        for i in range(len(candies)):
            output_list [i] = self.amongGreatestNumberOfCandies( candies[i], extraCandies, maxNumberOfCandy)

        return output_list

    def amongGreatestNumberOfCandies(self, candy, extraCandies,                 maxNumberOfCandy):
        #function among greatest number of candies
        #if >= maxCandy return true
        #else return false

            return candy + extraCandies >= maxNumberOfCandy
