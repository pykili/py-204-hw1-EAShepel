n = input()
num = int(n)
count = 0
summ = 0
for i in range(num):
    count = count + 1
    line = input()
    if line == '0':
        break
    count = count-1
    summ = summ + count

print(summ/(count))
