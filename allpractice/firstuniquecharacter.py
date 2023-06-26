def firstUniqChar(s):
    repeat = {}
    for i in range(len(s)):
        if s[i] not in repeat:
            repeat[s[i]] = 1
        else:
            repeat[s[i]] = repeat[s[i]] + 1
    for i in range(len(s)):
        print(repeat[s[i]])
        if repeat[s[i]] == 1:
            return i

    return -1


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(firstUniqChar('kanika'))
