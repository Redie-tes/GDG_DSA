class Solution:
    def addDigits(self, num: int) -> int:
        f = str(num)
        while len(f) > 1:
            sumtot = 0               
            for i in f:          
                sumtot += int(i)
            f = str(sumtot)     
        return int(f)

     

        
