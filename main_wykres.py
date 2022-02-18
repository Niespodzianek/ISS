import requests
import json
import time
import datetime
import os
import turtle

def odczytanie_skladu_zalogi(adres_strony):
    strona_www_zalogi = json.loads(requests.get(adres_strony).text)
    zaloga = strona_www_zalogi["people"]
    print(f"Obecny skład załogi Międzynarodowej Stacji Kosmicznej to {len(zaloga)} osób")
    for zalogant in zaloga:
        modul = zalogant["craft"]
        nazwisko = zalogant["name"]
        print(f"{nazwisko} zamieszkuje moduł {modul}")

def odczytanie_pozycji_iss(adres_strony):
    pomiar = json.loads(requests.get(adres_strony).text)
    pozycja_iss = pomiar["iss_position"]
    dlugosc_geo = pozycja_iss["longitude"]
    szerokosc_geo = pozycja_iss["latitude"]
    chwila = datetime.datetime.fromtimestamp(pomiar["timestamp"])
    print(f"W dniu {chwila.day} {chwila.month} {chwila.year} o godzinie {chwila.hour} minut {chwila.minute} sekund"
          f" {chwila.second}, Międzynarodowa Stacja Kosmiczna znajdowała się na pozycji o długości geograficznej"
          f" {dlugosc_geo} i szerokości geograficznej {szerokosc_geo}")
    return dlugosc_geo, szerokosc_geo

def program():
    ekran = turtle.Screen()
    iss = turtle.Turtle()
    ekran.title("Pozycja Międzynarodowej Stacji Kosmicznej")
    ekran.setup(1280, 640)
    ekran.setworldcoordinates(-180, -90, 180, 90)
    ekran.bgpic("tlo.gif")
    ekran.register_shape("iss.gif")
    iss.shape(name="iss.gif")
    iss.penup()
    petla_pracuje = True
    api_iss_zaloga = "http://api.open-notify.org/astros.json"
    odczytanie_skladu_zalogi(adres_strony=api_iss_zaloga)
    while petla_pracuje:
        api_iss_pozycja = "http://api.open-notify.org/iss-now.json"
        pozycja_na_mapie = odczytanie_pozycji_iss(adres_strony=api_iss_pozycja)

        iss_dlug_geo = float(pozycja_na_mapie[0])
        iss_szer_geo = float(pozycja_na_mapie[1])

        if iss_dlug_geo > 180:
            iss.penup()
            iss.goto(iss_dlug_geo, iss_szer_geo)
        else:
            iss.goto(iss_dlug_geo, iss_szer_geo)

        iss.pendown()
        time.sleep(2)
        os.system('clear')
    print("KONIEC PRACY")

if __name__ == '__main__':
    program()
