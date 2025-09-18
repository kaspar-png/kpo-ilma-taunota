import tkinter as tk
import math

# Funktsioon, mis avab laenukalkulaatori akna
def avada_laenukalkulaator():
    # Peidame peamise akna
    root.withdraw()

    kalkulaator_aken = tk.Toplevel(root)
    kalkulaator_aken.title("Laenukalkulaator")
    
    # Aken suurem
    kalkulaator_aken.geometry("500x400")

    # Tagasi nupp paigutatud vasakusse ülanurka
    button_tagasi = tk.Button(kalkulaator_aken, text="Tagasi", command=lambda: tagasi(kalkulaator_aken))
    button_tagasi.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    # Laenukalkulaatori sisend ja valem
    label_laenusumma = tk.Label(kalkulaator_aken, text="Laenusumma (€):")
    label_laenusumma.grid(row=1, column=0, padx=10, pady=10)

    entry_laenusumma = tk.Entry(kalkulaator_aken)
    entry_laenusumma.grid(row=1, column=1, padx=10, pady=10)

    label_sissemakse = tk.Label(kalkulaator_aken, text="Sissemakse (€):")
    label_sissemakse.grid(row=2, column=0, padx=10, pady=10)

    entry_sissemakse = tk.Entry(kalkulaator_aken)
    entry_sissemakse.grid(row=2, column=1, padx=10, pady=10)

    label_intress = tk.Label(kalkulaator_aken, text="Intressimäär (%):")
    label_intress.grid(row=3, column=0, padx=10, pady=10)

    entry_intress = tk.Entry(kalkulaator_aken)
    entry_intress.grid(row=3, column=1, padx=10, pady=10)

    label_periood = tk.Label(kalkulaator_aken, text="Periood (aastates või kuudes):")
    label_periood.grid(row=4, column=0, padx=10, pady=10)

    entry_periood = tk.Entry(kalkulaator_aken)
    entry_periood.grid(row=4, column=1, padx=10, pady=10)

    # Perioodi ühiku valik (dropdown)
    label_perioodi_ühik = tk.Label(kalkulaator_aken, text="Vali perioodi ühik:")
    label_perioodi_ühik.grid(row=5, column=0, padx=10, pady=10)

    var_periood_units = tk.StringVar(value="Aastates")
    perioodi_ühik_options = ["Aastates", "Kuudes"]
    dropdown_periood_units = tk.OptionMenu(kalkulaator_aken, var_periood_units, *perioodi_ühik_options)
    dropdown_periood_units.grid(row=5, column=1, padx=10, pady=10)

    # Nupp arvutamiseks
    def laenukalkulaator():
        try:
            laenusumma = float(entry_laenusumma.get())
            sissemakse = float(entry_sissemakse.get())
            intress = float(entry_intress.get())
            periood = int(entry_periood.get())
            perioodi_ühik = var_periood_units.get()

            # Arvutame sissemakse järgi uue laenusumma
            laenusumma = laenusumma - sissemakse

            # Kas periood on aastates või kuudes
            if perioodi_ühik == "Aastates":
                periood_kuudes = periood * 12  # Aastad kuudeks
            else:
                periood_kuudes = periood  # Kui periood on juba kuudes

            # Aastane intress jagatakse 12 kuuks
            kuine_intress = intress / 100 / 12

            # Annuiteedi valem: (P * r * (1 + r)^n) / ((1 + r)^n - 1)
            kuine_makse = laenusumma * kuine_intress * math.pow(1 + kuine_intress, periood_kuudes) / (math.pow(1 + kuine_intress, periood_kuudes) - 1)

            # Kuvame tulemuse
            label_tulemus.config(text=f"Igakuine makse: {kuine_makse:.2f} €")

        except ValueError:
            label_tulemus.config(text="Palun sisesta kehtivad numbrid.")

    # Nupp arvutamiseks
    button_arvuta = tk.Button(kalkulaator_aken, text="Arvuta", command=laenukalkulaator)
    button_arvuta.grid(row=6, columnspan=2, pady=20)

    # Tulemuse kuvamine
    label_tulemus = tk.Label(kalkulaator_aken, text="Igakuine makse: ")
    label_tulemus.grid(row=7, columnspan=2, pady=10)

# Funktsioon, mis avab kalkulaator 2 akna
def avada_kalkulaator2():
    # Peidame peamise akna
    root.withdraw()

    kalkulaator_aken = tk.Toplevel(root)
    kalkulaator_aken.title("Kalkulaator 2")
    kalkulaator_aken.geometry("400x300")
    
    # Tagasi nupp paigutatud vasakusse ülanurka
    button_tagasi = tk.Button(kalkulaator_aken, text="Tagasi", command=lambda: tagasi(kalkulaator_aken))
    button_tagasi.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    label2 = tk.Label(kalkulaator_aken, text="Siin on Kalkulaator 2, sisestage vajalikud andmed.")
    label2.grid(row=1, column=0, padx=10, pady=10)

# Funktsioon, mis avab kalkulaator 3 akna
def avada_kalkulaator3():
    # Peidame peamise akna
    root.withdraw()

    kalkulaator_aken = tk.Toplevel(root)
    kalkulaator_aken.title("Kalkulaator 3")
    kalkulaator_aken.geometry("400x300")
    
    # Tagasi nupp paigutatud vasakusse ülanurka
    button_tagasi = tk.Button(kalkulaator_aken, text="Tagasi", command=lambda: tagasi(kalkulaator_aken))
    button_tagasi.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

    label3 = tk.Label(kalkulaator_aken, text="Siin on Kalkulaator 3, sisestage vajalikud andmed.")
    label3.grid(row=1, column=0, padx=10, pady=10)

# Funktsioon, mis toob tagasi peamise akna
def tagasi(kalkulaator_aken):
    kalkulaator_aken.destroy()  # Sulgeme kalkulaatori akna
    root.deiconify()  # Kuvame tagasi peamise akna

# Peamine aken
root = tk.Tk()
root.title("Finantskalkulaator")

# Suur tekst pealkirjaga ja akna suurus
label_title = tk.Label(root, text="Finantskalkulaator", font=("Arial", 24))
label_title.grid(row=0, columnspan=2, padx=10, pady=40)

root.geometry("600x400")  # Suurendame algset akent

# Nupud kalkulaatorite avamiseks
button_kalkulaator1 = tk.Button(root, text="Kalkulaator 1", command=avada_laenukalkulaator)
button_kalkulaator1.grid(row=1, column=0, padx=10, pady=20)

button_kalkulaator2 = tk.Button(root, text="Kalkulaator 2", command=avada_kalkulaator2)
button_kalkulaator2.grid(row=1, column=1, padx=10, pady=20)

button_kalkulaator3 = tk.Button(root, text="Kalkulaator 3", command=avada_kalkulaator3)
button_kalkulaator3.grid(row=2, column=0, padx=10, pady=20)

# Aken jääb avatuks
root.mainloop()
