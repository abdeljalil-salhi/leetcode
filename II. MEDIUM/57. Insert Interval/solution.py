class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        ans, n, i = [], len(intervals), 0

        # Add all intervals that come before the new interval
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        # Merge all overlapping intervals
        while i < n and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        ans.append(newInterval)

        # Add all intervals that come after the new interval
        while i < n:
            ans.append(intervals[i])
            i += 1

        return ans
