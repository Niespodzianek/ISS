import requests
import json
import time
import os

def odczytanie_skladu_zalogi(adres_strony):
    strona_www_zalogi = json.loads(requests.get(adres_strony).text)
    zaloga = strona_www_zalogi["people"]
    print(f"Obecny skład załogi Międzynarodowej Stacji Kosmicznej to {len(zaloga)} osób\n")
    for zalogant in zaloga:
        modul = zalogant["craft"]
        nazwisko = zalogant["name"]
        print(f"{nazwisko} zamieszkuje moduł {modul}")

def program():
    licznik = 0
    petla_pracuje = True
    while petla_pracuje:
        licznik += 1
        os.system('clear')
        api_iss_zaloga = "http://api.open-notify.org/astros.json"
        odczytanie_skladu_zalogi(adres_strony=api_iss_zaloga)
        print(f"\nOdczyt nr: {licznik}")
        time.sleep(300)
        os.system('clear')
    print("KONIEC PRACY")

if __name__ == '__main__':
    program()
