user = input("entire the sentence:-")#takes the input from the user

list1 = user.split(" ")#splits the words in the given input

list1.sort()#sorts the list in the a;pahbetic order

print(list1)

frequency = {}
count = 0
for i in list1:#if there are any words in the list1 are stored in the frequency list and gives us the count
    frequency[i] = list1.count(i)

print(frequency)


