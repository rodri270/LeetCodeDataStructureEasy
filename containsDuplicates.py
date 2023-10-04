
print("this is a change")
print("this is work on pc")


'''
class Solution:
    nums=()
    def containsDuplicate(self, nums) -> bool:
        self.nums = nums
        if len(nums) != len(set(nums)):
           print("True")
        else:
            print("False")
        
obj = Solution()
'''

#Solution
def containsDuplicate(nums) -> bool:
        if len(nums) != len(set(nums)):
           print("True")
        else:
            print("False")

testing=(1,2,3,1)
containsDuplicate(testing)


