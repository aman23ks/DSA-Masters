class RangeModule:

    def __init__(self):
        # This will store the non-overlapping intervals
        self.intervals = []

    def mergeIntervals(self):
        # Merges overlapping intervals
        res = []
        for interval in self.intervals:
            if not res or res[-1][1] < interval[0]:  # No overlap
                res.append(interval)
            else:  # Overlapping intervals
                res[-1][1] = max(res[-1][1], interval[1])  # Merge the intervals
        self.intervals = res

    def addRange(self, left: int, right: int) -> None:
        # Add a new range and merge intervals
        new_intervals = []
        inserted = False

        for interval in self.intervals:
            if interval[1] < left:  # No overlap, current interval is entirely left of the new range
                new_intervals.append(interval)
            elif interval[0] > right:  # No overlap, current interval is entirely right of the new range
                if not inserted:
                    new_intervals.append([left, right])  # Insert the new range
                    inserted = True
                new_intervals.append(interval)
            else:  # Overlapping intervals, merge with the new range
                left = min(left, interval[0])
                right = max(right, interval[1])

        if not inserted:
            new_intervals.append([left, right])  # Add the new range if not already added

        self.intervals = new_intervals
        self.mergeIntervals()

    def queryRange(self, left: int, right: int) -> bool:
        # Check if the range [left, right] is fully covered by any interval
        for interval in self.intervals:
            if interval[0] <= left and interval[1] >= right:
                return True
        return False

    def removeRange(self, left: int, right: int) -> None:
        # Remove the range [left, right] from intervals
        new_intervals = []

        for interval in self.intervals:
            if interval[1] <= left or interval[0] >= right:  # No overlap, keep the interval
                new_intervals.append(interval)
            else:
                if interval[0] < left:
                    new_intervals.append([interval[0], left])  # Split the left part
                if interval[1] > right:
                    new_intervals.append([right, interval[1]])  # Split the right part

        self.intervals = new_intervals
        self.mergeIntervals()