class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        # Check if the operation is '++X' or 'X++', which indicates an increment,
        # we can use `if '+' in op` but this is faster.
        return sum(1 if op == "++X" or op == "X++" else -1 for op in operations)
