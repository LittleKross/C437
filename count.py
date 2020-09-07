file = open("data.dat")
linecount = 0
for line in file:
    count0 = 0
    count1 = 0
    for i in line:
        if i == '0':
            count0 += 1
        if i == '1':
            count1 += 1
    if count0 % 3 == 0 or count1 % 2 == 0:
        linecount += 1
print(linecount)