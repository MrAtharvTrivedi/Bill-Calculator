# Bill Calculator Made Using Python
# Made by Atharv Trivedi

#   Initializing variable bill to 0
bill = 0

#   Initializing a variable for coupon code
coupon_code = "sale15"

# Initializing some strings
confirmation = "Item Added To The Cart Successfully"
error_confirm = "The item you tried to add is currently unavailable on the store"
ask_ans = "Sorry I did not understand. Kindly enter a valid response"

#   Initializing a dictionary and storing items available in the store and their prices
items = {"mango": 30,
         "apple": 50,
         "banana": 20,
         "pineapple": 60,
         "orange": 40,
         "leeche": 10,
         "guava": 70,
         "watermelon": 80,
         "muskmelon": 90,
         "papaya": 100,
         }

#   Starting a while loop to start the buying process
while(True):
    order = str(input("Enter The Name of the item you wish to buy:")).lower()

    if order in items.keys():
        print(confirmation)
        bill = bill + items[order]
        print(f"Your Total Amount is {bill}")
        checkout = str(input("Would you like to checkout? (y/n):")).lower()
        if (checkout == "y"):
            if (bill < 100):
                print("You can only checkout on a minimun order of Rs 100")
            else:
                while True:
                    ask_if_code = input(
                        "Do you have a coupon code? (y/n):").lower()
                    if ask_if_code == "y":
                        while True:
                            ask_code = input("Enter the coupon code here:").lower()
                            if ask_code == coupon_code:
                                bill = bill - ((bill*15)/100)
                                print("Wow! You got 15% off on your order")
                                print(
                                    f"Thank You For Shopping With Us. Your Total Billing Amount is Rs {bill}")
                                quit()
                            else:
                                print("Enter a valid coupon code")
                    elif ask_if_code == "n":
                        print(
                            f"Thank You For Shopping With Us. Your Total Billing Amount is Rs {bill}")
                        quit()
                    else:
                        print(
                            "Sorry I did not understand. Kindly enter a valid response")
        elif (checkout != "n") and (checkout != "y"):
            while(True):
                print("Sorry I could not understand. Kindly enter a valid answer")
                checkout = str(input("Would you like to checkout? (y/n):")).lower()
                if (checkout == "y"):
                    if (bill < 100):
                        print("You can only checkout on a minimun order of Rs 100")
                        break
                    else:
                        while True:
                            ask_if_code = input("Do you have a coupon code? (y/n):").lower()
                            if ask_if_code == "y":
                                while True:
                                    ask_code = input( "Enter the coupon code here:").lower()
                                    if ask_code == coupon_code:
                                        bill = bill - ((bill*15)/100)
                                        print(
                                            "Wow! You got 15% off on your order")
                                        print(f"Thank You For Shopping With Us. Your Total Billing Amount is Rs {bill}")
                                        quit()
                                    else:
                                        print("Enter a valid coupon code")
                            elif ask_if_code == "n":
                                print(f"Thank You For Shopping With Us. Your Total Billing Amount is Rs {bill}")
                                quit()
                            else:
                                print("Sorry I did not understand. Kindly enter a valid response")
                elif (checkout == "n"):
                    break
        else:
            pass
    else:
        print(error_confirm)
        while True:
            ask = str(input("Do you Wish to add some other item to your cart? (y/n):"))
            if ask == "n":
                if (bill > 100):
                    while True:
                        ask_if_code = input("Do you have a coupon code? (y/n):").lower()
                        if ask_if_code == "y":
                            while True:
                                ask_code = input( "Enter the coupon code here:").lower()
                                if ask_code == coupon_code:
                                    bill = bill - ((bill*15)/100)
                                    print("Wow! You got 15% off on your order")
                                    print(f"Thank You For Shopping With Us. Your Total Billing Amount is Rs {bill}")
                                    quit()
                                else:
                                    print("Enter a valid coupon code")
                        elif ask_if_code == "n":
                            print(f"Thank You For Shopping With Us. Your Total Billing Amount is Rs {bill}")
                            quit()
                        else:
                            print("Sorry I did not understand. Kindly enter a valid response")
                else:
                    print(f"Thank You For Shopping With Us. Your Total Billing Amount is Rs {bill}")
                    quit()
            elif (ask != "n") and (ask != "y"):
                print(ask_ans)
            else:
                break
