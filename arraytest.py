arr =[4,5,7,2,9,43,2]

sum = 0
min= arr[0]
max= arr[0]

for i in arr:
    sum = sum + i
    if i > max:
        max = i
    elif i < min:
        min = i
print(sum)
print(min)
print(max)
