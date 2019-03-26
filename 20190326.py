arr="abcdefghijklmnopqrstuvwxyz"
arrlist=list(arr)
x=0
while x<len(arrlist)-len(arrlist)%5:
    print(arr[x:x+5])
    x=x+5
    
arr="abcdefghijklmnopqrstuvwxyz"
arrlist = list(arr)
length = int ((len(arrlist)-len(arrlist)%5)/5)
for x in range(length):
    if x%2 == 1:
        xlist = list(arr[x*5:x*5+5])
        position = len (xlist)-1
        y = ""
        while position >=0:
            y = y + xlist [position]
            position = position-1
        print(y)
    else:
        print(arr[x*5:x*5+5])
   