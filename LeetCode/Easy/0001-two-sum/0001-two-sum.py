class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        final_value = {}
        for index, value in enumerate(nums):
            needed = target - value
            if needed in final_value:
                return [final_value[needed], index]
            final_value[value] = index
