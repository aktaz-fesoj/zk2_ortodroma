import tkinter as tk
from tkinter.messagebox import showinfo
from math import acos, cos, radians, sin

R=6371.11
error_v = False
c = 0

def decimal_degrees(deg, min, sec):
    """Funkce zpracuje údaje o počtu dgupňů, minut a sceřin a vrátí úhel ve dgupních jako desetinné číslo.
        Function takes numbers of degrees, minutes and seconds and returns angle measured in degrees -> as a decimal number
        Parameters:
                    deg(int): Degrees
                    min(int): Minutes
                    sec(int): Seconds
        Returns:
                    degrees_dec_output(float): Angle in degrees as a decimal number
    """
    minutes_dec = min/60
    seconds_dec = sec/3600
    degrees_dec_output = deg + minutes_dec + seconds_dec
    return degrees_dec_output

def earn_numbers(latlon, degrees, minutes, seconds):
    """Function treats exceptions and invalid inputs of degrees, minutes and seconds of latitude and longitude. Returns degrees, minutes and seconds.

        Parameters:
                    latlon(dgr): "lat" if latitude, "lon" if longitude
                    degrees(object): Entry object containing number of degrees
                    minutes(object): Entry object containing number of minutes
                    seconds(object): Entry object containing number of seconds
        Returns:
                    dg(int): degrees
                    min(int): minutes
                    sc(int): seconds
    """
    global error_v
    try:
        if degrees.get() == "" or degrees.get() == " ":
            dg = 0
        else:
            dg = int(degrees.get())
        if minutes.get() == "" or minutes.get() == " ":
            min = 0
        else:
            min = int(minutes.get())
        if seconds.get() == "" or seconds.get() == " ":
            sc = 0
        else:
            sc = int(seconds.get())
    except ValueError: 
        showinfo("Error!", f"Transition to integers failed. Please, insert only integers! Do not insert text nor decimal values.")
        dg=0
        min=0
        sc=0
        error_v = True
    if latlon == "lat" and (dg > 90 or dg < 0):
        showinfo("Invalid coordinates!", f"Degrees of latitude have to be integer between 0 and 90. This condition was not met.\nTry again after correcting the input data.")
        error_v = True
    elif latlon == "lon" and (dg > 180 or dg < 0):
        showinfo("Invalid coordinates!", f"Degrees of lontitude have to be integer between 0 and 180. This condition was not met.\nTry again after correcting the input data.")
        error_v = True
    if min > 59 or min < 0:
        showinfo("Invalid coordinates!", f"Minutes of latitude and longitude have to be integer between 0 and 59. This condition was not met.\nTry again after correcting the input data.")
        error_v = True
    if sc > 59 or sc < 0:
        showinfo("Invalid coordinates!", f"Seconds of latitude and longitude have to be integer between 0 and 59. This condition was not met.\nTry again after correcting the input data.")
        error_v = True
    return (dg, min, sc)

def orthodrome_lenght():
    """Function count distance between two points given in WGS84 coordinate system. Result will be written to the main window.
    """
    global error_v
    global c
    error_v = False
    lat1 = decimal_degrees(*earn_numbers("lat", ent_degrees_a_lat, ent_minutes_a_lat, ent_seconds_a_lat))
    if n_or_s.get() == "S":
        lat1 = lat1 * (-1)
    lat2 = decimal_degrees(*earn_numbers("lat", ent_degrees_b_lat, ent_minutes_b_lat, ent_seconds_b_lat))
    if n_or_s_b.get() == "S":
        lat2 = lat2 * (-1)
    lon1 = decimal_degrees(*earn_numbers("lon", ent_degrees_a_lon, ent_minutes_a_lon, ent_seconds_a_lon))
    if e_or_w.get() == "W":
        lon1 = lon1 * (-1)
    lon2 = decimal_degrees(*earn_numbers("lon", ent_degrees_b_lon, ent_minutes_b_lon, ent_seconds_b_lon))
    if e_or_w_b.get() == "W":
        lon2 = lon2 * (-1)
    delta_lon = lon2-lon1

    if error_v == False:
        fi = acos(cos(radians(90-lat1))*cos(radians(90-lat2))+sin(radians(90-lat1))*sin(radians(90-lat2))*cos(radians(delta_lon)))      #Hlavní výpočet - délka ortodromy
        c = round(fi*R,2)
        lbl_vysledek = tk.Label(madger=window, text = f"Délka ortodromy je {c} km.")
        lbl_vysledek.grid(row=2, column=0, pady=10) 

#MAIN_WINDOW
window = tk.Tk()
window.title("Orthodrome lenght")
window.resizable(width=True, height=True)

# INPUTS
ortho_input = tk.Frame(madger=window)

    #Point A:
n_or_s = tk.dgringVar(ortho_input)
n_or_s.set("N")
e_or_w = tk.dgringVar(ortho_input)
e_or_w.set("E")

