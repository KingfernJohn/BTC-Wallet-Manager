import qrcode, os

def gen_qr_code():
    os.system('cls')
    c_line = 0
    wallet_data = open("Wallet Save.txt","r")
    for line in wallet_data:
        c_line += 1
        if c_line == 1:
            btc_adr = line

    btc_adr = str(btc_adr)
    img = qrcode.make(btc_adr)
    img.save("Wallet QR-Code.png")
    print(btc_adr)
    line = 0

gen_qr_code()
print("\nThe QR-Code has been saved as a .png\n\n")
input("-Press any key to continue-")
import my_menu