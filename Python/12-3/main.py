import re

string = open('input','r').read().strip()

total = 0
on = True
for letter in range(len(string)):
    if string[letter:letter+4] == 'do()':
        on = True
    if string[letter:letter+7] == "don't()":
        on = False
    if string[letter:letter+4] == 'mul(':
        s = letter+4
        while string[s]!=')':
            s += 1
        try:
            mul1, mul2 = map(int, re.findall(r'\d{1,3}', string[letter:s+1]))
            if string[s-1] not in ['0','1','2','3','4','5','6','7','8','9']:
                continue
            if on:
                total += mul1*mul2
        except:
            pass
print(total)
