#codewars "Columnize"
items, columns_count = ["1", "12", "123", "1234", "12345", "123456"], 3


item1 = [x**2 for x in range(1,22,2)]



def dividelist(listt, n):
    subarraysize = len(listt)//n
    arrayAnswer = []
    subarrayAnswer = []
    count = 0
    
    if n > len(listt):
        return listt
    else:
        for i in range(len(listt)):
            count += 1
            subarrayAnswer.append(listt[i])
            if count  == subarraysize:
                arrayAnswer.append(subarrayAnswer)
                count = 0
                subarrayAnswer = []
    if len(subarrayAnswer) > 0:
        arrayAnswer.append(subarrayAnswer)
    return arrayAnswer

print(dividelist(item1, 3))

def checkmaxbycolumn(listt):
    numberofcolumns = len(listt[0][0])