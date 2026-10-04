from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []
        for start, end in intervals:
            if result and start <= result[-1][1]:
                if end > result[-1][1]:
                    result[-1][1] = end
            else:
                result.append([start, end])
        return result
