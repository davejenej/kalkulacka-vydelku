import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import csv
import os

SOUBOR = "smeny.csv"

def ulozit_smenu():
    od = entry_od.get()
    do = entry_do.get()
    sazba = entry_sazba.get()

    try:
        t1 = datetime.strptime(od, "%H:%M")
        t2 = datetime.strptime(do, "%H:%M")
        hodiny = (t2 - t1).total_seconds() / 3600
        sazba = float(sazba)
        vydelano = hodiny * sazba
    except ValueError:
        messagebox.showerror("Chyba", "Zkontroluj formát času (HH:MM) a sazbu.")
        return

    # uložit do CSV
    zapis = [od, do, f"{sazba:.2f}", f"{hodiny:.2f}", f"{vydelano:.2f}"]
    file_exists = os.path.isfile(SOUBOR)
    with open(SOUBOR, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Od", "Do", "Sazba", "Hodiny", "Výdělek"])
        writer.writerow(zapis)

    messagebox.showinfo("Hotovo", f"Směna uložena. Výdělek: {vydelano:.2f} Kč")
    entry_od.delete(0, tk.END)
    entry_do.delete(0, tk.END)
    entry_sazba.delete(0, tk.END)

def celkovy_vydelek():
    if not os.path.isfile(SOUBOR):
        messagebox.showinfo("Info", "Žádné uložené směny.")
        return

    celkem = 0
    with open(SOUBOR, mode='r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            celkem += float(row["Výdělek"])
    messagebox.showinfo("Celkový výdělek", f"Zatím vyděláno: {celkem:.2f} Kč")

# GUI
root = tk.Tk()
root.title("Kalkulačka výdělku")

tk.Label(root, text="Čas od (HH:MM):").grid(row=0, column=0)
entry_od = tk.Entry(root)
entry_od.grid(row=0, column=1)

tk.Label(root, text="Čas do (HH:MM):").grid(row=1, column=0)
entry_do = tk.Entry(root)
entry_do.grid(row=1, column=1)

tk.Label(root, text="Hodinová sazba (Kč):").grid(row=2, column=0)
entry_sazba = tk.Entry(root)
entry_sazba.grid(row=2, column=1)

tk.Button(root, text="Uložit směnu", command=ulozit_smenu).grid(row=3, column=0, columnspan=2, pady=5)
tk.Button(root, text="Kolik mám zatím vyděláno", command=celkovy_vydelek).grid(row=4, column=0, columnspan=2, pady=5)

root.mainloop()