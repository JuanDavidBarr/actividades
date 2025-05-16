flight_information = {}
passangers = 0
passangers_international = 0
passangers_national = 0
#adding flight information
def add_f_information():
    global passangers
    global passangers_international
    global passangers_national
    counter = 1
    another_ticket = "yes"
    while another_ticket == "yes": 

        name = input("Please, type your name: ")
        while True:
            travel_type = input("Please, indicate the type of flight (national/international): ").lower().strip()
            if travel_type != "national" and travel_type != "international":
                print("Please, only 'international' or 'national' answers")
            else:
                break
        if travel_type == "national":
            passangers_national += 1
        elif travel_type == "international":
            passangers_international += 1
        destination = input("Please, introduce your destination: ")
        is_number = "no"
        is_positive = "no"
        while is_number == "no" or is_positive == "no":
            try:
                weight_main = int(input("How much is the weight of your luggage?: "))
                is_number = "yes"
                if weight_main >= 0:
                    is_positive = "yes"
                else:
                    print("Please, positive values only")
            except:
                print("Please, numbers only")
        if weight_main <= 50:
            while True:
                hand_luggage = input("Are you carrying hand-luggage? (yes/no): ").lower().strip()
                if hand_luggage != "yes" and hand_luggage != "no":
                    print("Please, 'yes' or 'no' answers only")
                else:
                    break
            if hand_luggage == "yes":
                is_number = "no"
                is_positive = "no"
                while is_number == "no" or is_positive == "no":
                    try:
                        weight_h_luggage = int(input("Indicate your hand luggage weight: "))
                        is_number = "yes"
                        if weight_h_luggage >= 0:
                            is_positive = "yes"
                        else:
                            print("Please, positive values only")
                    except:
                        print("Please, numbers only")
                if weight_h_luggage >= 13:
                    user_decision = input("The weight of your hand luggage exceeds the maximum allowed (13kg). You can either travel without it (1) or not travel with us (2): ")
                    if user_decision == "1":
                        weight_h_luggage = 0
                    elif user_decision == "2":
                        print("You have decided not to continue with your booking. You will be redirected to the options menu")
                        menu()       
            else:
                weight_h_luggage = 0
            date = input("What day are you travelling? (dd/mm/yy): ")
            flight_information["COMP000" + str(counter)] = {"Name" : name, "Flight type" : travel_type, 
                                                            "Main weight" : weight_main, "Destination": destination,
                                                            "Carries hand luggage" : hand_luggage, 
                                                            "Weight hand luggage" : weight_h_luggage,
                                                            "Date" : date}
            while True:
                another_ticket = input("Do you want to add more information? (yes/no): ").lower().strip()
                if another_ticket != "yes" and another_ticket != "no":
                    print("Please, 'yes' or 'no' answers only")
                else:
                    break
                if another_ticket == "yes":
                    counter += 1
                passangers += 1
        elif weight_main > 50:
            user_decision = input("The weight of your main luggage is way too heavy. You can either cancel your book (2) "
            "or travel without it (1). What do you want to do? ")
            if user_decision == "1":
                weight_main = 0
                while True:
                    hand_luggage = input("Are you carrying hand-luggage? (yes/no): ")
                    if hand_luggage != "yes" and hand_luggage != "no":
                        print("Please, 'yes' or 'no' answers only")
                    else:
                        break
                if hand_luggage == "yes":
                    is_positive = "no"
                    is_number = "no"
                    while is_number == "no" or is_positive == "no":
                        try:
                            weight_h_luggage = int(input("Indicate your hand luggage weight: "))
                            is_number = "yes"
                            if weight_h_luggage >= 0:
                                is_positive = "yes"
                            else:
                                print("Please, positive values only")
                        except:
                            print("Please, numbers only")
                    if weight_h_luggage >= 13:
                        user_decision = input("The weight of your hand luggage exceeds the maximum allowed (13kg). You can either travel without it (1) or not travel with us (2): ")
                        if user_decision == "1":
                            weight_h_luggage = 0
                        elif user_decision == "2":
                            print("You have decided not to continue with your booking. You will be redirected to the options menu")
                            menu()
                else:
                    weight_h_luggage = 0
                date = input("What day are you travelling? (dd/mm/yy): ")
                flight_information["COMP000" + str(counter)] = {"Name" : name, "Flight type" : travel_type, 
                                                            "Main weight" : weight_main, "Destination" : destination,
                                                            "Carries hand luggage" : hand_luggage, 
                                                            "Weight hand luggage" : weight_h_luggage,
                                                        "Date" : date}
                while True:
                    another_ticket = input("Do you want to add more information? (yes/no): ")
                    if another_ticket != "yes" and another_ticket != "no":
                        print("Please, 'yes' or 'no' answers only")
                    else:
                        break
                    if another_ticket == "yes":
                        counter += 1
                    passangers += 1

            elif user_decision == "2":
                print("You have decided not to continue with your booking.")
                while True:
                    another_ticket = input("Do you want to add more information? (yes/no): ")
                    if another_ticket != "yes" and another_ticket != "no":
                        print("Please, 'yes' or 'no' answers only")
                    else:
                        break
            else:
                print("Invalid answer, '1' or '2' only. You will be redirected to the menu")
                menu()


