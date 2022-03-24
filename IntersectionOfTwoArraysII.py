def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        newNums1=[]
        for i in nums1:
            if i in nums2:
                nums2.remove(i)
                newNums1.append(i)
        print(newNums1)
        return newNums1
                
                
        
numsTest1=[1,2,2,1]
numsTest2=[2,2]

numsTest3=[4,9,5]
numsTest4=[9,4,9,8,4,8]

intersect(numsTest1, numsTest2)   
intersect(numsTest3,numsTest4)           