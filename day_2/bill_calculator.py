bill = float(input("What is your total bill  "))
tip = int(input ("What percentage of tip you like to give?  10, 12, or 15?  "))
split = int(input ("How many people to split the bill  "))
each= f"your total bill is{bill+(bill*tip/100)}, the {tip} percentage of your bill is {bill * tip /100 }, each person has to pay {(bill+(bill*tip/100))/split} "
print(each)