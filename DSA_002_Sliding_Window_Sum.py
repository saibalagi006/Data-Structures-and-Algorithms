#Given an array of positive numbers and a positive number ‘k,’ 
# find the maximum sum of any contiguous subarray of size ‘k’
a = [2, 1, 5, 1, 3, 2]
k=3
windowstart = 0
windowend = 0
windowsum = 0
maxsum=0
maxind = -1
for windowend in range(len(a)):
    windowsum +=a[windowend]
    if(windowend>=k-1):
        if(windowsum>maxsum):
            maxsum = windowsum
            maxind = windowstart
        windowsum = windowsum-a[windowstart]
        windowstart = windowstart+1
print(maxsum)
print(a[maxind:maxind+k])       




