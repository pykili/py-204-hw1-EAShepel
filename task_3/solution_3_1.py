user_input = input()
alphabet = str()
for i in user_input:
    if not i in alphabet:
        alphabet = alphabet + i
print(alphabet)
