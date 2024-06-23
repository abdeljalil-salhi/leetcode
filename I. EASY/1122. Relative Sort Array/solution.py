class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        mymap = {i: 0 for i in arr2}

        for i in arr1:
            if i in mymap:
                mymap[i] += 1

        not_included = [i for i in arr1 if i not in mymap]
        not_included.sort()
        result = []

        for i in arr2:
            result += [i] * mymap[i]

        return result + not_included
