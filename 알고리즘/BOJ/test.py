left = 0
right = 0
while True:
    right += 1
    print(left, right)
    left = right

    if right == 3:
        break
print(left, right)