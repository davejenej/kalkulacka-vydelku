from datetime import datetime

print("Kalkulačka výdělku\n")

volba = input("Vyber možnost:\n1 - zadám počet hodin\n2 - zadám čas od-do\nVolba: ")

sazba = float(input("Zadej hodinovou sazbu (Kč): "))

if volba == "1":
    hodiny = float(input("Zadej počet odpracovaných hodin: "))

elif volba == "2":
    od = input("Čas příchodu (HH:MM): ")
    do = input("Čas odchodu (HH:MM): ")

    t1 = datetime.strptime(od, "%H:%M")
    t2 = datetime.strptime(do, "%H:%M")

    rozdil = t2 - t1
    hodiny = rozdil.total_seconds() / 3600

else:
    print("Neplatná volba.")
    exit()

vydelano = hodiny * sazba

print("\n--- Výsledek ---")
print(f"Odpracované hodiny: {hodiny:.2f}")
print(f"Hodinová sazba: {sazba} Kč")
print(f"Výdělek: {vydelano:.2f} Kč")