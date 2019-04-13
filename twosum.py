class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        table = {}
        for idx, value in enumerate(nums):
            if (target-value) in table.keys():
                return [table[target-value], idx]
            else:
                table[value] = idx