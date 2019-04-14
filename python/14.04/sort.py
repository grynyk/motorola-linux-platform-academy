def sortFun(inputList, reverseFlag, limitFlag):
    sortedInput = sorted(inputList)

    if reverseFlag == True :
        result = list(reversed(sortedInput))
    if limitFlag == True:
        result = sortedInput[:5]
    if limitFlag == True and reverseFlag == True:
        result = list(reversed(sortedInput[:5]))
    else:
        result = sorted(inputList)
    return result

res = sortFun('abcdefgaaaaaaaaaaaaa',True,True)
print(res)
