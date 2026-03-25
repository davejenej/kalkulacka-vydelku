# 💰 Kalkulačka výdělku

Jednoduchá desktopová aplikace v Pythonu pro evidenci odpracovaných směn a výpočet výdělku.  
Primárně určená pro vlastní orientační přehled (např. DPP), bez řešení odvodů.

---

## ✨ Funkce

- Zadání směny pomocí času **od–do**
- Výpočet:
  - odpracovaných hodin
  - výdělku podle hodinové sazby
- Ukládání směn do `CSV` souboru
- Výpočet **celkového výdělku** ze všech směn
- Jednoduché GUI pomocí `tkinter`

---

## 🖥️ Náhled použití

1. Zadáš:
   - čas příchodu (např. `08:00`)
   - čas odchodu (např. `16:30`)
   - hodinovou sazbu (např. `150`)
2. Klikneš na **"Uložit směnu"**
3. Aplikace:
   - spočítá hodiny
   - uloží směnu
   - zobrazí výdělek

---

## 📂 Struktura projektu


.


├── kalkulackav2.py # GUI aplikace


├── kalkulacka.py # jednoduchá CLI verze


└── smeny.csv # uložené směny (vytvoří se automaticky)

---

## ▶️ Spuštění

### Požadavky
- Python 3.x

### Spuštění GUI verze

```bash
python kalkulackav2.py
```

### Spuštění CLI verze

```bash
python kalkulacka.py
```

## 🧠 Jak to funguje
Časy se parsují pomocí datetime
Rozdíl času → převeden na hodiny
Výdělek:
```bash
výdělek = hodiny × hodinová_sazba
```
Data se ukládají do CSV souboru (smeny.csv)

## ⚠️ Omezení
Neřeší:
 - daně
 - odvody
 - noční směny přes půlnoc (zatím)
- Formát času musí být přesně HH:MM

## 🚀 Možná vylepšení
- filtrování podle měsíce
- přehled směn přímo v GUI
- editace / mazání směn
- export do Excelu
- build do .exe

## 📄 Licence
Volně použitelné pro osobní účely.
