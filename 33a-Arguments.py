def multiply(x, y):
    return x * y

def apply(funct, x, y):
    return funct(x, y)

result = apply(multiply, 5, 2)
print(result) #10
