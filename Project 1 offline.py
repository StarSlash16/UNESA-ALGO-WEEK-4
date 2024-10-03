def pizza_ordering_system():
    pepper_count = 0
    pepper_stuffed_count = 0
    pepper_cheese_count = 0
    pepper_top_count = 0
    cheese_count = 0
    cheese_stuffed_count = 0
    cheese_cheese_count = 0
    cheese_top_count = 0
    pine_count = 0
    pine_stuffed_count = 0
    pine_cheese_count = 0
    pine_top_count = 0
    meat_count = 0
    meat_stuffed_count = 0
    meat_cheese_count = 0
    meat_top_count = 0
    bread_count = 0
    soup_count = 0
    french_count = 0
    coca_count = 0
    teb_count = 0
    pop_count = 0
    choco_count = 0
    van_count = 0
    str_count = 0
    wat_count = 0
    pepper_cost = 0
    pepper_stuffed_cost = 0
    pepper_cheese_cost = 0
    pepper_top_cost = 0
    cheese_cost = 0
    cheese_stuffed_cost = 0
    cheese_cheese_cost = 0
    cheese_top_cost = 0
    pine_cost = 0
    pine_stuffed_cost = 0
    pine_cheese_cost = 0
    pine_top_cost = 0
    meat_cost = 0
    meat_stuffed_cost = 0
    meat_cheese_cost = 0
    meat_top_cost = 0
    bread_cost = 0
    soup_cost = 0
    french_cost = 0
    coca_cost = 0
    teb_cost = 0
    pop_cost = 0
    choco_cost = 0
    van_cost = 0
    str_cost = 0
    wat_cost = 0


    keep_looping = 1

    while keep_looping == 1:
        print ("Which pizza would you like to order today?")
        print("1) Pepperoni Pizza      :Rp. 24000")
        print("2) Cheese Pizza         :Rp. 23000")
        print("3) Hawaiian Pizza       :Rp. 26000")
        print("4) Meat Pizza           :Rp. 29000")
        print("-) Next")
        pizza_order=int(input("Order :"))
        print("")

        if 1 <= pizza_order <= 4 :
            print("Any addition?")
            print("1) Stuffed Crust         :+ Rp.  7000")
            print("2) Extra Cheese          :+ Rp.  4000")
            print("3) Extra Topping         :+ Rp.  5000")
            print("4) No Addition           :+ Rp.     0")
            print("-) Return")
            pizza_topping = int(input("Order :"))
            print("")

            if pizza_order == 1 and pizza_topping == 1:
                print(f"Total Ordered = {pepper_stuffed_count} ")
                pepper_stuffed_count = int(input("How many? :"))
                print("")
            elif pizza_order == 1 and pizza_topping == 2:
                print(f"Total Ordered = {pepper_cheese_count} ")
                pepper_cheese_count = int(input("How many? :"))
                print("")
            elif pizza_order == 1 and pizza_topping == 3:
                print(f"Total Ordered = {pepper_top_count} ")
                pepper_top_count = int(input("How many? :"))
                print("")
            elif pizza_order == 1 and pizza_topping == 4:
                print(f"Total Ordered = {pepper_count} ")
                pepper_count = int(input("How many? :"))
                print("")
            elif pizza_order == 2 and pizza_topping == 1:
                print(f"Total Ordered = {cheese_stuffed_count} ")
                cheese_stuffed_count = int(input("How many? :"))
                print("")
            elif pizza_order == 2 and pizza_topping == 2:
                print(f"Total Ordered = {cheese_cheese_count} ")
                cheese_cheese_count = int(input("How many? :"))
                print("")
            elif pizza_order == 2 and pizza_topping == 3:
                print(f"Total Ordered = {cheese_top_count} ")
                cheese_top_count = int(input("How many? :"))
                print("")
            elif pizza_order == 2 and pizza_topping == 4:
                print(f"Total Ordered = {cheese_count} ")
                cheese_count = int(input("How many? :"))
                print("")
            elif pizza_order == 3 and pizza_topping == 1:
                print(f"Total Ordered = {pine_stuffed_count} ")
                pine_stuffed_count = int(input("How many? :"))
                print("")
            elif pizza_order == 3 and pizza_topping == 2:
                print(f"Total Ordered = {pine_cheese_count} ")
                pine_cheese_count = int(input("How many? :"))
                print("")
            elif pizza_order == 3 and pizza_topping == 3:
                print(f"Total Ordered = {pine_top_count} ")
                pine_top_count = int(input("How many? :"))
                print("")
            elif pizza_order == 3 and pizza_topping == 4:
                print(f"Total Ordered = {pine_count} ")
                pine_count = int(input("How many? :"))
                print("")
            elif pizza_order == 4 and pizza_topping == 1:
                print(f"Total Ordered = {meat_stuffed_count} ")
                meat_stuffed_count = int(input("How many? :"))
                print("")
            elif pizza_order == 4 and pizza_topping == 2:
                print(f"Total Ordered = {meat_cheese_count} ")
                meat_cheese_count = int(input("How many? :"))
                print("")
            elif pizza_order == 4 and pizza_topping == 3:
                print(f"Total Ordered = {meat_top_count} ")
                meat_top_count = int(input("How many? :"))
                print("")
            elif pizza_order == 4 and  pizza_topping == 4:
                print(f"Total Ordered = {meat_count} ")
                meat_count = int(input("How many? :"))
                print("")
            else:
                keep_looping = 1
        else:
            keep_looping = 2

    keep_looping = 1

    while keep_looping == 1:
        print("Additional side dish?")
        print("1) Bread stick            :Rp. 11000")
        print("2) Soup                   :Rp.  6000")
        print("3) French Fries           :Rp. 12000")
        print("-) Next")
        side_order=int(input("Order :"))
        print("")

        if side_order == 1:
            print(f"Total Ordered = {bread_count} ")
            bread_count = int(input("How many? :"))
            print("")
        elif side_order == 2:
            print(f"Total Ordered = {soup_count} ")
            soup_count = int(input("How many? :"))
            print("")
        elif side_order == 3:
            print(f"Total Ordered = {french_count} ")
            french_count = int(input("How many? :"))
            print("")
        else:
            keep_looping = 2

    keep_looping = 1

    while keep_looping == 1:
        print("Additional drinks?")
        print("1) Soda                   :(...)")
        print("2) Milkshake              :(...)")
        print("3) Water Bottle           :Rp.  5000")
        print("-) Next")
        drink_order=int(input("Order :"))
        print("")

        if drink_order == 1:
            print("Which soda do you want?")
            print("1) Coca-Cola              :Rp.  5000")
            print("2) Teb                    :Rp.  6000")
            print("3) Pepsi                  :Rp.  5500")
            print("-) Return")
            soda_order=int(input("Order :"))
            print("")

            if soda_order == 1:
                print(f"Total Ordered = {coca_count} ")
                coca_count = int(input("How many? :"))
                print("")
            elif soda_order == 2:
                print(f"Total Ordered = {teb_count} ")
                teb_count = int(input("How many? :"))
                print("")
            elif soda_order == 3:
                print(f"Total Ordered = {pop_count} ")
                pop_count = int(input("How many? :"))
                print("")
            else:
                keep_looping = 1

        elif drink_order == 2:
            print("Which milkshake do you want?")
            print("1) Chocolate Milkshake    :Rp. 16000")
            print("2) Vanilla Milkshake      :Rp. 15000")
            print("3) Strawberry Milkshake   :Rp. 16000")
            print("-) Return")
            milkshake_order=int(input("Order :"))
            print("")

            if milkshake_order == 1:
                print(f"Total Ordered = {choco_count} ")
                choco_count = int(input("How many? :"))
                print("")
            elif milkshake_order == 2:
                print(f"Total Ordered = {van_count} ")
                van_count = int(input("How many? :"))
                print("")
            elif milkshake_order == 3:
                print(f"Total Ordered = {str_count} ")
                str_count = int(input("How many? :"))
                print("")
            else:
                keep_looping = 1

        elif drink_order == 3:
            print(f"Total Ordered = {wat_count} ")
            wat_count = int(input("How many? :"))
            print("")

        else:
            keep_looping = 2

    keep_looping = 1

    while keep_looping == 1:
        print("Here's your order :")
        if pepper_count > 0:
            pepper_cost = 24000 * pepper_count
            print(f"Pepperoni Pizza                 ({pepper_count}) :Rp. {pepper_cost}")
        if pepper_stuffed_count > 0:
            pepper_stuffed_cost = (24000 + 7000) * pepper_stuffed_count
            print(f"Pepperoni Pizza [Stuffed Crust] ({pepper_stuffed_count}) :Rp. {pepper_stuffed_cost}")
        if pepper_cheese_count > 0:
            pepper_cheese_cost = (24000 + 4000) * pepper_cheese_count
            print(f"Pepperoni Pizza [Extra Cheese]  ({pepper_cheese_count}) :Rp. {pepper_cheese_cost}")
        if pepper_top_count > 0:
            pepper_top_cost = (24000 + 4000) * pepper_top_count
            print(f"Pepperoni Pizza [Extra Topping] ({pepper_top_count}) :Rp. {pepper_top_cost}")

        if cheese_count > 0:
            cheese_cost = 23000 * cheese_count
            print(f"Cheese Pizza                    ({cheese_count}) :Rp. {cheese_cost}")
        if cheese_stuffed_count > 0:
            cheese_stuffed_cost = (23000 + 7000) * cheese_stuffed_count
            print(f"Cheese Pizza [Stuffed Crust]    ({cheese_stuffed_count}) :Rp. {cheese_stuffed_cost}")
        if cheese_cheese_count > 0:
            cheese_cheese_cost = (23000 + 4000) * cheese_cheese_count
            print(f"Cheese Pizza                    ({cheese_cheese_count}) :Rp. {cheese_cheese_cost}")
        if cheese_top_count > 0:
            cheese_top_cost = (23000 + 5000) * cheese_top_count
            print(f"Cheese Pizza [Extra Topping]    ({cheese_top_count}) :Rp. {cheese_top_cost}")

        if pine_count > 0:
            pine_cost = 26000 * pine_count
            print(f"Hawaiian Pizza                  ({pine_count}) :Rp. {pine_cost}")
        if pine_stuffed_count > 0:
            pine_stuffed_cost = (26000 + 7000) * pine_stuffed_count
            print(f"Hawaiian Pizza [Stuffed Crust]  ({pine_stuffed_count}) :Rp. {pine_stuffed_cost}")
        if pine_cheese_count > 0:
            pine_cheese_cost = (26000 + 4000) * pine_cheese_count
            print(f"Hawaiian Pizza [Extra Cheese]   ({pine_cheese_count}) :Rp. {pine_cheese_cost}")
        if pine_top_count > 0:
            pine_top_cost = (26000 + 5000) * pine_top_count
            print(f"Hawaiian Pizza [Extra Topping]  ({pine_top_count}) :Rp. {pine_top_cost}")

        if meat_count > 0:
            meat_cost = 24000 * meat_count
            print(f"Meat Pizza                      ({meat_count}) :Rp. {meat_cost}")
        if meat_stuffed_count > 0:
            meat_stuffed_cost = (29000 + 7000) * meat_stuffed_count
            print(f"Meat Pizza [Stuffed Crust]      ({meat_stuffed_count}) :Rp. {meat_stuffed_cost}")
        if meat_cheese_count > 0:
            meat_cheese_cost = (29000 + 4000) * meat_cheese_count + 4000
            print(f"Meat Pizza [Extra Cheese]       ({meat_cheese_count}) :Rp. {meat_cheese_cost}")
        if meat_top_count > 0:
            meat_top_cost = (29000 + 5000) * meat_top_count
            print(f"Meat Pizza [Extra Topping]      ({meat_top_count}) :Rp. {meat_top_cost}")

        if bread_count > 0:
            bread_cost = 11000 * bread_count
            print(f"Bread Stick                     ({bread_count}) :Rp. {bread_cost}")
        if soup_count > 0:
            soup_cost = 6000 * soup_count
            print(f"Soup                            ({soup_count}) :Rp. {soup_cost}")
        if french_count > 0:
            french_cost = 12000 * french_count
            print(f"French Fries                    ({french_count}) :Rp. {french_cost}")

        if coca_count > 0:
            coca_cost = 5000 * coca_count
            print(f"Coca-Cola                       ({coca_count}) :Rp. {coca_cost}")
        if teb_count > 0:
            teb_cost = 6000 * teb_count
            print(f"Teb                             ({teb_count}) :Rp. {teb_cost}")
        if pop_count > 0:
            pop_cost = 5500 * pop_count
            print(f"Pepsi                           ({pop_count}) :Rp. {pop_cost}")

        if choco_count > 0:
            choco_cost = 16000 * choco_count
            print(f"Chocolate Milkshake             ({choco_count}) :Rp. {choco_cost}")
        if van_count > 0:
            van_cost = 15000 * van_count
            print(f"Vanilla Milkshake               ({van_count}) :Rp. {van_cost}")
        if str_count > 0:
            str_cost = 16000 * str_count
            print(f"Strawberry Milkshake            ({str_count}) :Rp. {str_cost}")

        if wat_count > 0:
            wat_cost = 5500 * wat_count
            print(f"Water Bottle                    ({wat_count}) :Rp. {wat_cost}")

        print("_______________________________________________+")
        total_cost = pepper_cost + pepper_stuffed_cost + pepper_cheese_cost + pepper_top_cost + cheese_cost + cheese_stuffed_cost + cheese_cheese_cost + cheese_top_cost + pine_cost + pine_stuffed_cost + pine_cheese_cost + pine_top_cost + meat_cost + meat_stuffed_cost + meat_cheese_cost + meat_top_cost + bread_cost + soup_cost + french_cost + coca_cost + teb_cost + pop_cost + choco_cost + van_cost + str_cost + wat_cost
        print(f"Total                :Rp. {total_cost}")
        print("")
        print("Would this be your order?")
        print("1) Yes, that will be all.")
        print("2) I want to change my order.")
        finalize_order = int(input("Finalize :"))
        print("")

        if finalize_order == 1:
            print(f"Would you like delivery?")
            print("1) Delivery                                    :+ Rp.  5000")
            print("2) Self Pick Up                                :+ Rp.     0")
            print("-) Return")
            delivery_order = int(input("Order :"))
            print("")

            if delivery_order == 1:
                print("With delivery your total will be")
                total_cost = total_cost + 5000
                print(f"Rp. {total_cost}")
                print("Thank you for your purchase and have a great meal and a 'pon' day.")
                exit()

            elif delivery_order == 2:
                print("With self pick up your total will be")
                print(f"Rp. {total_cost}")
                print("We'll wait at location, thank you, and have a 'pon' day.")
                exit()

        elif finalize_order == 2:
            print("Alright please re-order from the beginning.")
            print("")

            pizza_ordering_system()


        else:
            keep_looping = 1




print("Welcome to Mama Pon Online Services, where happiness and fun transverse through cyber space.")

pizza_ordering_system()