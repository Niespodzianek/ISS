import requests
import json

def odczytanie_infornacji_o_misjach(adres_strony):
    misje = json.loads(requests.get(adres_strony).text)
    return misje

def prezentacja_misji(misje):
    for index in range(len(misje)):
        print(f"Pozycja {index + 1}. Nazwa misji: {misje[index]['mission_name']},"
              f" Symbol: {misje[index]['mission_id']},"
              f" Inwestor: {misje[index]['manufacturers']},"
              f" Ładunek: {misje[index]['payload_ids']}")

def program():
    api = "https://api.spacexdata.com/v3/missions"
    zaplanowane_misje = odczytanie_infornacji_o_misjach(adres_strony=api)
    prezentacja_misji(zaplanowane_misje)
    print("KONIEC PRACY")

if __name__ == '__main__':
    program()
