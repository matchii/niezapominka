niezapominka
============

Instalacja
----------

### Wymagania

  - biblioteka Fabric

    sudo apt-get install fabric

  - python-mysqldb

    sudo apt-get install python-mysqldb

### Kroki

1. Pobierz aplikację:

    git clone https://github.com/matchii/niezapominka.git

2. Wejdź do katalogu niezapominka/ i wywołaj:

    fab build_db

3. Wykonaj podane zapytania w bazie mysql.

4. Wywołaj:

    fab from_scratch

5. Pod adresem 127.0.0.1:8000 powinna być działająca aplikacja.

### Uwagi

Polecenia from_scratch i build_db przyjmują parametry w formie np.:
    fab build_db:db_name=<nazwa bazy>,db_user=<użytkownik>

Szczegóły: patrz plik fabfile.py
