#!/usr/bin/python3
"""finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """go through list to find a peak"""
    nums = list_of_integers
    if nums is None or nums == []:
        return None
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2 and (nums[0] == nums[1]):
        return nums[0]
    ln = len(nums)
    if ln % 2 != 0:
        ln - 1
    point = ln//2
    l = point - 1
    r = point + 1
    if len(nums) > 2:
        if nums[point] > nums[l] and nums[point] > nums[r]:
            return nums[point]
        else:
            if nums[l] > nums[r]:
                return find_peak(nums[0:point])
            else:
                return find_peak(nums[point+1:ln+1])
    else:
        if nums[0] > nums[1]:
            return nums[0]
        else:
            return nums[1]
