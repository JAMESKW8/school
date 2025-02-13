#Best possible way to initialize array
myArr = [None for _ in range(10)]

#array is fixed length while list can vary
#how to initialize array in pyhton, look at first line, same as the first line in txt

#Alternative method
myARR = [0 for i in  range(10)]
print (myArr)

#For string - camrbidge requires to use double quotes
myArr4=[""] * 10
#to print out of the array

for i in range (len(myArr4)):

    print(myArr[i])

#suitable for paper4 to print an array as a separate question
for element in MyArr:
    print(element)

#to test things out and to import
import random
myArr6 = [random.randint(1,100) for i in range(10)]
print(myArr6)

#2D ARRAYS
myArr9 = [[8,2,3,3],[2,2,2,3],[1,5,3,6],[1,7,6,5]]
print(myArr9)

for row in range(4):
    for col in range(4):
        print(myArr9[row][col], end = " ")

        