class Solution(object):
    def maxNumberOfFamilies(self, n, reservedSeats):
        """
        :type n: int
        :type reservedSeats: List[List[int]]
        :rtype: int
        """
        reserved = {}

        for r, c in reservedSeats:
            if c in (2, 3, 4, 5, 6, 7, 8, 9):
                if r not in reserved:
                    reserved[r] = set()
                reserved[r].add(c)

        ans = (n - len(reserved)) * 2

        for seats in reserved.values():
            count = 0

            if not (seats & {2, 3, 4, 5}):
                count += 1

            if not (seats & {6, 7, 8, 9}):
                count += 1

            if count == 0 and not (seats & {4, 5, 6, 7}):
                count = 1

            ans += count

        return ans