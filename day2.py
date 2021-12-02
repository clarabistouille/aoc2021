file = open('day2key.txt', 'r')
liste = file.read().split('\n')
liste.pop()

#ONE STAR
depth = 0
hor = 0
aim = 0
for line in liste:
    temp = line.split(' ')
    dir = temp[0]
    val = int(temp[1])
    if dir == "up":
        aim -= val
    elif dir == "down":
        aim += val
    elif dir == "forward":
        hor += val
        depth += aim * val
    else :
        print("wrong direction :", line)
print(depth*hor)
