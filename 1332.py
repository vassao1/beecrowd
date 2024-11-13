def wordCheck(palavra):
    sem = 0
    if len(palavra)>3:
        return "3"
    else:
        if palavra[0] == "o":
            sem += 1
        if palavra[1] == "n":
            sem += 1
        if palavra[2] == "e":
            sem += 1
        if sem >= 2:
            return "1"
        else:
            return "2"

cases = int(input())

for _ in range(cases):
    palavra = input()
    print(wordCheck(palavra))
