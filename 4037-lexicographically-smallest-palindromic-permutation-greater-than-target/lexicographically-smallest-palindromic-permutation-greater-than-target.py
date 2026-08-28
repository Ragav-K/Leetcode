class Solution(object):
    def lexPalindromicPermutation(self, s, target):
        """
        :type s: str
        :type target: str
        :rtype: str
        """
        n = len(s)
        cnt = [0] * 26

        for c in s:
            cnt[ord(c) - 97] += 1

        if sum(x % 2 for x in cnt) > 1:
            return ""

        half = [x // 2 for x in cnt]
        mid = ""

        if n % 2:
            for i in range(26):
                if cnt[i] % 2:
                    mid = chr(i + 97)
                    break

        left = []

        for _ in range(n // 2):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                left.append(chr(i + 97))

                rem = []
                for j in range(25, -1, -1):
                    rem.append(chr(j + 97) * half[j])

                l = "".join(left) + "".join(rem)
                p = l + mid + l[::-1]

                if p > target:
                    break

                left.pop()
                half[i] += 1
            else:
                return ""

        l = "".join(left)
        ans = l + mid + l[::-1]

        return ans if ans > target else ""