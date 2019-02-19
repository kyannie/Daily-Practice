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
c = b.replace(" ", "*")
print(b.replace("l", "i"))

print(b.split(" "))

d = "I am a mouse ."
print(d.split("a"))

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