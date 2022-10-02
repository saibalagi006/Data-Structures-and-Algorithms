"""
Given an array of sorted numbers, remove all duplicate number instances from it in-place, 
such that each element appears only once. The relative order of the elements should be kept the same 
and you should not use any extra space so that that the solution have a space complexity of O(1)
"""


#arr = [2, 3, 3, 3, 6, 9, 9]
arr = [1,1,2, 3, 3, 3, 6, 9, 9,18,18,21,21]

left = 0
for right in range(1,len(arr)):
    if(arr[left]!=arr[right] and right-left==1):
        left = left+1
    elif(arr[left]==arr[right]):
        continue
    elif(arr[left]!=arr[right] and right-left>1):
        arr[left+1],arr[right] = arr[right],arr[left+1]
        left = left+1
print(arr[:left+1])
