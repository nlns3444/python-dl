# Declaring python students list and Web Application students list
pystudents = ["tim", "john", "bhargavi", "reddy", "siddipeta", "UMKC"]
webstudents = ["mike", "sandeep", "laxmi", "siddipeta", "tim", "jim"]

# Loop for priting common students in both classes
# end = " " for printing on same line
print("Students attending both classes are: ", end=" ")
for item in pystudents:
    if item in webstudents:
        print(item, end=" ")

# Loop for students not common in both classes
# end = " " for printing on same line
print("\nStudents not common in both classes are: ", end = " ")
for item in pystudents:
    if item not in webstudents:
        print(item, end=" ")
for item in webstudents:
    if item not in pystudents:
        print(item, end=" ")

