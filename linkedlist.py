#heappointer points to the next available location
#print the linked list in order 9 7 6 5
# start pointer point to the heap pointer

linked_list_data = [5,6,7,9, None,None,None]
linked_list_pointer = [-1, 0 ,1 ,2, 5, 6,-1]
start = 3
heap = 4
itempointer =  start

while itempointer != -1:
    print(linked_list_data[itempointer])
    itempointer = linked_list_pointer[itempointer]

    #find element in the linked list



def add_ll(itemadd):
    global start, heap
    if heap != -1:
        temp = start
        start = heap
        linked_list_data[temp] = itemadd
        heap = linked_list_pointer[start]
        linked_list_pointer[start] = temp
    else:
        return -1


def searchll(itemsearch):
    global pointer
    pointer =  start
    while pointer != -1:
        if linked_list_data[pointer] == itemsearch:
            return pointer
        else:
            pointer = linked_list_pointer[pointer]    
    return -1

#delete item from linked list
#check if linked list is not empty
#check if the item  that wants to be deleted is there or not

def deleted(itemdelete):
    global start, heap
    if start != 0:
        if searchll(itemdelete) == -1:
            print("Item is not found")

        else:
            linked_list_data[pointer] =  None
            temp = pointer
            linked_list_pointer[pointer] = heap
            start = temp

    else:
        print("The list is empty")


itemdelete = int(input("what u wnt to delete? "))
deleted(itemdelete)
print(linked_list_data)

itemadd = int(input("Input yo number           "))

add_ll(itemadd)
print(linked_list_data)


# search = int(input("Enter the number you want to search   "))
# print(searchll(search))
itemadd2 = int(input("Input yo number           "))
add_ll(itemadd2)
print(linked_list_data)
print(linked_list_pointer)

itemadd3 = int(input("Input yo number           "))
add_ll(itemadd3)
print(linked_list_data)