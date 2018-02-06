
time = []

for i in range(24):
    for j in range(0,60,30):
        if i<10 and j<10:
            time.append("0" + str(i) + ":0" + str(j))
        elif i<10:
            time.append("0" + str(i) + ":" + str(j))
        elif j<10:
            time.append(str(i) + ":0" + str(j))
        else:
            time.append(str(i) + ":" + str(j))
print(time)
