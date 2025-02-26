from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet
from cart import Cart
import os
import time

devices = [
    Smartphone("Samsung Galaxy S21", 999.99, 6, 6, 6.2, 24),
    Smartphone("iPhone 13", 1099.99, 10, 12, 6.1, 22),
    Smartphone("Google Pixel 6", 899.99, 8, 8, 6.4, 25),
    Smartphone("OnePlus 9", 729.99, 5, 5, 6.55, 23),
    Smartphone("Xiaomi Mi 11", 799.99, 7, 7, 6.81, 26),
    Smartphone("Sony Xperia 1 III", 1299.99, 4, 4, 6.5, 24),
    Smartphone("Oppo Find X3 Pro", 1149.99, 6, 6, 6.7, 25),
    Smartphone("Huawei P50 Pro", 1199.99, 3, 3, 6.6, 24),
    Smartphone("Asus ROG Phone 5", 999.99, 9, 9, 6.78, 30),
    Smartphone("Nokia 8.3 5G", 699.99, 8, 8, 6.81, 27),
    Laptop("MacBook Pro", 1299.99, 50, 7, 16, 3.2),
    Laptop("Dell XPS 13", 999.99, 30, 12, 16, 3.1),
    Laptop("HP Spectre x360", 1199.99, 20, 24, 16, 3.0),
    Laptop("Lenovo ThinkPad X1", 1399.99, 15, 36, 16, 3.3),
    Laptop("Microsoft Surface Laptop 4", 1299.99, 25, 18, 16, 3.0),
    Laptop("Asus ZenBook 13", 899.99, 40, 12, 8, 2.8),
    Laptop("Acer Swift 3", 699.99, 35, 24, 8, 2.9),
    Laptop("Razer Blade 15", 1599.99, 10, 24, 16, 3.2),
    Laptop("LG Gram 17", 1699.99, 8, 36, 16, 3.1),
    Laptop("Samsung Galaxy Book Pro", 1099.99, 20, 18, 8, 2.7),
    Tablet("iPad Pro", 799.99, 75, 4, "2732x2048", 468),
    Tablet("Samsung Galaxy Tab S7", 649.99, 50, 6, "2560x1600", 498),
    Tablet("Microsoft Surface Pro 7", 749.99, 40, 12, "2736x1824", 775),
    Tablet("Amazon Fire HD 10", 149.99, 100, 2, "1920x1200", 504),
    Tablet("Lenovo Tab P11 Pro", 499.99, 30, 6, "2560x1600", 485),
    Tablet("Huawei MatePad Pro", 549.99, 25, 8, "2560x1600", 460),
    Tablet("Asus Chromebook Tablet CT100", 329.99, 20, 12, "2048x1536", 568),
    Tablet("Google Pixel Slate", 799.99, 15, 18, "3000x2000", 731),
    Tablet("Sony Xperia Z4 Tablet", 599.99, 10, 24, "2560x1600", 389),
    Tablet("Dell Latitude 7220 Rugged Extreme", 1999.99, 5, 36, "1920x1080", 1300)
]

cart = Cart()

while True:
    os.system("clear")
    option = input("1. Show Devices\n2. Show Cart\n3. Exit\n")

    if option == "3":
        break

    elif option == "1":

        while True:
            os.system("clear")
            for i in range(len(devices)):
                print(devices[i])
                print(f"{i + 1}. Add to cart")
                print("-------" * 5)

            opt = input(f"0. Go back\n{'-------' * 5}\n")

            if opt == "0":
                os.system("clear")
                break
            else:
                try:
                    print(devices[int(opt) - 1].name)
                    amount = int(input("Enter amount: "))
                    cart.add_device(devices[int(opt) - 1], amount)
                    time.sleep(1)
                except IndexError:
                    print("Invalid option")
                    time.sleep(1)
                    continue

    elif option == "2":
        os.system("clear")
        print("Your Cart:")
        cart.print_items()
        print("-------" * 5)
        print(f"Total Price: {round(cart.get_total_price(), 2)} USD")
        input("\n\nPress enter to continue... ")

    else:
        print("Invalid option")
        time.sleep(1)
        continue