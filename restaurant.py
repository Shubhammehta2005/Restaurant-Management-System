import pandas as pd
from pandas import DataFrame as df
import openpyxl as op
from datetime import datetime
from colorama import Fore, Style, init
import pyttsx3
from prettytable import PrettyTable
import time

init()

global orders1
orders1=[]
global name
global number
global totalprice
global orderscode
global payment_method
payment_method=''
orderscode=[]
totalprice=0

speech = pyttsx3.init()

def display_date_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{Fore.BLUE}Current Date and Time: {current_time}{Style.RESET_ALL}")
    
    # Speak the date and time
    speech.say(f"The current date and time is {current_time}")
    speech.runAndWait()

def start():
    print(f"{Fore.GREEN}{Style.BRIGHT}|-------------------------|")
    print("|                         |")
    print("|Welcome To Our Restaurant|")
    print("|                         |")
    print("|-------------------------|{Style.RESET_ALL}")


menu = {
                101: {"item": "BIG SPICY WRAP(V) + PEPSI", "price": 284},
                102: {"item": "SPICY TANDOOR(V) + COLD COFFEE", "price": 250},
                103: {"item": "MAHARAJA MECH(V) + NUGGETS", "price": 292},
                104: {"item": "CHEESE VEGGIE POCKETS + COKE", "price": 197},
                105: {"item": "CRISPY VEG + FRENCH FRIES", "price": 148},
                    }
menu1 = {
                201: {"item": "9 Cheese Pizza", "price": 451},
                202: {"item": "Veggie Victory Voyage", "price": 399},
                203: {"item": "Tandoori Temptation", "price": 373},
                204: {"item": "Supreme Symphony", "price": 301},
                205: {"item": "Margarita Marvel", "price": 251}}
menu2 = {
                301: {"item": "Gourmet Special", "price": 199},
                302: {"item": "Smoky BBQ Bistro Burger", "price": 210},
                303: {"item": "Cheesy Chorizo Fiesta", "price": 151},
                304: {"item": "Veggie Delight Dynamo", "price": 121},
                305: {"item": "Aloo Tikki", "price": 69}   
}
menu3 = {
                401: {"item": "Paneer Paradise Platter", "price": 249},
                402: {"item": "Tandoori Vegetable Tango", "price": 212},
                403: {"item": "Veggie Kebab Carnival", "price": 199},
                404: {"item": "Achari Avocado Adventure", "price": 179},
                405: {"item": "Cheese Chutney", "price": 99}}
menu4 = {
                501: {"item": "Pav Bhaji", "price": 151},
                502: {"item": "Masala Dosa", "price": 119},
                503: {"item": "Manchurian(Dry)", "price": 99},
                504: {"item": "Paneer Chilli", "price": 199},
                505: {"item": "Hara-Bhara Kebab", "price": 151}}
menu5 = {
                601: {"item": "Sex on the beach", "price": 199},
                602: {"item": "Melon Magic Infusion", "price": 151},
                603: {"item": "Blueberry Breeze Bliss", "price": 199},
                604: {"item": "Vanilla Velvet Dream", "price": 199},
                605: {"item": "Berry Burst Elixir", "price": 210}}
menu6 = {
                701: {"item": "Caramel Dream Delight", "price": 249},
                702: {"item": "Pistachio Paradise", "price": 210},
                703: {"item": "Blueberry Cheese Cake", "price": 199},
                704: {"item": "Coffee Caramel Cascade", "price": 199},
                705: {"item": "Choco Truffle Brownie", "price": 149}}
def Combo_menu():
    print(  "|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
          "\n|  CODE |         ITEM NAME                 | PRICE(Rs)|"
          "\n|- - - -| - - - - - - - - - - - - - - - - - |- - - - - |"
          "\n|  101  |  BIG SPICY WRAP(V) + PEPSI        |   284    |"
          "\n|  102  |  SPICY TANDOOR(V)  + COLD COFFEE  |   250    |"
          "\n|  103  |  MAHARAJA MECH(V)  + NUGGETS      |   292    |"
          "\n|  104  |  CHEESE VEGGIE POCKETS + COKE     |   197    |"
          "\n|  105  |  CRISPY VEG + FRENCH FRIES        |   148    |"
          "\n|- - - - - - - - - - - - - - - - - - - - - - - - - - - |")


