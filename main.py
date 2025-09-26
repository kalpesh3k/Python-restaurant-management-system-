import time
from datetime import date,datetime,timedelta
from tabulate import tabulate
import _strptime
print("*************** WELCOME ***********************")
print("********** RESTAURANT MANAGEMENT BY ~~KALPESHH *****************")
def valid_dish(code):
    f = open("dish.txt", "r")
    for line in f:
        if line.startswith(code + ","):
            f.close()
            return True
    f.close()
    return False
def get_date():
    obj = date.today()
    d = obj.day
    m = obj.month
    y = obj.year
    today_dt = str(d) + "/" + str(m) + "/" + str(y)
    return today_dt
def generate_bill():
    print("********************************************************")
    print("*\t                  GENERATE BILL                     *")
    print("********************************************************")
    fobj = open("dish.txt", "r")
    read_dish = fobj.readlines()
    fobj.close()
    total_cost = 0
    while True:
        enter_code = input("\tEnter Item Code :- ")
        return_val = valid_dish(enter_code)
        if return_val == False:
            print("Invalid Item Code ! Enter Again...\n")
            continue
        else:
            for r in read_dish:
                val = r.split(",")
                if val[0] == enter_code:
                    dish_n = val[1]
                    dish_p = val[2]
                    quantity = int(input("\tEnter Quantity of Item :- "))
                    print("\tSelected Item is :-", dish_n)
                    print("\tQuantity for ", dish_n, "is :- ", quantity)
                    new_dish_p = quantity * int(dish_p)
                    total_cost += new_dish_p
        another = input("\tDo You Want To Order Another Item (Y/N)? ")
        print("*********************************************************\n\n")
        if another.lower() == 'y':
            continue
        else:
            print("\t\t Ok then, Generating Your Bill")

            fobj2 = open("bills.txt", "r")
            bill_list = fobj2.readlines()
            fobj2.close()
            bill_id = len(bill_list)
            print("Please Wait ! Preparing your Bill.....")
            time.sleep(3)
            print("\tTotal Bill is :- ", total_cost)
           #==============================================
            date_s = '20/03/2023'
            date_f = '%d/%m/%y'
            date_obj = datetime.strptime(date_s,date_f).date()
            today_d = datetime.now().date()
            pass_d = (today_d-date_obj).days
            #=====================================
            datee = get_date()
            fobj1 = open("bills.txt", "a")
            fobj1.write(str(bill_id) + "," + str(total_cost) + ',' + str(datee) +','+str(pass_d)+"\n")
            fobj1.close()
            print("*----- New Bill is Generated SuccessFully..! -----*")
            break
    print("---------------------------------------------------------------------------------------------")
    time.sleep(2)
def menu():
    print("********************************************************")
    print("*\t                    MENU CARD                      *")
    print("********************************************************")

    fobj = open("dish.txt", "r")
    read_menu = fobj.readlines()
    fobj.close()
    data = []
    for r in read_menu:
        val = r.split(",")
        code = val[0]
        name = val[1]
        price = val[2]
        data.append([code, name, price])
    t = tabulate(data, headers=["CODE", "NAME", "PRICE"], tablefmt="fancy_grid")
    print(t)
    print("---------------------------------------------------------------------------------------------")
def update_price():
    while True:
        print("Update Price of Dish....")
        code = input("Enter Item Code For Update The Price: ")
        ret = valid_dish(code)
        if ret == False:
            print("Enter Valid Item Code .....")
            continue
        else:
            fobj = open("dish.txt", "r")
            read_menu = fobj.readlines()
            fobj.close()
            for item in read_menu:
                val = item.split(",")
                if val[0] == code:
                    name = val[1]
                    price = val[2]
                    print("The Current Price Of ", name, "is :- ", price, "\n")
                    new_p = input("\tEnter What you want you Set New Price: ")
                    fo = open("dish.txt", "w")
                    for line in read_menu:
                        if line == item:
                            fo.write(code + "," + name + "," + new_p + "\n")
                        else:
                            fo.write(line)
                    fo.close()
                    print("\tNew Price updated successfully... For ", name, "!!")
                    print(
                        "---------------------------------------------------------------------------------------------")

                    time.sleep(3)
                    break
            break
