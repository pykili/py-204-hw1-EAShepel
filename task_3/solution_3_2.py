alphabet = str()
for i in range(10):
    user_input = input()
    for i in user_input:
        if not i in alphabet:
            alphabet = alphabet + i
print(alphabet)
