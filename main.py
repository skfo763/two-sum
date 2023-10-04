from typing import List

def twoSum(self, nums: List[int], target: int) -> List[int]:
    list_size = len(nums)
    for left_index in range(0, list_size):
        for right_index in range(left_index+1, list_size):
            left_value = nums[left_index]
            right_value = nums[right_index]
            if left_value + right_value == target:
                return [left_index, right_index]
    return []

class Test:
    def printTest(self):
        print(twoSum(self, [2,7,11,15],9))
        print(twoSum(self, [3,2,4], 6))
        print(twoSum(self, [3,3],6))

# test = Test()
# test.printTest()

