class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perms = []
        n = len(nums)

        def backtrack(i: int) -> None:
            if i == n:
                perms.append(nums[:])
                return

            used = set()
            for j in range(i, n):
                if nums[j] in used:
                    continue

                used.add(nums[j])
                nums[i], nums[j] = nums[j], nums[i]
                backtrack(i + 1)
                nums[j], nums[i] = nums[i], nums[j]

        backtrack(0)

        return perms
