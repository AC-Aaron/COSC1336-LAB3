#Aaron Aguilar-Chavez
#Complete
#

'''Write a program that asks the user to enter the number of packages purchased.  The program should then display 
the dollar amount of the discount (if any) and the total amount of the purchase after discount. Your program should 
produce correctly labeled output with dollar amounts rounded to 2 decimal places and dollar signs displayed'''

softwarePackage = float(149.00)

orderQuantity = int(input('Please enter the number of Geekware packages you wish to purchase: '))
orderCost = softwarePackage * orderQuantity
oderDiscount = None
orderCostAfterDiscount = None


if orderQuantity < 1:
    print('Number of packages invalid. Please enter a number greater than 0.')

elif orderQuantity > 0 and orderQuantity <= 9: 
    print('You have received no discount on your order since you ordered less than 10 packages!')
    print(f'Your order total is ${orderCost:.2f}')

elif orderQuantity >= 10 and orderQuantity <= 49: 
    oderDiscount = orderCost * .10
    orderCostAfterDiscount = orderCost - oderDiscount
    print(f'You have received a %10 discount taking a total of ${oderDiscount:.2f} off your order!')
    print(f'Your order total is ${orderCostAfterDiscount:.2f}')

elif orderQuantity >= 50 and orderQuantity <= 99: 
    oderDiscount = orderCost * .20
    orderCostAfterDiscount = orderCost - oderDiscount
    print(f'You have received a %20 discount taking a total of ${oderDiscount:.2f} off your order!')
    print(f'Your order total is ${orderCost:.2f}')

elif orderQuantity >= 100 and orderQuantity < 150: 
    oderDiscount = orderCost * .30
    orderCostAfterDiscount = orderCost - oderDiscount
    print(f'You have received a %30 discount taking a total of ${oderDiscount:.2f} off your order!')
    print(f'Your order total is ${orderCost:.2f}')

elif orderQuantity >= 150: 
    oderDiscount = orderCost * .40
    orderCostAfterDiscount = orderCost - oderDiscount
    print(f'You have received a %40 discount taking a total of ${oderDiscount:.2f} off your order!')
    print(f'Your order total is ${orderCost:.2f}')

else:
    print('Error, please check your input and try again.')