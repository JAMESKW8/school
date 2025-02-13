#Write pseudocode and program code to search for an element in a 1D array using linear search
import random
MyArray = [random.randint(1,100) for _ in range (10)]
print(MyArray)
x =int(input("input the number to be searched:"))
Found =  False
for i in range (len(MyArray)):
    if x == MyArray[i]:
        Found=  True
        print("The number is found in number ", i )

if Found == False:
    print("Number is not found")


