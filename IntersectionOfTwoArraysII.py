def intersect(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        newNums=[]
        for i in range((len(nums1))):
            for k in range(len(nums2)):
                if nums1[i] == nums2[k]:
                    newNums.append(nums1[i])
                    newNums.append(nums2[k])
        newNums=list(dict.fromkeys(newNums))
        print(newNums)
        return newNums
                
                
        
numsTest1=[1,2,2,1]
numsTest2=[2,2]

numsTest3=[4,9,5]
numsTest4=[9,4,9,8,4,8]

intersect(numsTest1, numsTest2)   
intersect(numsTest3,numsTest4)           