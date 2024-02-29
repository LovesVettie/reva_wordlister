import random
import time
import colorama
from colorama import Fore, Back, Style
import os

def generate_wordlist(first_name, last_name, brand_name, ssid_name, birth_year):
    wordlist = []


    name_list = [first_name, last_name, first_name.lower(), last_name.lower(), first_name.capitalize(), last_name.capitalize()]
    brand_list = [brand_name, brand_name.lower(), brand_name.capitalize()]
    ssid_list = [ssid_name, ssid_name.lower(), ssid_name.capitalize()]
    birth_year_list = [birth_year]

  
    for name in name_list:
        for year in birth_year_list:
            wordlist.append(name + year)


    for first in name_list:
        for last in name_list:
            if first != last:
                wordlist.append(first + last)


    for name in name_list:
        for brand in brand_list:
            wordlist.append(name + brand)

    for last in name_list:
        for year in birth_year_list:
            wordlist.append(last + year)


    for ssid in ssid_list:
        for year in birth_year_list:
            wordlist.append(ssid + year)


    while len(wordlist) < 3000:
        word = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz1234567890', k=8))
        wordlist.append(word)

    return wordlist[:3000]  

def write_wordlist_to_file(wordlist):
    with open("wordlistsonuc.txt", "w") as file:
        for word in wordlist:
            file.write(word + "\n")
banner = """

 ██▀███  ▓█████ ██▒   █▓ ▄▄▄           ▄████ ▓█████  ███▄    █ 
▓██ ▒ ██▒▓█   ▀▓██░   █▒▒████▄        ██▒ ▀█▒▓█   ▀  ██ ▀█   █ 
▓██ ░▄█ ▒▒███   ▓██  █▒░▒██  ▀█▄     ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒
▒██▀▀█▄  ▒▓█  ▄  ▒██ █░░░██▄▄▄▄██    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒
░██▓ ▒██▒░▒████▒  ▒▀█░   ▓█   ▓██▒   ░▒▓███▀▒░▒████▒▒██░   ▓██░
░ ▒▓ ░▒▓░░░ ▒░ ░  ░ ▐░   ▒▒   ▓▒█░    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ 
  ░▒ ░ ▒░ ░ ░  ░  ░ ░░    ▒   ▒▒ ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░
  ░░   ░    ░       ░░    ░   ▒      ░ ░   ░    ░      ░   ░ ░ 
   ░        ░  ░     ░        ░  ░         ░    ░  ░         ░ 
                    ░                                          


"""
print(Fore.RED)
print(banner)
print(Fore.GREEN)
print("Kod Hazırlanıyor:                                10/100          ##..............................")
print("            ")
time.sleep(0.5)
print("Kod Hazırlanıyor:                                20/100          #####...........................")
print("            ")
time.sleep(0.5)
print("Kod Hazırlanıyor:                                30/100          #########.......................")
print("            ")
time.sleep(0.5)
print("Kod Hazırlanıyor:                                45/100          ##############..................")
print("            ")
time.sleep(0.5)
print("Kod Hazırlanıyor:                                60/100          #####################...........")
print("            ")
time.sleep(0.5)
print("Kod Hazırlanıyor:                                70/100          ############################....")
print("            ")
time.sleep(0.5)
print("Kod Hazırlanıyor:                                85/100          ##############################..")
print("            ")
time.sleep(0.5)
print("Kod Hazırlanıyor:                                100/100          ###############################")
print("            ")
time.sleep(0.5)

os.system("clear")

print(Fore.YELLOW)

girisyazi = '''

88""Yb 888888 Yb    dP    db         dP""b8 888888 88b 88 
88__dP 88__    Yb  dP    dPYb       dP   `" 88__   88Yb88 
88"Yb  88""     YbdP    dP__Yb      Yb  "88 88""   88 Y88 
88  Yb 888888    YP    dP""""Yb      YboodP 888888 88  Y8                                                                                             

'''

print(girisyazi)

time.sleep(2)

print(Fore.MAGENTA)
first_name = input("root$ADI: ")
last_name = input("root$SOYADI: ")
brand_name = input("root$MARKA_ADI: ")
ssid_name = input("root$EŞ_ADI: ")
birth_year = input("root$TAKIM_KURULUS_TARIHI ")

wordlist = generate_wordlist(first_name, last_name, brand_name, ssid_name, birth_year)
write_wordlist_to_file(wordlist)

print("Wordlist oluşturuldu.")
time.sleep(6)
print("Kod tamamlandı.")
time.sleep(3)
