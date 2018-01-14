class Solution:
    # @param {string} A a string
    # @param {string} B a string
    # @return {boolean} a boolean
    def stringPermutation(self, A, B):
        # Write your code here
        L1=[]
        L2=[]
        for i in A:
            L1.append(i)
        for i in B:
            L2.append(i)
        L2.sort()
        L1.sort()
        if L1==L2:
            return True
        else:
            return False