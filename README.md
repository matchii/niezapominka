niezapominka
============

Instalacja
----------

1. Zainstaluj bibliotekę Fabric:
    sudo easy_install fabric

2. Pobierz aplikację:
    git clone https://github.com/matchii/niezapominka.git

3. Wejdź do katalogu niezapominka/ i wywołaj:
    fab build_db

4. Wykonaj podane zapytania w bazie mysql.

5. Wywołaj:
    fab from_scratch

6. Pod adresem 127.0.0.1:8000 powinna być działająca aplikacja.


Polecenia from_scratch i build_db przyjmują parametry w formie np.:
    fab build_db:db_name=<nazwa bazy>,db_user=<użytkownik>

Szczegóły: patrz plik fabfile.py
