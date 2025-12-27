class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        f = str(n)
        prod = 1
        sum = 0
        for i in f:
            prod *=int(i)
            sum +=int(i)
        return prod - sum

       
               
