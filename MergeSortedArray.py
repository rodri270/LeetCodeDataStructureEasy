def merge(nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        indexLastPosition = m + n - 1
        
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[indexLastPosition] = nums1[m-1]
                m -= 1
            else:
                nums1[indexLastPosition] = nums2[n-1]
                n -= 1
            indexLastPosition -= 1
            
        while n > 0:
            nums1[indexLastPosition] = nums2[n-1]
            n, indexLastPosition = n - 1, indexLastPosition -1    

        print(nums1)

testNums1=[1,2,3,0,0,0]   
testM = 3
testNums2=[2,5,6]
testN = 3

test2Nums = [1]
test2M = 1
test2Nums2 = []
test2N = 0

test3Nums = [0]
test3M = 0
test3Nums2 = [1]
test3N = 1


merge(testNums1,testM,testNums2,testN)
merge(test2Nums,test2M,test2Nums2,test2N)
merge(test3Nums,test3M,test3Nums2,test3N)