class Solution:
    # The quickSort method sorts the list in ascending order
    def quickSort(self, alist):
        self.quickSortHelper(alist, 0, len(alist) - 1)

    # This helper method is used to recursively sort the list
    def quickSortHelper(self, alist, first, last):
        if first < last:

            splitpoint = self.partition(alist, first, last)

            self.quickSortHelper(alist, first, splitpoint - 1)
            self.quickSortHelper(alist, splitpoint + 1, last)

    # This method is used to partition the list and return the split point
    def partition(self, alist, first, last):
        pivotvalue = alist[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = alist[leftmark]
                alist[leftmark] = alist[rightmark]
                alist[rightmark] = temp

        temp = alist[first]
        alist[first] = alist[rightmark]
        alist[rightmark] = temp

        return rightmark

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Merge the two lists together
        for i in range(n):
            nums1[m + i] = nums2[i]

        # Sort the merged list
        self.quickSort(nums1)
