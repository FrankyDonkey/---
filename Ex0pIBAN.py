import colorama
import requests
from colorama import Fore, Style

print("IBAN Expl0it Checker\nExpl0it By: FrankyDonkey\nCoded By: Mostafa M. Mead\nEdited By: Priv8GHOST\nPRIV8GHOST TEAM")

IBANs = []

def load():
    txt_path = input("IBANS file.txt: ")
    with open(txt_path) as f:
        lines = f.read().split('\n')
    for IBAN in lines:
        if IBAN is not None and not '':
            IBANs.append(IBAN)

def check_iban(IBAN):
    url = "https://www.ibancalculator.com/iban_validieren.html"
    headers = {
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Content-Type':'application/x-www-form-urlencoded',
        'Host':'www.ibancalculator.com',
        'Origin':'https://www.ibancalculator.com',
        'Referer':'https://www.ibancalculator.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    }
    data = f"tx_valIBAN_pi1%5Biban%5D={IBAN}&tx_valIBAN_pi1%5Bfi%5D=fi&no_cache=1&Action=validate+IBAN"
    req = requests.post(url, data=data, headers=headers)
    source = req.text
    if 'The checksum in the account number is incorrect' in source:
        return False
    elif 'The account number contains a valid checksum' in source:
        return True

def main():
    load()
    for IBAN in IBANs:
        try:
            if check_iban(IBAN):
                valid_text = open("valid_ibans.txt" , 'a+' , encoding='UTF-8')
                valid_text.write(f"{IBAN}\n")
                valid_text.close()
                print(Fore.GREEN +f"GOOD => {IBAN}")
            else:
                print(Fore.RED +f"BAD => {IBAN}")
        except:
            pass

if __name__ == "__main__":
    main()
    quit()
