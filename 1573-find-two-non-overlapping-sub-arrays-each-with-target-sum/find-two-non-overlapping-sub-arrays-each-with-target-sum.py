class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)
        INF = float('inf')

        # best[i] = minimum length of a valid subarray
        # ending at or before index i
        best = [INF] * n

        left = 0
        curr_sum = 0
        ans = INF

        for right in range(n):
            curr_sum += arr[right]

            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            if curr_sum == target:
                length = right - left + 1

                # Previous subarray must end before left
                if left > 0 and best[left - 1] != INF:
                    ans = min(ans, length + best[left - 1])

                best[right] = length
            else:
                best[right] = INF

            # Carry forward the shortest previous subarray
            if right > 0:
                best[right] = min(best[right], best[right - 1])

        return ans if ans != INF else -1