class Solution:
    def maxProfitAssignment(
        self, difficulty: List[int], profit: List[int], worker: List[int]
    ) -> int:
        # Sort the jobs by difficulty and profit
        jobs = sorted(zip(difficulty, profit))
        n = len(jobs)
        worker.sort()

        max_profit = max_profit_so_far = job_index = 0

        for ability in worker:

            # Iterate through the jobs and find the maximum profit that can be made
            while job_index < n and jobs[job_index][0] <= ability:
                max_profit_so_far = max(max_profit_so_far, jobs[job_index][1])
                job_index += 1

            # Update the maximum profit that can be made by the worker
            max_profit += max_profit_so_far

        return max_profit
