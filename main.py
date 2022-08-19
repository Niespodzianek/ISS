import requests
import json
import time
import datetime
import os
import turtle


def odczytanie_skladu_zalogi(adres_strony):
    strona_www_zalogi = json.loads(requests.get(adres_strony).text)
    zaloga = strona_www_zalogi["people"]
    print(
        f"Obecny skład załogi Międzynarodowej Stacji Kosmicznej to {len(zaloga)} osób"
    )
    for zalogant in zaloga:
        modul = zalogant["craft"]
        nazwisko = zalogant["name"]
        print(f"{nazwisko} zamieszkuje moduł {modul}")


def odczytanie_pozycji_iss(adres_strony):
    pomiar = json.loads(requests.get(adres_strony).text)
    pozycja_iss = pomiar["iss_position"]
    dlugosc_geo = pozycja_iss["longitude"]
    szerokosc_geo = pozycja_iss["latitude"]
    czas_pomiaru = datetime.datetime.fromtimestamp(pomiar["timestamp"])
    print(
        f"W dniu {czas_pomiaru.day} {czas_pomiaru.month} {czas_pomiaru.year} o godzinie {czas_pomiaru.hour}"
        f" minut {czas_pomiaru.minute} sekund {czas_pomiaru.second}, Międzynarodowa Stacja Kosmiczna znajdowała"
        f" się na pozycji o długości geograficznej {dlugosc_geo} i szerokości geograficznej {szerokosc_geo}"
    )
    return dlugosc_geo, szerokosc_geo


def program():
    wykres = False

    decyzja = input(
        "Jeżeli chcesz aby ISS rysowała za sobą wykres, naciśnij klawisz 'W' i ENTER, jeżeli nie chcesz aby"
        " ISS rysowała wykres na ciśnij ENTER"
    )
    if decyzja == "w" or decyzja == "W":
        wykres = True

    ekran = turtle.Screen()
    iss = turtle.Turtle()
    ekran.title(
        "Pozycja Międzynarodowej Stacji Kosmicznej - z wykresem przelotu"
    )
    ekran.setup(640, 480)
    ekran.setworldcoordinates(-180, -90, 180, 90)
    ekran.bgpic(os.path.join("Gify", "tlo_5.gif"))
    ekran.register_shape(os.path.join("Gify", "satelita_2.gif"))
    iss.shape(name=os.path.join("Gify", "satelita_2.gif"))
    iss.penup()
    petla_pracuje = True
    api_iss_zaloga = "http://api.open-notify.org/astros.json"
    odczytanie_skladu_zalogi(adres_strony=api_iss_zaloga)
    while petla_pracuje:
        api_iss_pozycja = "http://api.open-notify.org/iss-now.json"
        pozycja_na_mapie = odczytanie_pozycji_iss(adres_strony=api_iss_pozycja)
        if wykres:
            if float(pozycja_na_mapie[0]) > 178:
                iss.penup()
                iss.goto(float(pozycja_na_mapie[0]), float(pozycja_na_mapie[1]))
            else:
                iss.goto(float(pozycja_na_mapie[0]), float(pozycja_na_mapie[1]))
                iss.pendown()
        else:
            iss.penup()
            iss.goto(float(pozycja_na_mapie[0]), float(pozycja_na_mapie[1]))
        time.sleep(2)
        os.system("clear")
    print("KONIEC PRACY")


if __name__ == "__main__":
    program()
