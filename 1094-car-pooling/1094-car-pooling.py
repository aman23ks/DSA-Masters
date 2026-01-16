
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        data = []
        for trip in trips:
            cap, start, end = trip
            data.append([start, 1, cap])
            data.append([end, 0, cap])

        data = sorted(data)
        for trip in data:
            trip_data, is_entered, cap = trip
            
            if is_entered == 1:
                capacity -= cap
                if capacity < 0:
                    return False
            else:
                capacity += cap

        return True