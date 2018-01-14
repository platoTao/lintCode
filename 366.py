class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        if n==1:return 0
        if n==2:return 1
        L=[0,1]
        for i in range(2,n):
            x=L[i-1]+L[i-2]
            L.append(x)
        return L[n-1]