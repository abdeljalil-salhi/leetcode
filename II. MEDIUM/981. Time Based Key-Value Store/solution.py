class TimeMap:

    def __init__(self):
        self.hmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.hmap:
            self.hmap[key] = []
        self.hmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hmap:
            return ""

        low, high = 0, len(self.hmap[key]) - 1

        while low <= high:
            mid = (low + high) // 2

            if self.hmap[key][mid][1] == timestamp:
                return self.hmap[key][mid][0]
            elif self.hmap[key][mid][1] < timestamp:
                low = mid + 1
            else:
                high = mid - 1

        if high >= 0 and self.hmap[key][high][1] <= timestamp:
            return self.hmap[key][high][0]

        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
