# 1. merge two array 
# 2. sort array
# 3. if no of elements in array is even then sum of numbers divide by length of array
# 4. if no of elements in array is odd then (length of array + 1)/ 2 
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        total_arr = nums1 + nums2
        total_arr.sort()
        len_arr = len(total_arr)
        if len_arr % 2 == 0:
            median = sum(total_arr)/len_arr
        else:
            median = ( len_arr + 1 ) / 2
            
        
        return median
