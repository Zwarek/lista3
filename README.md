# lista3

# zadanie 1

	# Automatyzacja Testów API z Wykorzystaniem Curl

	## Opis

	Ten skrypt automatycznie testuje różne endpointy API przy użyciu narzędzia curl. Skrypt wysyła żądania HTTP do wybranego publicznego API (JSONPlaceholder) i sprawdza, czy odpowiedzi są poprawne (statusy HTTP i kluczowe elementy w odpowiedziach JSON).

	## Jak Uruchomić

	1. Upewnij się, że masz zainstalowanego Pythona i narzędzie curl.
	2. Zapisz skrypt w pliku `api_skrypt.py`.
	3. Uruchom skrypt w terminalu:
		python api_skrypt.py

	## Wyniki

	Skrypt wyświetli wyniki testów w czytelny sposób, np. "Test /posts/1: ZDANY", "Test /comments/1: NIE ZDANY".

	## Przykładowe Testy

	Skrypt testuje następujące endpointy:

	1. `/posts/1` - sprawdza obecność kluczy: `userId`, `id`, `title`, `body`
	2. `/comments/1` - sprawdza obecność kluczy: `postId`, `id`, `name`, `email`, `body`
	3. `/users/1` - sprawdza obecność kluczy: `id`, `name`, `username`, `email`


# zadanie 2

	# Automatyzacja procesów z wykorzystaniem Makefile

	## Opis

	Ten projekt zawiera prostą aplikację napisaną w Pythonie, która dodaje dwie liczby, oraz testy jednostkowe dla tej aplikacji. Automatyzacja procesów testowania i uruchamiania aplikacji jest realizowana za pomocą Makefile.

	## Pliki

	- `app.py`: Prosta aplikacja dodająca dwie liczby.
	- `test_app.py`: Testy jednostkowe dla aplikacji.
	- `Makefile`: Plik Makefile automatyzujący instalację zależności, uruchamianie testów i aplikacji.
	- `requirements.txt`: Plik z zależnościami (pusty w tym przypadku).

	## Jak używać

	### Instalacja zależności

	```sh
	make install
	make test
	make run
