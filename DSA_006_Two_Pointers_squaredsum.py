class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        right = -1
        squared = []
        new_squared = []
        for i in range(len(nums)):
            if(nums[i]>=0):
                right = i
                break
        if(right==-1):
            right = len(nums)-1
        left = right-1
        
        while(right!=len(nums) or left!=-1):
            if(left==-1):
                new_squared.append(nums[right]*nums[right])
                right = right+1
            elif(right==len(nums)):
                new_squared.append(nums[left]*nums[left])
                left = left-1
            elif(nums[left]*nums[left]<=nums[right]*nums[right]):
                new_squared.append(nums[left]*nums[left])
                left = left-1
            elif(nums[left]*nums[left]>nums[right]*nums[right]):
                new_squared.append(nums[right]*nums[right])
                right = right+1
        return new_squared
                
            
        