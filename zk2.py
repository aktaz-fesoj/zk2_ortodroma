import tkinter as tk
from math import acos, cos, radians, sin, pi

R=6371.11
def stupne_desetinne(stup, min, vter):
    minuty_des = min/60
    vteriny_des = vter/3600
    stupne_des_vystup = stup + minuty_des + vteriny_des
    return stupne_des_vystup


def delka_ortodromy():
    lat1 = stupne_desetinne(int(ent_stupne_a_lat.get()), int(ent_minuty_a_lat.get()), int(ent_vteriny_a_lat.get()))
    if volba_ns == "S":
        lat1 = lat1 * (-1)
    lat2 = stupne_desetinne(int(ent_stupne_b_lat.get()), int(ent_minuty_b_lat.get()), int(ent_vteriny_b_lat.get()))
    if volba_ns_b == "S":
        lat2 = lat2 * (-1)
    lon1 = stupne_desetinne(int(ent_stupne_a_lon.get()), int(ent_minuty_a_lon.get()), int(ent_vteriny_a_lon.get()))
    if volba_ew == "W":
        lon1 = lon1 * (-1)
    lon2 = stupne_desetinne(int(ent_stupne_b_lon.get()), int(ent_minuty_b_lon.get()), int(ent_vteriny_b_lon.get()))
    if volba_ew_b == "W":
        lon2 = lon2 * (-1)
    delta_lon = lon2-lon1

    fi = acos(cos(radians(90-lat1))*cos(radians(90-lat2))+sin(radians(90-lat1))*sin(radians(90-lat2))*cos(radians(delta_lon)))
    c = fi*R
    print(c)    
    return c

#OKNO
window = tk.Tk()
window.title("Délka ortodromy")
window.resizable(width=False, height=False)

# VSTUPY
orto_vstup = tk.Frame(master=window)

#Bod A:
n_nebo_s = tk.StringVar(orto_vstup)
n_nebo_s.set("N") #Základní hodnota budiž N
e_nebo_w = tk.StringVar(orto_vstup)
e_nebo_w.set("E") #Základní hodnota budiž E

bod_a = tk.Label(master=orto_vstup, text="Souřadnice bodu A:  ")
volba_ns = tk.OptionMenu(orto_vstup, n_nebo_s, "N", "S")
ent_stupne_a_lat = tk.Entry(master=orto_vstup, width=3)
lbl_stupne_a_lat = tk.Label(master=orto_vstup, text="°")
ent_minuty_a_lat = tk.Entry(master=orto_vstup, width=2)
lbl_minuty_a_lat = tk.Label(master=orto_vstup, text="'")
ent_vteriny_a_lat = tk.Entry(master=orto_vstup, width=4)
lbl_vteriny_a_lat = tk.Label(master=orto_vstup, text="''")
volba_ew = tk.OptionMenu(orto_vstup, e_nebo_w, "E", "W")
ent_stupne_a_lon = tk.Entry(master=orto_vstup, width=3)
lbl_stupne_a_lon = tk.Label(master=orto_vstup, text="°")
ent_minuty_a_lon = tk.Entry(master=orto_vstup, width=2)
lbl_minuty_a_lon = tk.Label(master=orto_vstup, text="'")
ent_vteriny_a_lon = tk.Entry(master=orto_vstup, width=4)
lbl_vteriny_a_lon = tk.Label(master=orto_vstup, text="''")

#Bod B:
n_nebo_s_b = tk.StringVar(orto_vstup)
n_nebo_s_b.set("N") #Základní hodnota budiž N
e_nebo_w_b = tk.StringVar(orto_vstup)
e_nebo_w_b.set("E") #Základní hodnota budiž E

bod_b = tk.Label(master=orto_vstup, text="Souřadnice bodu B:  ")
volba_ns_b = tk.OptionMenu(orto_vstup, n_nebo_s_b, "N", "S")
ent_stupne_b_lat = tk.Entry(master=orto_vstup, width=3)
lbl_stupne_b_lat = tk.Label(master=orto_vstup, text="°")
ent_minuty_b_lat = tk.Entry(master=orto_vstup, width=2)
lbl_minuty_b_lat = tk.Label(master=orto_vstup, text="'")
ent_vteriny_b_lat = tk.Entry(master=orto_vstup, width=4)
lbl_vteriny_b_lat = tk.Label(master=orto_vstup, text="''")
volba_ew_b = tk.OptionMenu(orto_vstup, e_nebo_w_b, "E", "W")
ent_stupne_b_lon = tk.Entry(master=orto_vstup, width=3)
lbl_stupne_b_lon = tk.Label(master=orto_vstup, text="°")
ent_minuty_b_lon = tk.Entry(master=orto_vstup, width=2)
lbl_minuty_b_lon = tk.Label(master=orto_vstup, text="'")
ent_vteriny_b_lon = tk.Entry(master=orto_vstup, width=4)
lbl_vteriny_b_lon = tk.Label(master=orto_vstup, text="''")

#GRIDY_VSTUPY
#Bod A:
bod_a.grid(row=0, column=0, sticky="e")
volba_ns.grid(row=0, column=1, sticky="e")
ent_stupne_a_lat.grid(row=0, column=2, sticky="e")
lbl_stupne_a_lat.grid(row=0, column=3, sticky="w")
ent_minuty_a_lat.grid(row=0, column=4, sticky="e")
lbl_minuty_a_lat.grid(row=0, column=5, sticky="w")
ent_vteriny_a_lat.grid(row=0, column=6, sticky="e")
lbl_vteriny_a_lat.grid(row=0, column=7, sticky="w")

volba_ew.grid(row=0, column=8, sticky="e")
ent_stupne_a_lon.grid(row=0, column=9, sticky="e")
lbl_stupne_a_lon.grid(row=0, column=10, sticky="w")
ent_minuty_a_lon.grid(row=0, column=11, sticky="e")
lbl_minuty_a_lon.grid(row=0, column=12, sticky="w")
ent_vteriny_a_lon.grid(row=0, column=13, sticky="e")
lbl_vteriny_a_lon.grid(row=0, column=14, sticky="w")

#Bod B:
bod_b.grid(row=1, column=0, sticky="e")
volba_ns_b.grid(row=1, column=1, sticky="e")
ent_stupne_b_lat.grid(row=1, column=2, sticky="e")
lbl_stupne_b_lat.grid(row=1, column=3, sticky="w")
ent_minuty_b_lat.grid(row=1, column=4, sticky="e")
lbl_minuty_b_lat.grid(row=1, column=5, sticky="w")
ent_vteriny_b_lat.grid(row=1, column=6, sticky="e")
lbl_vteriny_b_lat.grid(row=1, column=7, sticky="w")

volba_ew_b.grid(row=1, column=8, sticky="e")
ent_stupne_b_lon.grid(row=1, column=9, sticky="e")
lbl_stupne_b_lon.grid(row=1, column=10, sticky="w")
ent_minuty_b_lon.grid(row=1, column=11, sticky="e")
lbl_minuty_b_lon.grid(row=1, column=12, sticky="w")
ent_vteriny_b_lon.grid(row=1, column=13, sticky="e")
lbl_vteriny_b_lon.grid(row=1, column=14, sticky="w")


#VÝPOČET-BUTTON + VÝSLEDEK
vypocti_tlacitko = tk.Button(
    master=window,
    text="Vypočti délku ortodromy",
    command=delka_ortodromy
)

#HLAVNI_GRIDY
orto_vstup.grid(row=0, column=0, padx=15)
vypocti_tlacitko.grid(row=1, column=0)

#BĚH
window.mainloop()