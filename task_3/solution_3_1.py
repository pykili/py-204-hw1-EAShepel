user_input = input()
alphabet = str()
for i in user_input:
    if i not in alphabet:
        alphabet = alphabet + i
print(alphabet)
