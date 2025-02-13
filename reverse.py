queue = [i for i in range(6)]
front = 0


reverse = [0 for i in range(6)]
def enqueue(x):
    if reverse[i] != front:
        print("It is full")
    else:
        reverse[front] = x
        front = front + 1

def dequeue():
    