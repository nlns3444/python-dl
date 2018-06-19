# Input list for the program
input = [1, 3, 6, 2, -1, 4 ,-4, 5, 2, 8, -2, 9]

# Using nested for loops to get each number for the triplet
print('Triplets that make a sum of Zero in the list are:\n')
for i in input:
    for j in input:
        for k in input:
            # Condition to check the sum of triplet is zero or not and i!=j, j!=k for getting unique triplets with no repetitions
            if (i+j+k) == 0 and i!=j and j!=k:
                # Printing output as list of tuples
                print(list([(i,j,k)]))

