n = input()
num = int(n)
count = 0
summ = 0
for i in range(num):
    count = count + 1
    line = input()
    if line == '0':
        break
    else:
        summ = summ + int(line)

print(summ/(count-1))
