class Solution(object):
    def maximumWealth(self, accounts):
        """
        :type accounts: List[List[int]]
        :rtype: int
        """
        #sum all the accounts for each customer
        #find the max richest each time
        #update the currentRichest and return

        currentRichest = 0;
        for customer in accounts:
             currentRichest = max(currentRichest, sum(customer))

        return currentRichest
