class Permute:

    def __init__(self, nums: List[int], unique: bool = False) -> None:
        self.nums = nums
        self.unique = unique
        self.length = len(nums)
        self.permutations = []

    def backtrack(self, i: int) -> None:
        if i == self.length:
            self.permutations.append(self.nums[:])
            return

        if self.unique:
            used = set()
        for j in range(i, self.length):
            if self.unique:
                if self.nums[j] in used:
                    continue
                used.add(self.nums[j])

            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
            self.backtrack(i + 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]

    def get(self) -> List[List[int]]:
        self.backtrack(0)
        return self.permutations


# # Get permutations with possible duplicates
# permutations = Permute([1, 2, 3]).get()

# # Get permutations without duplicates
# permutations = Permute([1, 1, 2], unique=True).get()
