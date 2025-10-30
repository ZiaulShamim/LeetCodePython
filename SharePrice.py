def TotalSaleAMI(num, price):  # Total sale after minimum increse (5% of the total share)
    TotalAfSale = num*price
    return TotalAfSale

def ShareAvgPrice(price):
    Half = price//2
    BShare = 5
    TotalBuy = 0
    TOtalShare = 0
    percentage = int(price*0.05)  # 100(5)=500, 95(10) 950, 90(20)1800, 85(40)3400, 80(80)6400, 75(160)12000, 70(320)22400, 65(640)41600, 60(1280)76800, 55(2560)140800, 50(excluded)
    for i in range(price, Half, -percentage):
        EveryBuy = BShare*price
        TOtalShare = TOtalShare + BShare
        BShare = BShare*2
        TotalBuy = TotalBuy + EveryBuy
        

        price = price - percentage 
    return (TotalBuy/TOtalShare), TOtalShare

def SelSlowley(NumOfShare, AvgBPrice):
    Totalsell = 0
    
    Currentshare = NumOfShare
    SellShare = Currentshare//2  # half of shares 56823

    Price = (AvgBPrice + (AvgBPrice*0.05)) # Good price

    for i in range(NumOfShare, 0, SellShare):
        SellShare = Currentshare//2
        
        Totalsell = Totalsell + (SellShare*Price)
        Currentshare = Currentshare - SellShare
        Price = (Price + (Price*0.05))
        
    return Totalsell

def main():
    SPrice = 100
    avgBuy, totalShare = ShareAvgPrice(SPrice)
    print(f"Avg price of buying share is {avgBuy} and ")

    toalPrice = avgBuy*totalShare
    print(f"Total price of buying share is {toalPrice}")
    lowestIncrease = (avgBuy + (avgBuy*0.05))
    print(f"TOtal price of selling after increse is {lowestIncrease}")
    totalPriceAI = TotalSaleAMI(lowestIncrease,totalShare)
    print(f"Total price of Selling after {5} % of increase from the lowest is {totalPriceAI}")
    print(f"The price difference is {((totalPriceAI - toalPrice)/toalPrice)*100} %")

    print()
    print("-------------------------")
    print("If you sell slowly :")
    TotalPriceAI1 = SelSlowley(totalShare , avgBuy)
    print(f"The total selling price is : {TotalPriceAI1}")




if __name__ == "__main__":
    main()