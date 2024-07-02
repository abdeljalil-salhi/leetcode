class Permute:

    def __init__(self, nums: List[int]) -> None:
        self.permutations = []
        self.nums = nums
        self.length = len(nums)

    def backtrack(self, i: int) -> None:
        if i == self.length:
            self.permutations.append(self.nums[:])
            return

        for j in range(i, self.length):
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            self.backtrack(i + 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def get(self) -> List[List[int]]:
        self.backtrack(0)
        return self.permutations


# permutations = Permute([1, 2, 3]).get()
