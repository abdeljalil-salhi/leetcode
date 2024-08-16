class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        hmap = {"5": 0, "10": 0, "20": 0}

        for bill in bills:
            if bill == 5:
                hmap["5"] += 1
            elif bill == 10:
                hmap["10"] += 1
                if hmap["5"] > 0:
                    hmap["5"] -= 1
                else:
                    return False
            else:
                hmap["20"] += 1
                if hmap["10"] > 0 and hmap["5"] > 0:
                    hmap["10"] -= 1
                    hmap["5"] -= 1
                elif hmap["5"] > 2:
                    hmap["5"] -= 3
                else:
                    return False

        return True
