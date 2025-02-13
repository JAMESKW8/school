arr2 = [[1,3,5],[7,9,11],[13,15,17]]

found = False

x = int(input("Input the item to be searched"))
for i in range (len(arr2)):
    for n in range (len(arr2[i])):
        if x == arr2[i][n]:
            found = True
            print("It is found in Row", i+1, "and column", n+1)


if not found:
    print("Item is not found")

#2

row = int(input("Input the row to be searched:"))
num = int(input("Input the number to be searched:"))
found = False
for i in range (len(arr2[row])):
    if arr2[i][row] == num:
        found = True
        print("The number is found ")

if not found:
    print("Item not found")
