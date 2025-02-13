#used when dealing with sorted array

arr = [10,18,29,34,56,57,67,88]

x = int(input("input the number to be searched"))

found = False
top = len(arr)
bottom = 0

while not found and top > bottom:
    mid = int((top + bottom)/2)
    if arr[mid] == x:
        found =  True
    elif x > arr[mid]:
        bottom =  mid + 1
    elif x < arr[mid]:
        top = mid - 1



if found:
    print("Item is found")
else:
    print("Item is not found")