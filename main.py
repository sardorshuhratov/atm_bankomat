# -------------------------

# Bankomat - Automated Teller Machine(ATM)

save_pasword = 1111
balance = 10000
password = int(input("Parolizni kiriting: "))
menu = ["Balansni tekshirish", "Naqd pul olish", "SMS habar ulash", "Parolni ozgartirish"]

if password == save_pasword:
    print("Xush kelibsiz")
    print(f"1-{menu[0]}")
    print(f"2-{menu[1]}")
    print(f"3-{menu[2]}")
    print(f"4-{menu[3]}")

    tanlov = int(input("Menudan birini tanlang: "))
    if tanlov == 1:
        print("Sizning xisonbingizda:", (balance))
    elif tanlov == 2:
        sum = float(input("Summani kiriting: "))
        if sum < balance:
            balance -= sum
            print(f"Siz {sum} so'm yechib oldingiz")
            print(f"Sizning balansingizda {balance} so'm qoldi!")
        else:
            print("Balansingizda mablag' yetarli emas!")
            print(f"Balansingizda: {balance} so'm bor")
else:
    print("ERROR PASSWORD!!!")