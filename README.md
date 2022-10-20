# DSW_Harmonogramy_Crawler

## Opis

Generator eventów Google Calendar z wykorzystaniem danych z harmonogramów DSW

## Instalacja

```bash
pip install -r requirements.txt
```

Następnie należy utworzyć foldery `calendar` i `extracted` w katalogu data.
W pliku `main.py` należy ustawić zakres ID grup, które mają zostać przetworzone.

## Użycie

```bash
python -m main.py
```

Pliki wygenerowane zostaną umieszczone w folderze `calendar`.
Można je zaimportować do Google Calendar.

## TODOLIST

- [ ] User friendly interface
- [ ] Konfiguracja z pliku
- [ ] Więcej opcji eksportu
- [ ] Optymalizacja (ładowanie cachowanych danych)
- [ ] ...
