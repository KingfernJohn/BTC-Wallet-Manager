import os.path
import os

def loop_menu():
    os.system('cls')
    wallet_conf_exists = os.path.exists('Wallet Config.txt')
    print("\n1 - Create new wallet\n2 - Show wallet details\n3 - Generate Wallet QR-Code\n")
    user_choise = input (">>> ")
    if user_choise == "1":
        if wallet_conf_exists == False:
            import create_new_btc_wallet
        else:
            print("\nWallet Config.txt  &  Wallet Save.txt  -  exist!\n")
            input("-Press any key to continue-")
            loop_menu()
    
    if user_choise == "2":
        print("\n------------\n")
        wallet_data = open("Wallet Save.txt","r")
        for line in wallet_data:
            print(line)
        print("\n-----------\n")
        input("-Press any key to continue-")
        loop_menu()

    if user_choise == "3":
        if wallet_conf_exists == True:
            import gen_qr_code
        else:
            loop_menu()


loop_menu()