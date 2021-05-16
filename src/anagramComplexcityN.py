def isAnagram(s1:str, s2:str)->bool:
    characterOccurenceS1 = [0]*26
    characterOccurenceS2 = [0]*26
    pos1 = 0
    flag = True
    for i in s1:
        charAtPos = ord(i) - ord('a')
        characterOccurenceS1[charAtPos] = characterOccurenceS1[charAtPos] + 1

    for i in s2:
        charAtPos = ord(i) - ord('a')
        characterOccurenceS2[charAtPos] = characterOccurenceS2[charAtPos] + 1

    j = 0
    while j < 26:
        if characterOccurenceS2[j] != characterOccurenceS1[j]:
            return False
        j +=1
    return flag

if __name__ == '__main__':
    if isAnagram('python', 'hello'):
        print('Is an anagram')
    else:
        print('Not an Anagram')










