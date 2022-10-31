#Your challenge is to write a Python program that calculates the discounted price of an object using the if-elif-else statement.

#Your conditions are as follows:

#If the price is 300 or above, it will be discounted by 30%
#If the price falls between 200 and 300, it will be discounted by 20%
#If the price falls between 100 and 200, it will be discounted by 10%
#If the price is less than 100, it will be discounted by 5%
#There is no discount for negative prices

price = float(input("enter price: "))

if price >= 300:
    print((30 / 100) * price)  
elif price >= 200 and price < 300:
    print((20 / 100) * price)
elif price >= 100 and price < 200:
    print((10 / 100) * price)
elif price < 100:
    print((5/100) * price)
