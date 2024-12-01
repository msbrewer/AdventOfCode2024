
leftlist = []
rightlist = []

with open("input", "r") as f:
    rows = f.read().split("\n")

for row in rows:
    if row != "":
        item = row.split("   ")
        leftlist.append(item[0])
        rightlist.append(item[1])

similarity = 0
for lnumber in leftlist:
    countl = 0
    for rnumber in rightlist:
        if rnumber == lnumber:
            countl += 1
    similarity += (int(lnumber) * countl)

totaldiff = 0
while len(leftlist) > 0:
    totaldiff += abs(int(min(leftlist)) - int(min(rightlist)))
    leftlist.remove(min(leftlist))
    rightlist.remove(min(rightlist))
print(totaldiff)
print(similarity)
