class Solution:
    # @param {int[]} A an integer array
    # @return nothing
    def sortIntegers(self, A):
        # Write your code here
        for i in range(0,len(A)):
            for j in range(0,len(A)-1-i):
                if A[j]>A[j+1]:
                     A[j],A[j+1]=A[j+1],A[j]