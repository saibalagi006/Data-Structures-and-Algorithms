#### Given an array, find the average of each subarray of ‘K’ contiguous elements in it.

### Brute force 

a = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k=5
avg = []

for i in range(len(a)-k+1):
    sum = 0
    for j in range(i,i+5):
        sum = sum+a[j]
    avg.append(sum/5.0)
print(avg)
        
#### Sliding Window Technique
sum = 0
avg = []
for i in range(len(a)):
    if(i<=k-1):
        sum = sum+a[i]
    else:
        avg.append(sum/k)
        sum = sum-a[i-k]+a[i]
avg.append(sum/k)
print(avg)


