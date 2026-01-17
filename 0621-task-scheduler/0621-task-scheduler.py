import heapq
from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        # Create a max-heap by using negative values
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        
        time = 0
        queue = []
        
        while maxHeap or queue:
            # If the task in the queue is ready to be processed (cooldown is over)
            if queue and queue[0][1] == time:
                val = queue.pop(0)  # Pop the task that has finished its cooldown
                heapq.heappush(maxHeap, val[0])  # Push the task back into the max-heap
            
            # If there are tasks in the max-heap, process the one with the highest frequency
            if maxHeap:
                val = heapq.heappop(maxHeap)  # Get the task with the highest frequency (most negative)
                if val + 1 != 0:  # If there are still occurrences of the task left
                    # Add the task to the queue with the time it will be available again (time + n + 1)
                    queue.append((val + 1, time + n + 1))
            
            time += 1  # Increase time after each round
        
        return time