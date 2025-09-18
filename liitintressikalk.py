import tkinter as tk
import math

# Funktsioon, mis arvutab liitintressi
def liitintress_kalkulaator():
    try:
        # Kogume kõik sisendid
        algkapital = float(entry_algkapital.get())
        igakuine = float(entry_igakuine.get())
        tootlus = float(entry_tootlus.get())
        periood = int(entry_periood.get())

        # Liitintressi valem
        n = periood  # periood aastates
        r = tootlus / 100  # aastane tootlus

        # Arvutame lõpliku summa (algkapital + igakuine investeering)
        tulemus = algkapital * math.pow(1 + r, n) + igakuine * ((math.pow(1 + r, n) - 1) / r)

        # Kuvame tulemuse
        label_tulemus.config(text=f"Lõplik summa: {tulemus:.2f} €")

    except ValueError:
        label_tulemus.config(text="Palun sisesta kehtivad numbrid.")

# Peamine aken
root = tk.Tk()
root.title("Liitintressi Kalkulaator")

# Akna suurus
root.geometry("400x400")

# Tiitel
label_title = tk.Label(root, text="Liitintressi Kalkulaator", font=("Arial", 14))
label_title.grid(row=0, columnspan=2, padx=10, pady=20)

# Esimene investeering (algkapital)
label_algkapital = tk.Label(root, text="Esimene investeering (€):")
label_algkapital.grid(row=1, column=0, padx=10, pady=10)

entry_algkapital = tk.Entry(root)
entry_algkapital.grid(row=1, column=1, padx=10, pady=10)

# Igakuine investeering
label_igakuine = tk.Label(root, text="Igakuine investeering (€):")
label_igakuine.grid(row=2, column=0, padx=10, pady=10)

entry_igakuine = tk.Entry(root)
entry_igakuine.grid(row=2, column=1, padx=10, pady=10)

# Aastane tootlus
label_tootlus = tk.Label(root, text="Aastane tootlus (%):")
label_tootlus.grid(row=3, column=0, padx=10, pady=10)

entry_tootlus = tk.Entry(root)
entry_tootlus.grid(row=3, column=1, padx=10, pady=10)

# Investeerimisperiood
label_periood = tk.Label(root, text="Investeerimisperiood (aastates):")
label_periood.grid(row=4, column=0, padx=10, pady=10)

entry_periood = tk.Entry(root)
entry_periood.grid(row=4, column=1, padx=10, pady=10)

# Nupp arvutamiseks
button_arvuta = tk.Button(root, text="Arvuta", command=liitintress_kalkulaator)
button_arvuta.grid(row=5, columnspan=2, pady=20)

# Tulemuse kuvamine
label_tulemus = tk.Label(root, text="Lõplik summa: ")
label_tulemus.grid(row=6, columnspan=2, pady=10)

# Aken jääb avatuks
root.mainloop()

