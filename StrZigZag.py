def ZigZag(str, row):
     retArr = []
     cycle = 2 *(row -1)

     if not str :
          return str
     
     if len(str) == 1 or row <= 1 or row>len(str):
          return str
     
     for r in range(row):
          i = r
          if r == 0 or r == (row -1):
               while(i < len(str)):
                    retArr.append(str[i])
                    i = i + cycle

          else:
               step1 = cycle - 2*r
               step2 = 2*r
               use_step1 = True
               while (i <len(str)):
                    retArr.append(str[i])
                    if use_step1:
                         i = i + step1

                    else:
                         i = i + step2

                    use_step1 = not use_step1

     return ''.join(retArr)
     

def main():
     s = "PAYPALISHIRING"
     numRows = 3
     out = ZigZag(s, numRows)
     print(f" The zig zag of {s}  with the num of row {numRows} is {out}")

     s1 = "PAYPALISHIRING"
     numRows1 = 4
     out1 = ZigZag(s1, numRows1)
     print(f" The zig zag of {s1}  with the num of row {numRows1} is {out1}")


     s2 = "A"
     numRows2 = 1
     out2 = ZigZag(s2, numRows2)
     print(f" The zig zag of {s2}  with the num of row {numRows2} is {out2}")


if __name__ == "__main__":
     main()