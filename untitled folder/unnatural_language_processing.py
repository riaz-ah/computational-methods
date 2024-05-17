def split_syllabels(word):
    vowels = 'a', 'e', 'i', 'o', 'u'
    pointer = 0
    count=0
    new_word = word
    while len(new_word[pointer:]) > 3:
        for i in new_word[pointer + 1: pointer + 4]:
            if i in vowels:
                count = count + 1
        if count <2:
            new_word = new_word[pointer:pointer + 2] + '.' + new_word[pointer + 2:]
            pointer = pointer + 3
            count=0

        else:
            new_word = new_word[pointer:pointer + 3] + '.' + new_word[pointer + 3:]
            pointer = pointer + 4
            count=0

    return new_word


t = int(input())

for i in range(t):
    n = int(input())
    word = input()
    print(split_syllabels(word))
