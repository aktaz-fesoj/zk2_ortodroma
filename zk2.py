import tkinter as tk

#OKNO
window = tk.Tk()
window.title("Délka ortodromy")
window.resizable(width=False, height=False)

# VSTUPY
orto_vstup = tk.Frame(master=window)
n_nebo_s = tk.StringVar(orto_vstup)
n_nebo_s.set("N") #Základní hodnota budiž N

volba_ns = tk.OptionMenu(orto_vstup, n_nebo_s, "N", "S")
ent_stupne_a = tk.Entry(master=orto_vstup, width=7)
lbl_stupne_a = tk.Label(master=orto_vstup, text="°")
ent_minuty_a = tk.Entry(master=orto_vstup, width=7)
lbl_minuty_a = tk.Label(master=orto_vstup, text="'")
ent_vteriny_a = tk.Entry(master=orto_vstup, width=7)
lbl_vteriny_a = tk.Label(master=orto_vstup, text="''")

#GRIDY_VSTUPY
volba_ns.grid(row=0, column=0, sticky="e")
ent_stupne_a.grid(row=0, column=1, sticky="e")
lbl_stupne_a.grid(row=0, column=2, sticky="w")
ent_minuty_a.grid(row=0, column=3, sticky="e")
lbl_minuty_a.grid(row=0, column=4, sticky="w")
ent_vteriny_a.grid(row=0, column=5, sticky="e")
lbl_vteriny_a.grid(row=0, column=6, sticky="w")


#HLAVNI_GRIDY
orto_vstup.grid(row=0, column=0, padx=10)

#BĚH
window.mainloop()