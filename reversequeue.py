queue = [i for i in range(10)]
dequeue = [0 for i in range(10)]
print(queue)
x=9

for i in range(10):
    dequeue[i] = queue[x]
    x = x-1
    i =i+1

print(dequeue)
