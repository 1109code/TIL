import sys
input = sys.stdin.readline

def push(X):
    stack.append(X)
    return
    
def pop():
    if len(stack) == 0:
        return -1
    else:
        return stack.pop()

def size():
    return len(stack)
    

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0
    

def top():
    if len(stack) == 0:
        return -1
    else:
        return stack[-1]
    

N = int(input())

stack = []

for i in range(N):
    order = input().split()

    if order[0] == 'push':
        push((int(order[1])))

    elif order[0] == 'pop':
        print(pop())
    
    elif order[0] == 'size':
        print(size())

    elif order[0] == 'empty':
        print(empty())

    elif order[0] == 'top':
        print(top())