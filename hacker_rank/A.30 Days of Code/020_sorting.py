import sys

n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# track number of elements swapped during a single array transversal

totalNumberOfSwaps = 0

for i in range(n):
    currentSwaps = 0

    for j in range(0, n-1):
        if a[j] > a[j+1]:
            a[j], a[j + 1] = a[j + 1], a[j] # swap adjacent elements if they are in decreasing order
            currentSwaps += 1
            totalNumberOfSwaps += 1
# if no elements were swapped during a transversal, array is sorted
    if currentSwaps == 0:
        break

print('Array is sorted in ' + str(totalNumberOfSwaps) + ' swaps.')
print('First Element: '+ str(a[0]))
print('Last Element: ' + str(a[n-1]) )