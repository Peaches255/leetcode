class Solution {
    //n^2 time complexity two for loops run for n iterations
    //O(1) space coplexity, since doesnt allocate additional space in proportion to the input size.
    
    public int majorityElement(int[] nums) {
         int majorityCount =  nums.length/ 2;

    for(int num : nums){
        int count = 0;
        for(int element : nums){
            if(element == num){
                count+= 1;
            }
        }
        if(count > majorityCount)
            return num;
    }
    return -1;
 }
}