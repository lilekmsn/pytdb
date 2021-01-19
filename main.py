
dic = {}
mas = []
while True:
    print("Menu:", "\n"
          "1-Register a new patient?", "\n"
          "2-Enter patient's results and, if possible, wihdraw it if he is completely healthy?", "\n"
          "3-Display all results for a specific patient?", "\n"
          "4-Display statistics?", "\n"
          "5-Show everyone healthy?", "\n")
    print("Enter 1 to register a new patient;", "\n"
            "Enter 2 to display the patient's results and,if possible, display it if he is completely healthy;", "\n"
            "Enter 3 to show all results for a specific patient;", "\n"
            "Enter 4 to show statistics;", "\n"
            "Enter 5 to show all healthy;", "\n"
            "Or enter Q to exit the program.")
    i = input("> ")

    if i == "1":
        print("Write another answer? (Yes/No): ", end="")
        c = input()
        if c == "Yes":
            continue
        print("Enter patient data: ", end="")
        data = input()
        dic[data] = []

        print("Add new patient?: ", end="")
        data_1 = input()
        while data_1 == "Yes":
            print("Enter patient data: ", end="")
            data = input()
            dic[data] = []
            print("Add new patient?: ", end="")
            data_1 = input()
        continue

    if i == "2":
        print("Write another answer? (Yes/No): ", end="")
        a = input()
        if a == "Yes":
            continue
        print("Enter patient data: ", end="")
        patient = input()
        while patient not in dic:
            print("There is no such patient!")
            print("1-Register a new patient?", "\n"
                  "2-Enter another patient?")
            k=input("Choose 1 or 2: ")
            if k=="1":
                print("Enter patient data: ", end="")
                data = input()
                dic[data] = []

                print("Add new patient?: ", end="")
                data_1 = input()
                while data_1 == "Yes":
                    print("Enter patient data: ", end="")
                    data = input()
                    dic[data] = []
                    print("Add new patient?: ", end="")
                    data_1 = input()
                break
            if k=="2":
                print("Enter patient data: ", end="")
                patient = input()
        print("Enter the result (+/-): ", end="")
        result = input()
        dic[patient] += [result]
        line = dic[patient]
        if len(line) == 3 and line[-1] == "-" and line[-2] == "-" and line[-3] == "-":
            print(patient + " is healthy!")
            mas += [patient]
            del dic[patient]

        print("Add other results? (Yes/No): ", end="")
        f = input()
        while f=="Yes":
            print("Enter patient data: ", end="")
            patient = input()
            print("Enter the result (+/-): ", end="")
            result = input()
            dic[patient] += [result]
            if len(dic[patient]) == 3 and dic[patient][-1] == "-" and dic[patient][-2] == "-" and dic[patient][-3] == "-":
                print(patient + " is healthy!")
                mas += [patient]
                del dic[patient]
            print("Add other results? (Yes/No): ", end="")
            f = input()
        continue

    if i == "3":
        print("Write another answer? (Yes/No): ", end="")
        v = input()
        if v == "Yes":
            continue
        print("Whose results to display?: ", end="")
        w = input()
        while w not in dic:
            print("Re - enter patient data: ", end="")
            w = input()
        print(dic.get(w))
        print("Display other results? (Yes/No): ", end="")
        dd = input()
        if dd == "No":
            continue
        else:
            while dd == "Yes":
                print("Whose results to display?: ", end="")
                w = input()
                while w not in dic:
                    print("Re - enter patient data: ", end="")
                    w = input()
                print(dic.get(w))

    if i == "4":
        print("Write another answer? (Yes/No): ", end="")
        m = input()
        if m == "Yes":
            continue
        key = []
        for k in dic.keys():
            key += k
        g = len(key)
        h = len(mas)
        r =int(g + h)
        per=str(g * 100 / r)
        hel=str(h * 100 / r)
        print("Percentage of patients: " + per)
        print("The percentage of healthy: " + hel)

    if i == "5":
        print("Write another answer? (Yes/No): ", end="")
        e = input()
        if e == "Yes":
            continue
        if len(mas)==0:
            print("There are no healthy patients!")
            continue
        print(print('\n'.join(mas)))
        continue

    if i == "Q":
       break