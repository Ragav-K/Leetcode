class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        FAC = {1:(0,0,0,0), 2:(1,0,0,0), 3:(0,1,0,0), 4:(2,0,0,0), 5:(0,0,1,0),
               6:(1,1,0,0), 7:(0,0,0,1), 8:(3,0,0,0), 9:(0,2,0,0)}

        need = [0,0,0,0]
        for i, p in enumerate((2,3,5,7)):
            while t % p == 0:
                t //= p
                need[i] += 1
        if t > 1:
            return "-1"                     

        def minimal_digits(rem):
            """Smallest multiset of digits 2..9 covering rem = [e2,e3,e5,e7]."""
            r2, r3, r5, r7 = rem
            d = [7]*r7 + [5]*r5
            d += [9] * (r3 // 2); r3 %= 2
            d += [8] * (r2 // 3); r2 %= 3
            if r3 and r2:
                d.append(6); r3 -= 1; r2 -= 1
            if r2 == 2: d.append(4)
            elif r2 == 1: d.append(2)
            if r3: d.append(3)
            return sorted(d)

        def rem_after(pre, extra):
            return [max(0, need[i] - pre[i] - extra[i]) for i in range(4)]

        n = len(num)
        pre = [[0,0,0,0]]
        for ch in num:
            c = pre[-1][:]
            if ch != '0':
                f = FAC[int(ch)]
                for i in range(4):
                    c[i] = min(need[i], c[i] + f[i])
            pre.append(c)

        first_zero = num.find('0')
        limit = n - 1 if first_zero == -1 else first_zero

        if first_zero == -1 and all(pre[n][i] >= need[i] for i in range(4)):
            return num

        for i in range(limit, -1, -1):
            k = n - 1 - i
            for d in range(int(num[i]) + 1, 10):
                r = rem_after(pre[i], FAC[d])
                tail = minimal_digits(r)
                if len(tail) <= k:
                    return (num[:i] + str(d) + '1' * (k - len(tail))
                            + ''.join(map(str, tail)))

        tail = minimal_digits(need)
        L = max(n + 1, len(tail))
        return '1' * (L - len(tail)) + ''.join(map(str, tail))