def NumAscinSent(sentence):
    arr = sentence.split()

    i = 0 
    prev_num = 0 
    while i < len(arr):
        if arr[i].isdigit() :
            num = int(arr[i])
            if num <=prev_num:
                return False
            prev_num = num

        i += 1
        
    return True

def main():
    s = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
    out = NumAscinSent(s)
    print(f"The sentence is {out} Ascending order.")

    s1 = "hello world 5 x 5"
    out1 = NumAscinSent(s1)
    print(f"The sentence is {out1} Ascending order.")

    s2 = "sunset is at 7 51 pm overnight lows will be in the low 50 and 60 s"
    out2 = NumAscinSent(s2)
    print(f"The sentence is {out2} Ascending order.")

if __name__ == "__main__":
    main()