def Pizza():
    print(  "|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
          "\n|  CODE |         ITEM NAME                 | PRICE(Rs)|"
          "\n|- - - -| - - - - - - - - - - - - - - - - - |- - - - - |"
          "\n|  201  | 9 Cheese Pizza                    |   459    |"
          "\n|  202  | Veggie Victory Voyage             |   399    |"
          "\n|  203  | Tandoori Temptation               |   379    |"
          "\n|  204  | Supreme Symphony                  |   301    |"
          "\n|  205  | Margarita Marvel                  |   251    |"
          "\n|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
    )
def Burgers():
    print(  "|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
          "\n|  CODE |         ITEM NAME                 | PRICE(Rs)|"
          "\n|- - - -| - - - - - - - - - - - - - - - - - |- - - - - |"
          "\n|  301  | Gourmet Special                   |   199    |"
          "\n|  302  | Smoky BBQ Bistro Burger           |   210    |"
          "\n|  303  | Cheesy Chorizo Fiesta             |   151    |"
          "\n|  304  | Veggie Delight Dynamo             |   121    |"
          "\n|  305  | Aloo tikki                        |   69     |"
          "\n|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
    )
def Sandwhich():
    print(  "|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
          "\n|  CODE |         ITEM NAME                 | PRICE(Rs)|"
          "\n|- - - -| - - - - - - - - - - - - - - - - - |- - - - - |"
          "\n|  401  | Paneer Paradise Platter           |   249    |"
          "\n|  402  | Tandoori Vegetable Tango          |   212    |"
          "\n|  403  | Veggie Kebab Carnival             |   199    |"
          "\n|  404  | Achari Avocado Adventure          |   179    |"
          "\n|  405  | Cheese Chutney                    |   099    |"
          "\n|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
    )
def others():
    print(  "|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
          "\n|  CODE |         ITEM NAME                 | PRICE(Rs)|"
          "\n|- - - -| - - - - - - - - - - - - - - - - - |- - - - - |"
          "\n|  501  | Pav Bhaji                         |   151    |"
          "\n|  502  | Masala Dosa                       |   119    |"
          "\n|  503  | Manchurian(Dry)                   |    99    |"
          "\n|  504  | Paneer Chilli                     |   199    |"
          "\n|  505  | Hara-Bhara Kebab                  |   151    |"
          "\n|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
    )
def Beverages():
    print(  "|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
          "\n|  CODE |         ITEM NAME                 | PRICE(Rs)|"
          "\n|- - - -| - - - - - - - - - - - - - - - - - |- - - - - |"
          "\n|  601  | Sex on the beach                  |   151    |"
          "\n|  602  | Melon Magic Infusion              |   119    |"
          "\n|  603  | Blueberry Breeze Bliss            |    99    |"
          "\n|  604  | Vanilla Velvet Dream              |   199    |"
          "\n|  605  | Berry Burst Elixir                |   151    |"
          "\n|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
    )
def Desserts():
    print(  "|- - - - - - - - - - - - - - - - - - - - - - - - - - - |"
          "\n|  CODE |         ITEM NAME                 | PRICE(Rs)|"
          "\n|- - - -| - - - - - - - - - - - - - - - - - |- - - - - |"
          "\n|  701  | Caramel Dream Delight             |   249    |"
          "\n|  702  | Pistachio Paradise                |   210    |"
          "\n|  703  | Blueberry Cheese Cake             |   199    |"
          "\n|  704  | Coffee Caramel Cascade            |   199    |"
          "\n|  705  | Choco Truffle Brownie             |   149    |"
          "\n|- - - - - - - - - - - - - - - - - - - - - - - - - - - |")
    
def display_menu(menu):
    table = PrettyTable()
    table.field_names = ["Code", "Item", "Price (Rs)"]

    for code, details in menu.items():
        table.add_row([code, details["item"], details["price"]])

    print(table)

