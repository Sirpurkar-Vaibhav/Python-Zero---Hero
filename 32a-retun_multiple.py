def mult():
    a = 1
    b = 2
    return a, b

n1, n2 = mult()
print(n1)
print(n2)

def greeting():
    a = 1
    b = 2
    return (a, b)

print(greeting())

def greeting_v2():
    a = 1
    b = 2
    return [a, b]

print(greeting_v2())
'''1
   2
(1, 2)
[1, 2]'''
