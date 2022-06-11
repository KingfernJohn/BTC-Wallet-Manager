from bitcoin import *
import os

def loop_creation():
    os.system('cls')
    print("_______________________________________________")
    print("\nDo you want to create a new BTC wallet -  y | n\n")
    sure_ = input(">>> ")
    if sure_ == "y":
        print("\n----------------\n")
        print("Loading...\n")
        wallet_save = open("Wallet Save.txt","w+")
        wallet_conf = open("Wallet Config.txt","w+")
        private_key = random_key()
        public_key = privtopub(private_key)
        adress = pubtoaddr(public_key)
        wallet_save.write("BTC Adress: " +adress+ "\n")
        wallet_save.write("Pub Key: " +privtopub(private_key)+ "\n")
        wallet_save.write("Prv Key: " +private_key)
        wallet_save.close
        wallet_conf.write(adress+"\n")
        wallet_conf.write(privtopub(private_key)+ "\n")
        wallet_conf.write(private_key)    
        wallet_conf.close
        print("BTC Wallet created!\n\nMore info in the Wallet Save.txt file\n\nYour BTC Adress is -> "+adress+"\n")
        print("----------------\n")
        input("-Press any key to continue-")
        import my_menu
    else:
        import my_menu
loop_creation()