#Final reports for administrators:
def total_purchases():
#Total purchases:
    values_list = list(flight_information.values())
    purchases_list = []
    main_luggage_list = []
    light_luggage = []
    medium_luggage = []
    heavy_luggage = []
    forbidden_luggage = []
    for value in values_list:
        purchases_list.append(value["Flight type"])
        main_luggage_list.append(value["Main weight"])
    times_national = purchases_list.count("national")
    times_international = purchases_list.count("international")
    value_for_tickets = (times_international * 230000) + (times_national * 4200000)
    for element in main_luggage_list:
        if 0 < element <= 20:
            light_luggage.append(element)
        elif 20 < element <= 30:
            medium_luggage.append(element)
        elif 30 < element <= 50:
            heavy_luggage.append(element)
        elif element > 50:
            forbidden_luggage.append(element)
    value_for_m_luggage = (len(light_luggage) * 50000) + (len(medium_luggage) * 70000) + (len(heavy_luggage) * 110000)
    total_value = value_for_tickets + value_for_m_luggage
    print(f"Total value for purchases is {total_value}")
#Total purchases specific date
def total_purchases_date():
    admin_date = input("Introduce the date of your flight: ")
    values_list = list(flight_information.values())
    purchases_list = []
    main_luggage_list = []
    light_luggage = []
    medium_luggage = []
    heavy_luggage = []
    forbidden_luggage = []
    for value in values_list:
        if value["Date"] == admin_date:
            purchases_list.append(value["Flight type"])
            main_luggage_list.append(value["Main weight"])
    else:
        print(f"{admin_date} is not in the record")
    times_national = purchases_list.count("national")
    times_international = purchases_list.count("international")
    value_for_tickets = (times_international * 230000) + (times_national * 4200000)
    for element in main_luggage_list:
        if 0 < element <= 20:
            light_luggage.append(element)
        elif 20 < element <= 30:
            medium_luggage.append(element)
        elif 30 < element <= 50:
            heavy_luggage.append(element)
        elif element > 50:
            forbidden_luggage.append(element)
    value_for_m_luggage = (len(light_luggage) * 50000) + (len(medium_luggage) * 70000) + (len(heavy_luggage) * 110000)
    total_value = value_for_tickets + value_for_m_luggage
    print(f"Total value for purchases in {admin_date} is {total_value}")

#number of passangers
def total_passangers():
    global passangers
    print(f"Total of passangers is {passangers}")


#number of passangers according to destination
def total_passangers_dest():
    global passangers_national
    global passangers_international
    print(f"""Total international passangers is {passangers_international} 
          \nTotal national passangers is {passangers_national}""")
    


#search by using ID
def serch_ID():
    user_id = input("Please, enter the ID: ")
    if flight_information.get(user_id) != None:
        print(f"Information of the ID {user_id}:")
        for key, value in flight_information.get(user_id).items():
            print(f"{key}: {value}")
        if flight_information.get(user_id)["Flight type"] == "national":
            print(f"cost: {230000}")
        else:
            print(f"cost: {4200000}") 
    else:
        print(f"{user_id} is not in the record")



#menu
def menu():
    users_option = input("choose an option: ")
    if users_option == "1":
        add_f_information()
    elif users_option == "2":
        total_purchases()
    elif users_option == "3":
        total_purchases_date()
    elif users_option == "4":
        total_passangers()
    elif users_option == "5":
        total_purchases_date()
    elif users_option == "6":
        serch_ID()


menu()





    




