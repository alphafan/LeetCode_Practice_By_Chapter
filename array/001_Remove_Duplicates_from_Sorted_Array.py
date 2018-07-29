""" Remove Duplicates from Sorted Array

Given a sorted array nums, remove the duplicates in-place such that
each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by
modifying the input array in-place with O(1) extra memory.

---

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements
of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.

---

Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements
of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.

---

Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means
modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

"""

import unittest
import random

from utils.timer import timer


class Solution(object):

    @timer
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i, pivot = 1, nums[0]
        while i < len(nums):
            if nums[i] == pivot:
                nums.pop(i)
            else:
                pivot = nums[i]
                i += 1
        return i

    @timer
    def removeDuplicates_V2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Very tricky, but it's really faster
        nums[:] = sorted(list(set(nums)))
        return nums

    def __repr__(self):
        return 'Solution'


class Test(unittest.TestCase):

    # --------------------------------------------------------
    # Normal cases
    # --------------------------------------------------------

    def test_1(self):
        a = [1, 1, 2]
        s = Solution()
        l = s.removeDuplicates(a)
        assert a == [1, 2]
        assert l == 2

    def test_2(self):
        a = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        s = Solution()
        l = s.removeDuplicates(a)
        assert a == [0, 1, 2, 3, 4]
        assert l == 5

    # --------------------------------------------------------
    # Corner cases
    # --------------------------------------------------------

    def test_3(self):
        a = [1, 1]
        s = Solution()
        l = s.removeDuplicates(a)
        assert a == [1]
        assert l == 1

    def test_4(self):
        a = [1]
        s = Solution()
        l = s.removeDuplicates(a)
        assert a == [1]
        assert l == 1

    def test_5(self):
        a = []
        s = Solution()
        l = s.removeDuplicates(a)
        assert a == []
        assert l == 0

    def test_6(self):
        a = [random.randrange(1, 10) for _ in range(0, 50000)]
        s = Solution()
        s.removeDuplicates(a)
        s.removeDuplicates_V2(a)


if __name__ == '__main__':
    unittest.main()
