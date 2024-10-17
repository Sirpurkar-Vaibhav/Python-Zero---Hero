#logical operators and or not
a = 10
b = 20
c = 60

if a > b and c > b:
    print("All the conditions are satisfied")
else:
    print("One or more conditions are failed")

if a > b or c > b:
    print("At least one condition is satisfied")
else:
    print("None of the conditions are satisfied")
