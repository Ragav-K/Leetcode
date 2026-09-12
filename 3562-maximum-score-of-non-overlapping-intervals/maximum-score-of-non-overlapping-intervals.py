class Solution(object):
    def maximumWeight(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        n = len(intervals)

        # Keep original indices
        arr = sorted(
            [(l, r, w, i) for i, (l, r, w) in enumerate(intervals)],
            key=lambda x: x[0]
        )

        # dp[i][k] = (maximum score, selected original indices)
        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(n - 1, -1, -1):
            l, r, w, idx = arr[i]

            # Find first interval with start > r
            left, right = i + 1, n
            while left < right:
                mid = (left + right) // 2

                if arr[mid][0] > r:
                    right = mid
                else:
                    left = mid + 1

            next_i = left

            for k in range(5):
                # Skip current interval
                skip = dp[i + 1][k]

                # Take current interval
                if k > 0:
                    take_score = w + dp[next_i][k - 1][0]
                    take_indices = sorted(
                        [idx] + dp[next_i][k - 1][1]
                    )
                    take = (take_score, take_indices)
                else:
                    take = (-1, [])

                # Maximize score, then lexicographically smallest indices
                if take[0] > skip[0]:
                    dp[i][k] = take
                elif take[0] < skip[0]:
                    dp[i][k] = skip
                else:
                    dp[i][k] = min(take, skip, key=lambda x: x[1])

        return dp[0][4][1]