#Given an array of sorted numbers and a target sum, 
#find a pair in the array whose sum is equal to the given target.

from pickle import TRUE


arr =[1, 2, 3, 4, 6]
target=6

left = 0
right = len(arr)-1
s = 0
while(left<right):
    sum = arr[left]+arr[right]
    if(sum==target):
        print("found",left,right)
        s = 1
        break
    elif(sum<target):
        left = left+1
    elif(sum>target):
        right = right-1

if(s==0):
    print("failure, not found")

    