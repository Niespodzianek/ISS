import requests
# import json

def odczytanie_infornacji(adres_strony):
    strona = requests.get(adres_strony)
    zawartosc = strona.text
    print(zawartosc)
    # misje = json.loads(zawartosc)
    # print(misje)

    # for index in range(len(misje)):
    #    print(f"Pozycja {index + 1}. Nazwa misji: {misje[index]['mission_name']},"
    #          f" Symbol: {misje[index]['mission_id']},"
    #          f" Inwestor: {misje[index]['manufacturers']},"
    #          f" Ładunek: {misje[index]['payload_ids']}")

        # print(f"Opis: {misje[index]['description']}")
        # for klucz, wartosc in misje[index].items():
        #     print(f"Klucz - {klucz}, wartość - {wartosc}")
        # input("\nNaciśnij ENTER aby kontynuować")

def program():
    api = "https://api.spacexdata.com/v3/missions"
    odczytanie_infornacji(adres_strony=api)
    print("KONIEC PRACY")

if __name__ == '__main__':
    program()
