class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for indx, num in enumerate(nums):
            for indx2, num2 in enumerate(nums[1:]):
                if (num + num2 == target):
                    result.append(indx)
                    result.append(indx2+1)
                    return result
        return -1

