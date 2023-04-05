# -*- coding: utf-8 -*-
# @Time    : 5/4/23 2:56 pm
# @Author  : Yaona
# @File    : randomized_select.py
# @Software: PyCharm
# @Description : randomized select algorithm

import random
def findKSmallest(nums, k):
    """
    Find Top K smallest elements
    :param nums: an array
    :param k: the number of selected elements
    :return: selected elements
    """
    def quickSelect(nums, lo, hi, k):
        pivot = random.randint(lo, hi) # randomly select one element
        nums[hi], nums[pivot] = nums[pivot], nums[hi] # store pivot in the rightmost
        i = j = lo
        while j < hi:
            if nums[j] > nums[hi]: # find one element larger than pivot
                nums[i], nums[j] = nums[j], nums[i] # swap num[i] and num[j]
                i += 1
            j += 1 # one step forward with each j
        nums[i], nums[j] = nums[j], nums[i] # put pivot in the middle
        if hi > k + i - 1: # recur for the left subset
            return quickSelect(nums, i + 1, hi, k)
        elif hi < k + i -1: # recur for the right subset
            return quickSelect(nums, lo, i - 1, k - (hi - i + 1))
        else:
            return nums[i:]
    return quickSelect(nums, 0, len(nums)-1, k)