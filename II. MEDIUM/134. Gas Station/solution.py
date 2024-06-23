class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # If the total amount of gas is less than the total amount of cost,
        # return -1. (It is impossible to complete the circuit.)
        if sum(gas) < sum(cost):
            return -1

        n = len(gas)
        total_tank = current_tank = start = 0

        for i in range(n):
            # Add the remaining gas after traveling from the previous station to the current station.
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]
            # If the remaining gas is less than 0, reset the starting station to the next station.
            if current_tank < 0:
                start = i + 1
                current_tank = 0

        # Return the last starting station if the total amount of gas is greater than or equal to the total amount of cost.
        return start if total_tank >= 0 else -1
