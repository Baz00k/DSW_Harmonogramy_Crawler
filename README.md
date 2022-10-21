# DSW_Harmonogramy_Crawler

## Opis

Generator eventów Google Calendar z wykorzystaniem danych z harmonogramów DSW

## Instalacja

Wymagany Python 3.10+ i zainstalowany Chrome.

```bash
pip install -r requirements.txt
```

W pliku `config.json` należy ustawić zakres ID grup, które mają zostać przetworzone.

## Użycie

```bash
python -m dswhc
```

Pliki wygenerowane zostaną umieszczone w folderze `calendar`.
Można je zaimportować do Google Calendar.

## To-do

- [ ] User friendly interface
- [x] Konfiguracja z pliku ([@trag1c](https://github.com/trag1c))
- [ ] Więcej opcji eksportu
- [ ] Optymalizacja (ładowanie cachowanych danych)
- [ ] ...
