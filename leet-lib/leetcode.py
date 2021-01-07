"""
This is a library designated to help myself train my usage of python
in solving leetcode problems with different time-complexities
"""



"""
LeetCode Problem 1: Two Sum
Input: List[int] arr, int Target, int Time, space Time
    arr -> Array input
    Target -> Target Value
    Time -> Time complexity to solve this problem
    Space -> Space complexity to solve this problem
Output: List[int]
"""
def twoSum(arr, target, time==None, space==None):
    if time is None and space is None:
        return twoSumN(arr,target)
    elif time is "n2" and space is "1":
        return twoSumNSquared(arr, target)
    elif time is "n" and space is "n":
        return twoSumN(arr,target)
    elif time is None:
        return twoSumNSquared(arr,target)
    elif space is None:
        return twoSumN(arr, target)
    else:
        raise Exception("There is no solution with this time and space complexity")

def twoSumNSquared(arr, target):
    """
    The Brute Force Solution:
    We loop through the array twice, get the indices of a given pair and return them if they are the target
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    size = len(arr)
    for i in range(size):
        for j in range(i+1, size):
            if (nums[i] + nums[j]) == target:
                return [i, j]
    raise Exception("There is no solution for this arr, target combination")

def twoSumN(arr, target):
    #store a hashmap of values and their indices
    """
    The optimized one-pass solution
    We loop through the array once

    """
    seen = {}
    for i, val in enumerate(arr):
        complement = target - arr[i]
        if complement in seen:
            return [i, seen[complement]]
        else:
            seen[val] = i
    raise Exception("There is no solution for this arr, target combination")
