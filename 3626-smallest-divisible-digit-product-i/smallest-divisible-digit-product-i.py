class Solution(object):
    def smallestNumber(self, n, t):
        """
        :type n: int
        :type t: int
        :rtype: int
        """
        isCorrect = False
        while isCorrect != True:
            prod = 1
            c = n
            while c != 0:
                prod *= c%10
                c //= 10
            if prod % t == 0:
                isCorrect = True
            else:
                n += 1
        return n