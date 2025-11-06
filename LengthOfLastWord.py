def LOFW(line):
    lastIn = len(line) -1  # index of the last character
    count = 0
    while(lastIn >=0 and line[lastIn] == " " ):  # to go to the first character from the back
        lastIn = lastIn -1

    # Now make another loop to till get to the next space from ther previous space by using lastIn
    while(lastIn>=0 and line[lastIn] !=" "): # if it's not space then continue
        count = count +1
        lastIn = lastIn -1 


    return count


def LastWord(str):
    pass

def main():
    s = "Hello World"
    out1 = LOFW(s)
    word1 = LastWord(s)
    print(f"The length of the last word {word1} is {out1} ")

    s1 = "   fly me   to   the moon  "
    out2 = LOFW(s1)
    word2 = LastWord(s1)
    print(f"The length of the last word {word2} is {out2} ")

    s2 = "luffy is still joyboy"
    out3 = LOFW(s2)
    word3 = LastWord(s2)
    print(f"The length of the last word {word3} is {out3} ")

if __name__ == "__main__":
    main()