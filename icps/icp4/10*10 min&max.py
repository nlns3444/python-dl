import numpy as np#numpy isa library which has numerous uses and one of them is generating random numbers in an array
x = np.random.randint(100,size=(10,10))#randit is a predefined thing which takes the size of the array and as well as the range 
print("Original Array:")
print(x)
j=0
for i in x
    j=j+1
    print(f"Minimum and Maximum Values in {j} are ")#here f is string formatting cause we are using direct value of j in print statement
    xmin, xmax = i.min(), i.max()

    print(xmin, xmax)#prints max and min value in the array

