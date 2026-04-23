def total_calc(bill_amount,tip_perc):
    #define function to calculate the tip on bill 
    total = bill_amount*(1+ 0.01*tip_perc)
    total = round(total,2)
    print(f"please pay ${total}")

#specify only bill amount
#defualt value of tip perecentage is use 

total_calc(150,23)

       