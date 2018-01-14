class Solution:
    # @param {int} num a non-negative integer
    # @return {int} one digit
    def addDigits(self, num):
        # Write your code here
        if num<10:
            return num
        i=10
        s=num
        while(s>=10):
            sum=0
            while(num!=0):
                sum=sum+num%i
                num=num/10
            s=sum
            num=sum
        return s