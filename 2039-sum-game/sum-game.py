class Solution(object):
    def sumGame(self, num):
        """
        :type num: str
        :rtype: bool
        """
        n = len(num)
        s1 = s2 = 0
        c1 = c2 = 0

        for i in range(n // 2):
            if num[i] == '?':
                c1 += 1
            else:
                s1 += int(num[i])

        for i in range(n // 2, n):
            if num[i] == '?':
                c2 += 1
            else:
                s2 += int(num[i])

        if (c1 + c2) % 2 == 1:
            return True

        return s1 - s2 != 9 * (c2 - c1) // 2