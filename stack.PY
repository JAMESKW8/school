#how to write function in python

#x = 5
#y= 6
#def add(x,y):
#   return x + y
#print(add(x,y)) = 11




StackArr = [None for i in range(7)]
top = -1
base = 0
full = 7

def isfull():
    if top >= full:
        return True
    else:
        return False

def isEmpty():
    if top < base:
        return True
    else:
        return False

def pop():
    global top
    if top < 0:
        print("The stack is empty")
    else:
        top = top - 1
        print("The item has been popped")

def push(y):
    global top
   
    if isfull() :
        print("The stack is full, cannot push")
    else:
        top = top + 1
        StackArr [top] = y
        print("Item has been pushed")

choice = input("Do you want to push or pop?")
if choice == "pop":
    pop()
if choice == "push": 
    y = int(input("Enter the number to add"))
    push(y)


print(StackArr)