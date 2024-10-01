#Strings
name = "James"
print("Hello", "World", 2024)
print("Hello", end=" ")
print(f"Your name is {name}")
print("Your name is {}".format(name))

#Arithmetic
print((10//3)**2)
for i in range(1, 13):
    print(f"2 x {i} = {2*i}")
a = 6
b = 4
c = 5
d = 2
e = 3
result = (a*b) + (c**d) - (b%e)
print(f"({a} * {b}) + ({c} ** {d}) - ({b} % {e}) = {result}")

#Input
name = input("What is your name? ")
print(f"Your name is {name}")