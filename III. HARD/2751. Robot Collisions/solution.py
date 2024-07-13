class Solution:
    def survivedRobotsHealths(
        self, positions: List[int], healths: List[int], directions: str
    ) -> List[int]:
        hashmap = {position: index for index, position in enumerate(positions)}
        stack = []

        for position in sorted(positions):
            index = hashmap[position]

            if directions[index] == "R":
                stack.append(index)
                continue

            while stack and healths[index]:
                second = stack.pop()

                if healths[index] > healths[second]:
                    healths[index] -= 1
                    healths[second] = 0
                elif healths[index] < healths[second]:
                    healths[second] -= 1
                    healths[index] = 0
                    stack.append(second)
                else:
                    healths[index] = healths[second] = 0

        return [health for health in healths if health]
