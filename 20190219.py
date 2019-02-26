a = "Hello*11World"

print(a[0])

print(a[1:3])
print(a[1:4])
print(a[-1])
print(a[0:-1])
print(a[-2:-1])
print(a[-1:-5])

print(len(a)) #Get String's length

print(len(" "))
print(len(" "))

print("\"")
print("\"\"")
print("\\")
print("a\ta")
print("a\na")

b = "Hello World"
b = b.replace(" ", "*")
print(b.replace("l", "i"))

print(b.split(" "))

d = "I am a mouse ."

e = ["a", 1, "c"]
print(e)
print(e[0])
print(e[-1])
print(e[0:-1])

e[1] = 2
print(e)

e[2] = "d"
print(e)

print(len(e))

x=["a","b","c"]
x.append("d")
print(x)
x.pop(1)
print(x)
x.append("1")
print(x)

print(2==1+1)

print(2 > 1)
print(3 >= 2)

print(-2 < 2)
print(-2 <= 2)

print(1 > 2)
print(2 <= 2)

a = 2
b = 3
if a == b:
    print("Hi this is True")
else:
    print("Bye this is false")
    print("Bye Bye")
    
print("Hi")

a = 1
b = 2
if a == b:
    print("This is true")
elif a > b:
    print("A is greater than B")
else:
    print("This is False")

mum = 10
while mum > 0 :
    mum = mum - 1
print("Loop End")

family = ["cat", "dog", "mouse"]
for x in family:
    print(x)
print("For Loop End")

numbers = [0, 1, 2, 3, 4, 5]
for i in numbers:
    print(i)
print("For Loop End")

x = [1,2,3,4,5,6,7,8,9]
for i in x:
    if i%2 == 1:
        print("Odd Number")
    else:
        print("Even Number")
print("Loop 1 End")

y = 30
while y > 0:
    y = y-1
    if y%3 == 0:
        print("Yeah")
    elif y%5 == 0:
        print("Ohhh")
    else:
        print("Sad")
print("Loop 2 End")


