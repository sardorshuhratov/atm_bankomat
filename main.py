# -------------------------
# Bankomat - Automated Teller Machine(ATM)
# -------------------------

save_pasword = 1311
balance = 16303
password = int(input("Plastik karta parolingizni kiriting: "))
menu = ["Balansni tekshirish", "Naqd pul olish", "To'lovlar", "Parolni ozgartirish"]
menuTolovlar = ["Komunal", "Soliqlar", "Jarimalar"]
menuKomunal = ["Gaz", "Suv", "Svet", "Chiqindi"]
menuSoliqlar = ["Mol-mulk", "Jon solig'i"]
menuJarimalar = ["IIV jarimalari", "MIB jarimalari"]

if password == save_pasword:
    print("\nXush kelibsiz")
    print(f"\n1-{menu[0]}")
    print(f"2-{menu[1]}")
    print(f"3-{menu[2]}")
    print(f"4-{menu[3]}")

    tanlov = int(input("\nMenudan birini tanlang: "))

    if tanlov == 1:
        print(f"\nSizning xisobingizda: {balance} so'm")

    elif tanlov == 2:
        summa = float(input("\nSummani kiriting: "))
        if summa <= balance:
            balance = balance - summa
            print(f"\nSiz {summa} so'm yechib oldingiz")
            print(f"Sizning balansingizda {balance} so'm qoldi!")
        else:
            print("\nBalansingizda mablag' yetarli emas!")
            print(f"Balansingizda: {balance} so'm bor")

    elif tanlov == 3:
        for i in range(len(menuTolovlar)):
            print(f"\n{i + 1}-{menuTolovlar[i]}")

        tanlov_tolovlar = int(input("\nMenu dan birini tanlang: "))

        if tanlov_tolovlar == 1:
            for i in range(len(menuKomunal)):
                print(f"\n{i + 1}-{menuKomunal[i]}")

            tanlov_komunal = int(input("\nMenu dan birini tanlang: "))

            if tanlov_komunal == 1:
                xisob_raqam = int(input("\nGaz xisob raqamingizni kiriting: "))
                if xisob_raqam == 1610178:
                    tolov_sum = float(input("\nTo'lov summasini kiriting: "))
                    if balance >= tolov_sum:
                        balance = balance - tolov_sum
                        print(f"\nSiz Gazga: {tolov_sum} so'm to'lov qildingiz")
                        print(f"Sizning xisobingizda {balance} so'm qoldi")
                    else:
                        print(f"\nSizning xisobingizda {balance} so'm bor")
                        print("Sizning xisobingizda mablag' yetarli emas...")
                else:
                    print("Notog'ri xisob raqam kiritdingiz")

            elif tanlov_komunal == 2:
                xisob_raqam = int(input("\nSuv xisob raqamingizni kiriting: "))
                if xisob_raqam == 101010:
                    tolov_sum = float(input("\nTo'lov summasini kiriting: "))
                    if balance >= tolov_sum:
                        balance = balance - tolov_sum
                        print(f"\nSiz Suvga: {tolov_sum} so'm to'lov qildingiz")
                        print(f"Sizning xisobingizda {balance} so'm qoldi")
                    else:
                        print(f"\nSizning xisobingizda {balance} so'm bor")
                        print("Sizning xisobingizda mablag' yetarli emas...")
                else:
                    print("Notog'ri xisob raqam kiritdingiz")

            elif tanlov_komunal == 3:
                xisob_raqam = int(input("\nSvet xisob raqamingizni kiriting: "))
                if xisob_raqam == 100102:
                    tolov_sum = float(input("\nTo'lov summasini kiriting: "))
                    if balance >= tolov_sum:
                        balance = balance - tolov_sum
                        print(f"\nSiz Svetga: {tolov_sum} so'm to'lov qildingiz")
                        print(f"Sizning balansingizda {balance} so'm qoldi")
                    else:
                        print(f"\nSizning balansingizda {balance} so'm bor")
                        print("Sizning xisobingizda mablag' yetarli emas...")
                else:
                    print("Notog'ri xisob raqam kiritdingiz")

            elif tanlov_komunal == 4:
                xisob_raqam = int(input("\nChiqindi xisob raqamingizni kiriting: "))
                if xisob_raqam == 223311:
                    tolov_sum = float(input("\nTo'lov summasini kiriting: "))
                    if balance >= tolov_sum:
                        balance = balance - tolov_sum
                        print(f"\nSiz Chiqindini olib ketishga: {tolov_sum} so'm to'lov qildingiz")
                        print(f"Sizning balansingizda {balance} so'm qoldi")
                    else:
                        print(f"\nSizning balansingizda {balance} so'm bor")
                        print("Sizning xisobingizda mablag' yetarli emas...")
                else:
                    print("Notog'ri xisob raqam kiritdingiz")

        elif tanlov_tolovlar == 2:
            for i in range(len(menuSoliqlar)):
                print(f"\n{i + 1}-{menuSoliqlar[i]}")

            tanlov_soliqlar = int(input("\nMenu dan birini tanlang: "))

            if tanlov_soliqlar == 1:
                xisob_raqam = int(input("\nMol-mulk solig'i xisob raqamingizni kiriting: "))
                if xisob_raqam == 171717:
                    tolov_sum = float(input("\nTo'lov summasini kiriting: "))
                    if balance >= tolov_sum:
                        balance = balance - tolov_sum
                        print(f"\nMol-mulk solig'i uchun: {tolov_sum} so'm to'lov qildingiz")
                        print(f"Sizning balansingizda {balance} so'm qoldi")
                    else:
                        print(f"\nSizning balansingizda {balance} so'm bor")
                        print("Sizning xisobingizda mablag' yetarli emas...")
                else:
                    print("Notog'ri xisob raqam kiritdingiz")

            elif tanlov_soliqlar == 2:
                xisob_raqam = int(input("\nJon solig'i xisob raqamingizni kiriting: "))
                if xisob_raqam == 151515:
                    tolov_sum = float(input("\nTo'lov summasini kiriting: "))
                    if balance >= tolov_sum:
                        balance = balance - tolov_sum
                        print(f"\nJon solig'i uchun: {tolov_sum} so'm to'lov qildingiz")
                        print(f"Sizning balansingizda {balance} so'm qoldi")
                    else:
                        print(f"\nSizning balansingizda {balance} so'm bor")
                        print("Sizning xisobingizda mablag' yetarli emas...")
                else:
                    print("Notog'ri xisob raqam kiritdingiz")

            else:
                print("Notog'ri bolimni tanladingiz!!!")

        elif tanlov_tolovlar == 3:
            for i in range(len(menuJarimalar)):
                print(f"\n{i + 1}-{menuJarimalar[i]}")

            tanlov_jarimalar = int(input("\nMenu dan birini tanlang: "))

            if tanlov_jarimalar == 1:
                xisob_raqam = int(input("\nIIV jarimangiz raqamini kiriting: "))
                if xisob_raqam == 181818:
                    tolov_sum = float(input("\nTo'lov summasini kiriting: "))
                    if balance >= tolov_sum:
                        balance = balance - tolov_sum
                        print(f"\nIIV jarimangiz uchun: {tolov_sum} so'm to'lov qildingiz")
                        print(f"Sizning balansingizda {balance} so'm qoldi")
                    else:
                        print(f"\nSizning balansingizda {balance} so'm bor")
                        print("Sizning xisobingizda mablag' yetarli emas...")
                else:
                    print("Notog'ri jarima raqam kiritdingiz")

            elif tanlov_jarimalar == 2:
                xisob_raqam = int(input("\nMIB jarimangiz raqamini kiriting: "))
                if xisob_raqam == 191919:
                    tolov_sum = float(input("\nTo'lov summasini kiriting: "))
                    if balance >= tolov_sum:
                        balance = balance - tolov_sum
                        print(f"\nMIB jarimangiz uchun: {tolov_sum} so'm to'lov qildingiz")
                        print(f"Sizning balansingizda {balance} so'm qoldi")
                    else:
                        print(f"\nSizning balansingizda {balance} so'm bor")
                        print("Sizning xisobingizda mablag' yetarli emas...")
                else:
                    print("Notog'ri jarima raqam kiritdingiz")

    elif tanlov == 4:
        new_pasword = int(input("\nYangi parolingizni kiriting: "))
        save_pasword = new_pasword
        print("\nParolingiz muvaffaqiyatli o'zgartirildi")

    else:
        print("Notog'ri tanlov!")

    print("\nBankimiz xizmatlaridan foydalanganiz uchun raxmat")

else:
    print("ERROR PASSWORD!!!")