def display_orders():
    if not orders1:
        print("No orders yet.")
        return

    print("\nCurrent Orders:")
    table = PrettyTable()
    table.field_names = ["Code", "Item", "Quantity", "Total Price (Rs)"]

    for code, item in zip(orderscode, orders1):
        quantity = orders1.count(item)
        total_price = menu[code]["price"] * quantity
        table.add_row([code, item, quantity, total_price])

    print(table)
    print(f"Total Cost: RS {totalprice}\n")

def take_order(menu):
    global totalprice
    orders = []
    while True:
        print("What do you want to order from above? ")
        c = int(input("Enter the code of the item you want to eat: "))

        if c in menu:
            d = int(input("Enter the quantity of your order (or press 00 to exit): "))
            if d == 0:
                break
            order_price = menu[c]['price'] * d
            print(f"{Fore.YELLOW}{menu[c]['item']}: RS {order_price}{Style.RESET_ALL}")
            orders.append((menu[c]['item'], d, order_price))
            orders1.append((menu[c]['item'], d, order_price))
            orderscode.append(c)
            totalprice += order_price
            print("Orders1 after append:", orders1)
            e = int(input("(1) Add items (0) Back to menu "))
            if e == 0:
                break
        else:
            print(f"{Fore.RED}Invalid code. Please enter a valid code from the menu.{Style.RESET_ALL}")
            speech.say("Invalid code. Please enter a valid code from the menu.")
            speech.runAndWait()

    print("\nYour Orders:")
    for item, quantity, price in orders:
        print(f"{Fore.CYAN}{item} x{quantity}: RS {price}{Style.RESET_ALL}")
    total_cost = sum(price for _, _, price in orders)
    print(f"{Fore.MAGENTA}Total Cost: RS {total_cost}{Style.RESET_ALL}\n")

