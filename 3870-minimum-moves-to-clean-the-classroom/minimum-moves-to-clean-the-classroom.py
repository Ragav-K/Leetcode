from collections import deque

class Solution(object):
    def minMoves(self, classroom, energy):
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        sr = sc = 0

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    sr, sc = r, c
                elif classroom[r][c] == 'L':
                    litter[(r, c)] = len(litter)

        k = len(litter)

        if k == 0:
            return 0

        full = (1 << k) - 1

        # (row, col, energy, mask)
        q = deque([(sr, sc, energy, 0)])

        # For each (position, mask), store maximum energy seen
        best = {}

        best[(sr, sc, 0)] = energy

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        moves = 0

        while q:

            for _ in range(len(q)):
                r, c, e, mask = q.popleft()

                if mask == full:
                    return moves

                for dr, dc in directions:
                    nr = r + dr
                    nc = c + dc

                    # Outside classroom
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Wall
                    if classroom[nr][nc] == 'X':
                        continue

                    # Need energy to move
                    if e == 0:
                        continue

                    ne = e - 1
                    nmask = mask

                    # Recharge
                    if classroom[nr][nc] == 'R':
                        ne = energy

                    # Collect litter
                    if classroom[nr][nc] == 'L':
                        idx = litter[(nr, nc)]
                        nmask |= (1 << idx)

                    key = (nr, nc, nmask)

                    # Only keep this state if it gives us MORE energy
                    if key not in best or ne > best[key]:
                        best[key] = ne
                        q.append((nr, nc, ne, nmask))

            moves += 1

        return -1