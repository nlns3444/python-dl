user_input = input("enter a sentence:-")#takes input from the user

list_1 = list(user_input)# takes  the input into the list1

print(list_1)
set_1 ={'a', 'e', 'i', 'o', 'u', 'A', 'e', 'i', 'o', 'u'}
count = 0

for i in list_1:# counnts the number of vowels in the list1 and counts them in the set
    if i in set_1:
        count+=1


print(count)