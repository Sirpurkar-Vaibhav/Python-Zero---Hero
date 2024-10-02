'''
1.selection
2.sequence
3.iteration
'''
#Selection

#1. One-Way Selection (`if` statement)
#Executes a block of code if a condition is true.
x = 10
if x > 5:
    print("x is greater than 5")
  
# 2. Two-Way Selection (`if-else` statement)
#Executes one block of code if a condition is true, and another block if it is false.
x = 10
if x > 15:
    print("x is greater than 15")
else:
    print("x is not greater than 15")
  
#3. Multiple-Way Selection (`if-elif-else` statement)
#Executes different blocks of code based on multiple conditions.
x = 10
if x > 15:
    print("x is greater than 15")
elif x == 10:
    print("x is 10")
else:
    print("x is less than 10")
