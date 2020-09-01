class Solution(object):
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        time = ''
        A.sort(reverse=True)

        hourDigit1 = []
        hourDigit2 = []
        minuteDigit1 = []
        minuteDigit2 = []
        
        for i in A:
            if i <= 2:
                hourDigit1.append(i)
            if i < 6:
                minuteDigit1.append(i)
                
            minuteDigit2.append(i)
        
        if (0 not in A) and (1 not in A):
            for i in A:
                if i < 4:
                    hourDigit2.append(i)
        else:
            hourDigit2 = A[:]
        
        if (not hourDigit1) or (not hourDigit2) or (not minuteDigit1) or (not minuteDigit2):
            return ''
        
        hourDigit1Copy = hourDigit1[:]
        hourDigit2Copy = hourDigit2[:]
        minuteDigit1Copy = minuteDigit1[:]
        minuteDigit2Copy = minuteDigit2[:]
        
        for i in hourDigit1:
            time = time + str(i)
            
            if i in hourDigit2Copy: hourDigit2Copy.remove(i)
            if i in minuteDigit1Copy: minuteDigit1Copy.remove(i)
            if i in minuteDigit2Copy: minuteDigit2Copy.remove(i)
                    
            if i == 2:
                for j in hourDigit2Copy[:]:
                    if j >= 4:
                        hourDigit2Copy.remove(j)
            
            if not hourDigit2Copy:
                time = ''
                hourDigit1Copy = hourDigit1[:]
                hourDigit2Copy = hourDigit2[:]
                minuteDigit1Copy = minuteDigit1[:]
                minuteDigit2Copy = minuteDigit2[:]
                continue
            else:
                hourDigit = hourDigit2Copy[0]
                time = time + str(hourDigit)
                if hourDigit in minuteDigit1Copy: minuteDigit1Copy.remove(hourDigit)
                if hourDigit in minuteDigit2Copy: minuteDigit2Copy.remove(hourDigit)
                    
            time = time + ':'

            if not minuteDigit1Copy:
                time = ''
                hourDigit1Copy = hourDigit1[:]
                hourDigit2Copy = hourDigit2[:]
                minuteDigit1Copy = minuteDigit1[:]
                minuteDigit2Copy = minuteDigit2[:]
                continue
            else:
                minuteDigit = minuteDigit1Copy[0]
                time = time + str(minuteDigit)
                if minuteDigit in minuteDigit2Copy: minuteDigit2Copy.remove(minuteDigit)

            time = time + str(minuteDigit2Copy[0])
            break
        
        return time
        