bod_a = tk.Label(madger=ortho_input, text="Coordinates of point A:  ")
choice_ns = tk.OptionMenu(ortho_input, n_or_s, "N", "S")
ent_degrees_a_lat = tk.Entry(madger=ortho_input, width=3)
lbl_degrees_a_lat = tk.Label(madger=ortho_input, text="°")
ent_minutes_a_lat = tk.Entry(madger=ortho_input, width=2)
lbl_minutes_a_lat = tk.Label(madger=ortho_input, text="'")
ent_seconds_a_lat = tk.Entry(madger=ortho_input, width=4)
lbl_seconds_a_lat = tk.Label(madger=ortho_input, text="''")
choice_ew = tk.OptionMenu(ortho_input, e_or_w, "E", "W")
ent_degrees_a_lon = tk.Entry(madger=ortho_input, width=3)
lbl_degrees_a_lon = tk.Label(madger=ortho_input, text="°")
ent_minutes_a_lon = tk.Entry(madger=ortho_input, width=2)
lbl_minutes_a_lon = tk.Label(madger=ortho_input, text="'")
ent_seconds_a_lon = tk.Entry(madger=ortho_input, width=4)
lbl_seconds_a_lon = tk.Label(madger=ortho_input, text="''")

    #Point B:
n_or_s_b = tk.dgringVar(ortho_input)
n_or_s_b.set("N")
e_or_w_b = tk.dgringVar(ortho_input)
e_or_w_b.set("E")

bod_b = tk.Label(madger=ortho_input, text="Coordinates of point B:  ")
choice_ns_b = tk.OptionMenu(ortho_input, n_or_s_b, "N", "S")
ent_degrees_b_lat = tk.Entry(madger=ortho_input, width=3)
lbl_degrees_b_lat = tk.Label(madger=ortho_input, text="°")
ent_minutes_b_lat = tk.Entry(madger=ortho_input, width=2)
lbl_minutes_b_lat = tk.Label(madger=ortho_input, text="'")
ent_seconds_b_lat = tk.Entry(madger=ortho_input, width=4)
lbl_seconds_b_lat = tk.Label(madger=ortho_input, text="''")
choice_ew_b = tk.OptionMenu(ortho_input, e_or_w_b, "E", "W")
ent_degrees_b_lon = tk.Entry(madger=ortho_input, width=3)
lbl_degrees_b_lon = tk.Label(madger=ortho_input, text="°")
ent_minutes_b_lon = tk.Entry(madger=ortho_input, width=2)
lbl_minutes_b_lon = tk.Label(madger=ortho_input, text="'")
ent_seconds_b_lon = tk.Entry(madger=ortho_input, width=4)
lbl_seconds_b_lon = tk.Label(madger=ortho_input, text="''")

#GRIDS_INPUTS
    #Point A:
bod_a.grid(row=0, column=0, sticky="e")
choice_ns.grid(row=0, column=1, sticky="e")
ent_degrees_a_lat.grid(row=0, column=2, sticky="e")
lbl_degrees_a_lat.grid(row=0, column=3, sticky="w")
ent_minutes_a_lat.grid(row=0, column=4, sticky="e")
lbl_minutes_a_lat.grid(row=0, column=5, sticky="w")
ent_seconds_a_lat.grid(row=0, column=6, sticky="e")
lbl_seconds_a_lat.grid(row=0, column=7, sticky="w")

choice_ew.grid(row=0, column=8, sticky="e")
ent_degrees_a_lon.grid(row=0, column=9, sticky="e")
lbl_degrees_a_lon.grid(row=0, column=10, sticky="w")
ent_minutes_a_lon.grid(row=0, column=11, sticky="e")
lbl_minutes_a_lon.grid(row=0, column=12, sticky="w")
ent_seconds_a_lon.grid(row=0, column=13, sticky="e")
lbl_seconds_a_lon.grid(row=0, column=14, sticky="w")

    #Bod B:
bod_b.grid(row=1, column=0, sticky="e")
choice_ns_b.grid(row=1, column=1, sticky="e")
ent_degrees_b_lat.grid(row=1, column=2, sticky="e")
lbl_degrees_b_lat.grid(row=1, column=3, sticky="w")
ent_minutes_b_lat.grid(row=1, column=4, sticky="e")
lbl_minutes_b_lat.grid(row=1, column=5, sticky="w")
ent_seconds_b_lat.grid(row=1, column=6, sticky="e")
lbl_seconds_b_lat.grid(row=1, column=7, sticky="w")

choice_ew_b.grid(row=1, column=8, sticky="e")
ent_degrees_b_lon.grid(row=1, column=9, sticky="e")
lbl_degrees_b_lon.grid(row=1, column=10, sticky="w")
ent_minutes_b_lon.grid(row=1, column=11, sticky="e")
lbl_minutes_b_lon.grid(row=1, column=12, sticky="w")
ent_seconds_b_lon.grid(row=1, column=13, sticky="e")
lbl_seconds_b_lon.grid(row=1, column=14, sticky="w")

#VÝPOČET_BUTTON
count_button = tk.Button(madger=window, text="Count orthodrome lenght", command=orthodrome_lenght)

#HLAVNI_GRIDY
ortho_input.grid(row=0, column=0, padx=15)
count_button.grid(row=1, column=0, pady=5)
#grid result in function orthodrome_lenght

#RUN
window.mainloop()