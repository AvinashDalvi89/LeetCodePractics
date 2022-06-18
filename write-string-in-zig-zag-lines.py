#The string "PAYPALISHIRING" should be "PAHNAPLSIIGYIR"
# P   A   H   N
# A P L S I I G
# Y   I   R
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = len(s)
        step = 2*numRows-2
        slist = []
        for i in range(0,n,5):
            print(i)
        for i in range(numRows):
            for j in range(i,n,step):
                slist.append(s[j])
            #print(slist)
                if i != numRows-1 and i != 0 and j+step-2*i < n:
                    slist.append(s[j+step-2*i])             
        final_str = ''.join(slist)
        return final_str
            
