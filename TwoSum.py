def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for b in range(i+1, len(nums)):
            if nums[i] + nums[b] == target:
                return i,b
inputs=[2,7,11,15]
twoSum(inputs,9)