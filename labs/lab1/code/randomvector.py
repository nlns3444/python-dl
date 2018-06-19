import numpy as np
x = np.random.randint(20, size=15)
print("Original array:")
print(x)
print("Sorted array:")
print(x)
counts = {}
# to print count of every number
for i in x:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
print('\nCount of each element in the list is ')
print(counts)
# Displays the number with maximum counts
print('\nInteger with maximum occurences in the list is: ')
count = np.bincount(x).argmax()
print(count)