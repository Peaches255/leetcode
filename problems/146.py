from collections import OrderedDict
class LRUCache(object):
    #put in O(1) time complexity - linkedList append to the end
    #get in O(1) time complexity - hashmap.
#ordered dict is like a regular map except it remmebers the order in which the elements were added into it.
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.orderedDict = OrderedDict()
        self.capacity = capacity


    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        #if key in Dict - return value and move key to the front of cache.
        #if key not in dict- return -1
        if key in self.orderedDict:
            keyVal = self.orderedDict[key]
            del(self.orderedDict[key])# in an orderedDict when you delete and re-insert will insert at the front.
            self.orderedDict[key]= keyVal
            return keyVal
        else:
            return -1


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        #if key already exists- update value and move it the front.
        #if > capacity - remove the front key pair
        #else add pair

        if key in self.orderedDict:
            #to update val, need to delete and re-insert so will be moved to the front of cache.
            del(self.orderedDict[key])
            self.orderedDict[key] = value
        else: #key is not in orderedDict
            if len(self.orderedDict) >= self.capacity:
                #delete the oldest in cache and add new - will add to the front.
                self.orderedDict.popitem(last = False) # popitem(last = False)- FIFO(not last) popitem(last = True) - (last yes)- LIFO
            self.orderedDict[key] = value




# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
