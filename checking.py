NumOfShare = 306650
Currentshare = 306650
SellShare = Currentshare//2  # half of shares 56823
AvgBPrice = 59.951124144672534
Price = (AvgBPrice + (AvgBPrice*0.05)) # Good price

for i in range(NumOfShare, 0, -(SellShare)):
    print(i)
    i = i//2
    
#     Totalsell = Totalsell + (SellShare*Price)
#     Currentshare = Currentshare - SellShare
#     Price = (Price + (Price*0.05))
#     print(Totalsell)

for i in range(10 , 1 , -1):
    print(i)

print("THis is the code !")