def view_records(name, number, orders1, totalprice, mode_of_payment):
    items = [item for item in orders1]
    df = pd.DataFrame({
        'Name': [name],
        'Contact Number': [number],
        'Orders': ['+'.join(map(str, items))],
        'Total Price': [totalprice],
        'Mode of payment':[mode_of_payment]
    })
    try:
        existing_data = pd.read_excel(r"customerdetails1.xlsx",index_col=0)
        df = pd.concat([existing_data, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_excel(r"customerdetails1.xlsx", index=True)

def delete_specific_record():
    f=pd.read_excel(r"customerdetails1.xlsx",index_col=0)
    print(f)
    index_number=int(input("Enter the Serial number of the record you want to delete:"))
    k=str(input("Are you sure you want to delete?(Y/N)"))
    if k.lower()=='y':
        f=f.drop(f.index[index_number])
        f = f.reset_index(drop=True)
        f.to_excel(r"customerdetails1.xlsx", index=True)
        print("Record deleted successfully.")
    elif k.lower()=='n':
        admin_Menu()

def delete_records(file_path):
    workbook = op.Workbook()
    workbook.save(file_path)


def print_bill(name, number, orders1, totalprice, payment_method):
    print("\n------------------------BILL------------------------")
    print(f"Customer Name: {Fore.GREEN}{name}{Style.RESET_ALL}")
    print(f"Mobile Number: {Fore.GREEN}{number}{Style.RESET_ALL}")

    items_table = PrettyTable()
    items_table.field_names = [Fore.BLUE + "Item", Fore.BLUE + "Quantity", Fore.BLUE + "Price (RS)" + Style.RESET_ALL]

    for item, quantity, price in orders1:
        items_table.add_row([item, quantity, price])

    print(items_table)

    print(f"Total Price: {Fore.YELLOW}{totalprice}{Style.RESET_ALL}")
    gst = totalprice * 0.18
    print(f"GST (18%): {Fore.YELLOW}{gst}{Style.RESET_ALL}")
    total_with_gst = totalprice + gst
    print(f"Total with GST: {Fore.YELLOW}{total_with_gst}{Style.RESET_ALL}")
    print(f"Payment Method: {Fore.CYAN}{payment_method}{Style.RESET_ALL}")
    print("---------------------------------------------------")

    time.sleep(3)

def details():
    global orders1, totalprice, payment_method

    name = input("Enter your name: ")
    while True:
        number = input("Enter contact number: ")
        if len(number) == 10 and number.isdigit():
            print("\nYour Orders:")
            for order in orders1:
                item, quantity, price = order
                print(f"{item} x{quantity}: RS {price}")

            if not orders1:
                print("No orders found.")

            print(f"Total Cost: RS {totalprice}\n")
            confirmation = input("Confirm your order (yes/no): ").lower()
            while confirmation not in ['yes', 'no']:
                print("Invalid input. Please enter 'yes' or 'no'.")
                confirmation = input("Confirm your order (yes/no): ").lower()
            if confirmation == "yes":
                while True:
                    payment_method = input("Will you pay using cash or UPI? ").lower()
                    if payment_method!='cash' and payment_method!='upi':
                        print("Enter valid method.")
                        continue
                    else:
                        view_records(name, number, orders1,totalprice, payment_method)
                        print("Generating bill....")
                        speech.say("Your order is confirmed. Generating bill.")
                        speech.runAndWait()
                        print_bill(name, number, orders1, totalprice, payment_method)
                        orders1=[]
                        totalprice=0
                        Main_Menu()
            elif confirmation == "no":
                orders1 = []
                totalprice = 0
                print("Order cancelled. Starting a new order.")
                speech.say("Order cancelled. Starting a new order.")
                speech.runAndWait()
                Main_Menu()
def admin_Menu():
    while True:
                k=int(input("1.View previous records\n2.Delete a specific record\n3.Delete all records\n4.Back to main menu\n\tEnter choice:"))
                if k==1:
                    f=pd.read_excel(r"customerdetails1.xlsx",index_col=0)
                    if f.empty:
                        print("No records found.")
                    else:
                        print(f)
                elif k==2:
                    delete_specific_record()
                elif k==3:
                    ask=str(input("Are you sure you want to delete the existing records?(y/n):"))
                    if ask=='y':
                        delete_records(r"customerdetails1.xlsx")
                        print("Records deleted.")
                        break
                    else:
                        break
                elif k==4:
                    Main_Menu()
def Main_Menu():
    start()
    print("*Main Menu*\nSelect Your Choice\n( 1 )Admin Menu\n( 2 )Customer Menu\n( 3 )Exit\n")
    a = int(input("Enter Your Choice here: "))
    if a==1:
        admin_Menu()
    elif a==2:
        global orders1, totalprice, payment_method
        while True:
            print("\n\t***Menu***\nChoose your appropriate option ")
            print("  (1)VEG COMBOS 🌽\n  (2)PIZZA 🍕\n  (3)VEG BURGERS 🍔\n  (4)SANDWICH 🥪\n  (5)DESSERTS 🍰\n  (6)BEVERAGES 🥤\n  (7)OTHERS 🛒\n  (8)BILLING 💳\n  (9)MISORDER ❌\n  (10)BACK TO MAIN MENU ⬅️\n  (11)EXIT 🚪")
            b = int(input("Enter your choice: "))
            if b == 1:
                Combo_menu()
                take_order(menu)
            elif b == 2:
                Pizza()
                take_order(menu1)
            elif b == 3:
                Burgers()
                take_order(menu2)
            elif b == 4:
                Sandwhich()
                take_order(menu3)
            elif b == 5:
                Desserts()
                take_order(menu6)
            elif b == 6:
                Beverages()
                take_order(menu5)
            elif b == 7:
                others()
                take_order(menu4)
            elif b == 8:
                details()
            elif b == 10:
                Main_Menu()
            elif b == 11:
                if orders1 and payment_method.lower() not in ['cash', 'upi']:
                        print("Please pay the bill first.")
                        details()
                else:
                        print("Exiting. Have a nice day!")
                        break
            
            elif b==9:
                orders1 = []
                totalprice
                totalprice = 0
                print("Order discarded. Start a new order.")
            else:
                print("Invalid choice. Please enter a valid option.")
    elif a==3:
                if orders1 and payment_method.lower() not in ['cash', 'upi']:
                        print("Please pay the bill first.")
                        details()
                else:
                    while True:
                        print("Exiting. Have a nice day!")
                        exit()
            
Main_Menu()