def todays_earn():
    print("********************************************************")
    print("*\t                 Today's Earning                   *")
    print("********************************************************")
    fobj = open("bills.txt", "r")
    read_all = fobj.readlines()
    fobj.close()
    today_earn = 0
    data = []
    today = date.today()
    for all in read_all:
        val = all.split(",")
        if len(val) < 2:  # Add error handling for list length
            continue
        b_id = val[0]
        b_cost = float(val[1])
        b_date = val[2].strip()
        bill_date = datetime.strptime(b_date, "%d/%m/%Y").date()
        if bill_date == today:
            data.append([b_id, b_cost, b_date])
            today_earn += b_cost
    t = tabulate(data, headers=["BILL_ID", "COST", "DATE"], tablefmt="fancy_grid")
    print(t)
    print("---------------------------------------------------------------------------------------------")
    print("Total Earning: ", today_earn)
    print("---------------------------------------------------------------------------------------------")
def past_days():
        print("********************************************************")
        print("*\t               PAST DAYS EARNINGS                  *")
        print("********************************************************")
        days = int(input("\tEnter How Many Days Bill you want: "))
        today = datetime.today().date()
        past_date = today - timedelta(days=days)
        data = []
        f = open("bills.txt", "r")
        for line in f:
            if line.strip():
                values = line.strip().split(",")
                if len(values) == 3:
                    bill_id, cost, date_str = values
                    bill_date = datetime.strptime(date_str, "%d/%m/%Y").date()
                    if past_date <= bill_date <= today:
                        data.append([bill_id, float(cost), date_str])
        f.close()
        if data:
            print(tabulate(data, headers=["BILL_ID", "COST", "DATE"], tablefmt="fancy_grid"))
            total_earn = sum(row[1] for row in data)
            print("Total Earnings Of last ", days, "is **", total_earn, " **")
        else:
            print("No bills found for the past", days, "days.")
        print("--------------------------------------------------------------------")
def past_dates():
    print("********************************************************")
    print("*\t               PAST DATES EARNINGS                  *")
    print("********************************************************")
    print("\tBill On the Basis of Dates.")
    start_date_str = input("\tEnter Start Date (DD/MM/YYYY): ")
    end_date_str = input("\tEnter End Date (DD/MM/YYYY): ")
    start_date = datetime.strptime(start_date_str, "%d/%m/%Y").date()
    end_date = datetime.strptime(end_date_str, "%d/%m/%Y").date()
    data = []
    fobj = open("bills.txt", "r")
    for line in fobj:
        values = line.strip().split(",")
        if len(values) == 3:
            bill_id, cost, date_str = values
            bill_date = datetime.strptime(date_str, "%d/%m/%Y").date()
            if start_date <= bill_date <= end_date:
                data.append([bill_id, float(cost), date_str])
    fobj.close()
    if data:
        print(tabulate(data, headers=["BILL_ID", "COST", "DATE"], tablefmt="fancy_grid"))
        total_earn = sum(row[1] for row in data)
        print("Total Earning: ", total_earn)
    else:
        print("No bills found between", start_date_str, "and", end_date_str)
    print("---------------------------------------------------------------------------------------------")
def add_dishes():
    print("********************************************************")
    print("*\t               ADD NEW DISH/ITEM                   *")
    print("********************************************************")
    print("\tAdding New dish.....!")
    d_code = input("\tEnter Dish code :- ")
    d_name = input("\tEnter Dish Name :- ")
    d_price = input("\tEnter price of Dish :- ")
    fobj = open("dish.txt", "a")
    fobj.write(d_code + "," + d_name + "," + d_price + "\n")
    fobj.close()
    print("\tNew Dish Added successFully...!!")
    print("---------------------------------------------------------------------------------------------")
def exit_p():
    print("Exiting program..")
    i = 5
    while i>=0:
        print("\rExiting in",i,"secs", end="")
        time.sleep(1)
        print("\b", end="")
        i = i - 1
    print("\n\n********************************************************")
    print("*\t                 Thank you !                       *")
    print("*\t              Exited SuccessFully                  *")
    print("********************************************************")
    print("")
    exit(0)
while True:
    print("1:- Generate bill")
    print("2:- View Menu")
    print("3:- update price")
    print("4:- View Today's Total Earning ")
    print("5:- View Bills")
    print("6:- Add Dishes in Menu ")
    print("0:- exit")
    sel = int(input("\t\tSelect Your choice :-  "))
    if sel == 1:
        generate_bill();
    elif sel == 2:
        menu();
    elif sel == 3:
        update_price();
    elif sel == 4:
        todays_earn();
    elif sel == 5:
        print("1:- Based On past days")
        print("2:- Based On past dates")
        print("Select one Of this :----")
        sel1 = int(input())
        if sel1 == 1:
            past_days();
        elif sel1 == 2:
            past_dates();
    elif sel == 6:
        add_dishes();
    elif sel ==0:exit_p()
