arr2 = [[1,3,5],[7,9,11],[13,15,17]]

row = int(input("Input the row to be searched:"))
num = int(input("Input the number to be searched:"))
found = False
for i in range (len(arr2[row])):
    if arr2[i][row] == num:
        found = True
        print("The number is found ")

if not found:
    print("Item not found")
