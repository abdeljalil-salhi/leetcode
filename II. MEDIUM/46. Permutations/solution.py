class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        n = len(nums)

        def backtrack(i: int) -> None:
            if i == n:
                perms.append(nums[:])
                return

            for j in range(i, n):
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        backtrack(0)

        return perms
