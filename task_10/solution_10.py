line = input()
count = 0
a = str()
b = str()
for i in line:
    if i == ' ':
        line[count] == line[count+1]
    if line[count] == line [-count-1]:
        a = True
    else:
        b = False
    count += 1
c = (a,b)
if False not in c:
    print('полином')
else:
    print('неполином')
