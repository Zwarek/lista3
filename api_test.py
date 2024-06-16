import subprocess
import json


def wyslij_zadanie_curl(url):
    try:
        odpowiedz = subprocess.check_output(["curl", "-s", "-w", "%{http_code}", url])
        tresc = odpowiedz[:-3]
        kod_statusu = int(odpowiedz[-3:])
        return kod_statusu, tresc.decode('utf-8')
    except subprocess.CalledProcessError as e:
        return e.returncode, ''


def sprawdz_odpowiedz(endpoint, kod_statusu, tresc, klucze):
    if kod_statusu != 200:
        return f"Test {endpoint}: NIE ZDANY (Kod Statusu {kod_statusu})"

    try:
        json_tresc = json.loads(tresc)
    except json.JSONDecodeError:
        return f"Test {endpoint}: NIE ZDANY (Niepoprawny JSON)"

    for klucz in klucze:
        if klucz not in json_tresc:
            return f"Test {endpoint}: NIE ZDANY (Brak klucza '{klucz}')"

    return f"Test {endpoint}: ZDANY"


def main():
    api_url = "https://jsonplaceholder.typicode.com"
    testy = [
        ("/posts/1", ["userId", "id", "title", "body"]),
        ("/comments/1", ["postId", "id", "name", "email", "body"]),
        ("/users/1", ["id", "name", "username", "email"]),
    ]

    for endpoint, klucze in testy:
        url = f"{api_url}{endpoint}"
        kod_statusu, tresc = wyslij_zadanie_curl(url)
        wynik = sprawdz_odpowiedz(endpoint, kod_statusu, tresc, klucze)
        print(wynik)


if __name__ == "__main__":
    main()
