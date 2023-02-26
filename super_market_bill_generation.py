from datetime import datetime

name = input("Enter Your Name : ")

lists = '''
Rice    Rs 20/Kg
Sugar   Rs 25/Kg
Salt    Rs 30/Kg
Eggs    Rs 8/one
Panner  Rs 100/200g
Milk    Rs 35/packet
Bread   Rs 35/packet
'''

# Declaration
price = 0
price_list = []
total_price = 0
final_price = 0
i_list = []
q_list = []
p_list = []

# Prices for Items
items = {"rice": 20,
         "sugar": 25,
         "salt": 30,
         "eggs": 8,
         "panner": 100,
         "milk": 35,
         "bread": 35
         }

option= int(input("List of items Press 1 : "))
if option == 1:
    print(lists)

for i in range(len(items)) :
    input_1=int(input("If you want to buy Press 1 or Press 2 for exit : "))
    if input_1==2:
        break
    if input_1 ==1:
        item= input("Enter your Items : ")
        quantity = int(input("Enter quantity : "))
        if item in items.keys():
            price = quantity * (items[item])
            price_list.append((item,quantity,items,price))
            total_price += price

            i_list.append(item)
            q_list.append(quantity)
            p_list.append(price)
            gst= (total_price*5)/100
            final_amount = gst + total_price
        else:
            print("Sorry the item you have entered is not available")
    else:
        print("You entered the wrong number")
    inp = input("Can i bill the items Yes or No : ")
    if inp=="yes":
        pass
        if final_amount!=0:
            print(25 * "=", "Python Super Market ", 25*"=")
            print(28 * " ","Kakinada")
            print("Name : ",name,30*" ","Date : ",datetime.now())
            print(75*"-")
            print("S.No: ", 8*" ","items",8*" ","quantity",3*" ", "price")
            for i in range(len(price_list)):
                print(i+1,8*" ",5 *" ",i_list[i],8*" ",q_list[i],8*" ",p_list[i])
            print(75*"-")
            print(50*" ","Total Amount  : Rs ",total_price)
            print(50*" ","GST Amount    : Rs ",gst )
            print(50*" ","Final Amount  : Rs ", final_amount)
            print(75*"-")
            print(10 * " ","Thanks ",name.upper(), "for Shopping here...Please Visit again")
            print(75* "-")