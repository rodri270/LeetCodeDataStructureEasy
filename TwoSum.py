def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for i in range(len(nums)):
        for b in range(i+1, len(nums)):
            if nums[i] + nums[b] == target:
                print(nums[i],nums[b])
                return nums[i],nums[b]
inputs=(2,7,11,15)
twoSum(inputs,9)