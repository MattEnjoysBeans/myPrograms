def scrab1(string):
    score = 0
    for i in string:
        i = i.lower()
        if i in {'a','e','i','o','u','l','n','s','t','r'}:
            score += 1
        elif i in {'d','g'}:
            score += 2
        elif i in {'b','c','m','p'}:
            score += 3
        elif i in {'f','h','v','w','y'}:
            score += 4
        elif i in 'k':
            score += 5
        elif i in {'j','x'}:
            score += 8
        elif i in {'q','z'}:
            score += 10
    return score

def scrab2(a_list):
    scoreList = []
    for j in a_list:
        scoreList.append(scrab1(j))
    return scoreList

def scrabSort(b_list):
    scoreList = scrab2(b_list)
    for k in range(1, len(scoreList)):
        m = k
        while m < 0:
            if scoreList[m-1] > scoreList[m]:
                scoreList[m-1], scoreList[m] = scoreList[m], scoreList[m-1]
                b_list[m-1], b_list[m] = b_list[m], b_list[m-1]
            else:
                break
            m -= 1
    return b_list[::-1]

WORD_LIST = ["CAT", "DOG", "SUN", "BED", "QUIZ"]
print(scrabSort(WORD_LIST))



            

