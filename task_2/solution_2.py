user_input = input()
c = 0
for i in user_input:
    count = 0
    for j in user_input:
        if i == j:
            count = count + 1
    if count > c:
        c = count
        most_frequent_character = i
print(most_frequent_character)
