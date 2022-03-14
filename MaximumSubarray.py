def maxSubArray(nums) -> int:
    largestNumber = nums[0]
    sizeOfList = len(nums)
    maxEndingNumber = 0
    
    for i in range(0,sizeOfList):
        maxEndingNumber = maxEndingNumber + nums[i]
        if maxEndingNumber < 0:
            maxEndingNumber = 0
        elif (largestNumber<maxEndingNumber):
            largestNumber = maxEndingNumber
    print(largestNumber)       
    return largestNumber

inputs=[-2,-1]
maxSubArray(inputs)