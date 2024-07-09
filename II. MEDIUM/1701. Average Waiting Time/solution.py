class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        total_time = current_time = 0

        for arrival, time in customers:
            current_time = max(current_time, arrival) + time
            total_time += current_time - arrival

        return total_time / len(customers)
