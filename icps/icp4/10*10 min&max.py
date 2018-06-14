import numpy as np
x = np.random.randint(100,size=(10,10))
print("Original Array:")
print(x)
j=0
for i in x:
    j=j+1
    print(f"Minimum and Maximum Values in {j} are ")
    xmin, xmax = i.min(), i.max()

    print(xmin, xmax)

