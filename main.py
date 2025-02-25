from smartphone import Smartphone
from laptop import Laptop
from tablet import Tablet
from cart import Cart
import os
import time

devices = [
    Smartphone("Samsung Galaxy S21", 999.99, 6, 6, "1080x2400", 4000),
    Smartphone("iPhone 13", 1099.99, 10, 12, "1170x2532", 3095),
    Smartphone("Google Pixel 6", 899.99, 8, 8, "1080x2400", 4614),
    Smartphone("OnePlus 9", 729.99, 5, 5, "1080x2400", 4500),
    Smartphone("Xiaomi Mi 11", 799.99, 7, 7, "1440x3200", 4600),
    Smartphone("Sony Xperia 1 III", 1299.99, 4, 4, "1644x3840", 4500),
    Smartphone("Oppo Find X3 Pro", 1149.99, 6, 6, "1440x3216", 4500),
    Smartphone("Huawei P50 Pro", 1199.99, 3, 3, "1228x2700", 4360),
    Smartphone("Asus ROG Phone 5", 999.99, 9, 9, "1080x2448", 6000),
    Smartphone("Nokia 8.3 5G", 699.99, 8, 8, "1080x2400", 4500),
    Laptop("MacBook Pro", 1299.99, 50, 7, "13-inch", "Apple M1"),
    Laptop("Dell XPS 13", 999.99, 30, 12, "13.3-inch", "Intel i7"),
    Laptop("HP Spectre x360", 1199.99, 20, 24, "13.3-inch", "Intel i7"),
    Laptop("Lenovo ThinkPad X1", 1399.99, 15, 36, "14-inch", "Intel i7"),
    Laptop("Microsoft Surface Laptop 4", 1299.99, 25, 18, "13.5-inch", "AMD Ryzen 5"),
    Laptop("Asus ZenBook 13", 899.99, 40, 12, "13.3-inch", "Intel i5"),
    Laptop("Acer Swift 3", 699.99, 35, 24, "14-inch", "AMD Ryzen 7"),
    Laptop("Razer Blade 15", 1599.99, 10, 24, "15.6-inch", "Intel i7"),
    Laptop("LG Gram 17", 1699.99, 8, 36, "17-inch", "Intel i7"),
    Laptop("Samsung Galaxy Book Pro", 1099.99, 20, 18, "15.6-inch", "Intel i5"),
    Tablet("iPad Pro", 799.99, 75, 4, "12.9-inch", "Apple M1"),
    Tablet("Samsung Galaxy Tab S7", 649.99, 50, 6, "11-inch", "Snapdragon 865+"),
    Tablet("Microsoft Surface Pro 7", 749.99, 40, 12, "12.3-inch", "Intel i5"),
    Tablet("Amazon Fire HD 10", 149.99, 100, 2, "10.1-inch", "Mediatek MT8183"),
    Tablet("Lenovo Tab P11 Pro", 499.99, 30, 6, "11.5-inch", "Snapdragon 730G"),
    Tablet("Huawei MatePad Pro", 549.99, 25, 8, "10.8-inch", "Kirin 990"),
    Tablet("Asus Chromebook Tablet CT100", 329.99, 20, 12, "9.7-inch", "OP1 Hexa-core"),
    Tablet("Google Pixel Slate", 799.99, 15, 18, "12.3-inch", "Intel i5"),
    Tablet("Sony Xperia Z4 Tablet", 599.99, 10, 24, "10.1-inch", "Snapdragon 810"),
    Tablet("Dell Latitude 7220 Rugged Extreme", 1999.99, 5, 36, "11.6-inch", "Intel i7")
]

cart = Cart()

while True:
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
        cart.print_items()
        print(f"Total Price: {cart.get_total_price()}")

    else:
        print("Invalid option")
        continue
