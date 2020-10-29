for i in range(10):
    user_input = input()
    k = 0
    s1 = 0
    s2 = 0
    s3 = 0
    for letter in user_input:
        if '\t' not in user_input:
            break
        if letter == '\t':
            if s1 == 0:
                s1 = k
            elif s2 == 0:
                s2 = k
            else:
                s3 = k
        k = k + 1
    form = user_input[s1+1:s2]
    lemma = user_input[s2+1:s3]
    if form != lemma and form not in lemma:
        print(form,lemma)
