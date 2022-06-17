# 1. merge two array 
# 2. sort array
# 3. if no of elements in array is even then sum of numbers divide by length of array
# 4. if no of elements in array is odd then index = (length of array + 1)/ 2 and array[index]

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
            m1 = int((len_arr/2) - 1 )
            m2 = int(len_arr/2) 
            median = (float(total_arr[m1]+ total_arr[m2] ) /2 )
            
        else:
            index = int(( len_arr + 1 ) / 2 - 1)
            median = float(total_arr[index])
        return median
            
        
