import tkinter as tk
from tkinter.messagebox import showinfo
from math import acos, cos, radians, sin, pi
import sys

eps = sys.float_info.epsilon
R=6371.11
error_g = False

def decimal_degrees(deg, min, sec):
    """Function takes numbers of degrees, minutes and seconds and returns angle measured in degrees -> as a decimal number

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

def interval_control(c, a, b, text):
    global error_g
    if c < a or c > b:
        error_g = True
        showinfo("Invalid coordinates!", f"{text} have to be integer between {a} and {b}. This condition was not met.\nTry again after correcting the input data.")

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
    global error_g
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
        error_g = True
    if latlon == "lat":
        interval_control(dg, 0, 90, "Degrees of latitude")
    elif latlon == "lon":
        interval_control(dg, 0, 180, "Degrees of longitude")
    interval_control(min, 0, 59, "Minutes of latitude and longitude")
    interval_control(sc, 0, 59, "Seconds of latitude and longitude")
    return (dg, min, sc)

def orthodrome_lenght(lat1, lon1, lat2, lon2, R):
    """Function counts distance between two points given in WGS84 coordinate system. Result will be written to the main window.
    """
    delta_lon = lon2-lon1
    inside_acos = cos(0.5*pi-lat1)*cos(0.5*pi-lat2)+sin(0.5*pi-lat1)*sin(0.5*pi-lat2)*cos(delta_lon)
    if (abs(inside_acos)-1 > eps):
        print("An error occured. Value for arcus cosinus function is out of domain. The program has stopped.")
    if (abs(inside_acos)-1 < eps):
        round(inside_acos, 0)
    sig = acos(inside_acos)
    c = round(sig*R,2)
    return c
    

def click_ortho_button():
    global error_g
    error_g = False

    lat1 = radians(decimal_degrees(*earn_numbers("lat", ent_degrees_a_lat, ent_minutes_a_lat, ent_seconds_a_lat)))
    if n_or_s.get() == "S":
        lat1 = lat1 * (-1)
    lat2 = radians(decimal_degrees(*earn_numbers("lat", ent_degrees_b_lat, ent_minutes_b_lat, ent_seconds_b_lat)))
    if n_or_s_b.get() == "S":
        lat2 = lat2 * (-1)
    lon1 = radians(decimal_degrees(*earn_numbers("lon", ent_degrees_a_lon, ent_minutes_a_lon, ent_seconds_a_lon)))
    if e_or_w.get() == "W":
        lon1 = lon1 * (-1)
    lon2 = radians(decimal_degrees(*earn_numbers("lon", ent_degrees_b_lon, ent_minutes_b_lon, ent_seconds_b_lon)))
    if e_or_w_b.get() == "W":
        lon2 = lon2 * (-1)

    if error_g == False:
        c = orthodrome_lenght(lat1, lon1, lat2, lon2, R)
        lbl_result = tk.Label(master=window, text = f"Orthodrome lenght is {c} km.")
        lbl_result.grid(row=2, column=0, pady=10)

def enter_is_within(P, a, b):
    a = int(a)
    b = int(b)
    try:
        P = int(P)
    except:
        return False
    if P<a or P>b:
        return False
    else:
        return True

def enter_wrong(a,b, dg_min_sc):
    showinfo("Invalid input!", f"Invalid input! Insert integer between {a} and {b} in the {dg_min_sc} field.")

#MAIN_WINDOW
window = tk.Tk()
window.title("Orthodrome lenght")
window.resizable(width=True, height=True)

# INPUTS
ortho_input = tk.Frame(master=window)

    #Point A:
n_or_s = tk.StringVar(ortho_input)
n_or_s.set("N")
e_or_w = tk.StringVar(ortho_input)
e_or_w.set("E")

reg = window.register(enter_is_within)
inv = window.register(enter_wrong)

bod_a = tk.Label(master=ortho_input, text="Coordinates of point A:  ")
choice_ns = tk.OptionMenu(ortho_input, n_or_s, "N", "S")
ent_degrees_a_lat = tk.Entry(master=ortho_input, width=3)
ent_degrees_a_lat.insert(0,"00")
lbl_degrees_a_lat = tk.Label(master=ortho_input, text="°")
ent_minutes_a_lat = tk.Entry(master=ortho_input, width=2)
ent_minutes_a_lat.insert(0,"00")
lbl_minutes_a_lat = tk.Label(master=ortho_input, text="'")
ent_seconds_a_lat = tk.Entry(master=ortho_input, width=4)
ent_seconds_a_lat.insert(0,"000")
lbl_seconds_a_lat = tk.Label(master=ortho_input, text="''")
choice_ew = tk.OptionMenu(ortho_input, e_or_w, "E", "W")
ent_degrees_a_lon = tk.Entry(master=ortho_input, width=3)
ent_degrees_a_lon.insert(0,"000")
lbl_degrees_a_lon = tk.Label(master=ortho_input, text="°")
ent_minutes_a_lon = tk.Entry(master=ortho_input, width=2)
ent_minutes_a_lon.insert(0,"00")
lbl_minutes_a_lon = tk.Label(master=ortho_input, text="'")
ent_seconds_a_lon = tk.Entry(master=ortho_input, width=4)
ent_seconds_a_lon.insert(0,"000")
lbl_seconds_a_lon = tk.Label(master=ortho_input, text="''")

    #Point B:
n_or_s_b = tk.StringVar(ortho_input)
n_or_s_b.set("N")
e_or_w_b = tk.StringVar(ortho_input)
e_or_w_b.set("E")

bod_b = tk.Label(master=ortho_input, text="Coordinates of point B:  ")
choice_ns_b = tk.OptionMenu(ortho_input, n_or_s_b, "N", "S")
ent_degrees_b_lat = tk.Entry(master=ortho_input, width=3, validate= "focusout", validatecommand= (reg, "%P",0,90), invalidcommand=(inv, 0, 90, "degrees"))
ent_degrees_b_lat.insert(0,"00")
lbl_degrees_b_lat = tk.Label(master=ortho_input, text="°")
ent_minutes_b_lat = tk.Entry(master=ortho_input, width=2)
ent_minutes_b_lat.insert(0,"00")
lbl_minutes_b_lat = tk.Label(master=ortho_input, text="'")
ent_seconds_b_lat = tk.Entry(master=ortho_input, width=4)
ent_seconds_b_lat.insert(0,"000")
lbl_seconds_b_lat = tk.Label(master=ortho_input, text="''")
choice_ew_b = tk.OptionMenu(ortho_input, e_or_w_b, "E", "W")
ent_degrees_b_lon = tk.Entry(master=ortho_input, width=3)
ent_degrees_b_lon.insert(0,"00")
lbl_degrees_b_lon = tk.Label(master=ortho_input, text="°")
ent_minutes_b_lon = tk.Entry(master=ortho_input, width=2)
ent_minutes_b_lon.insert(0,"00")
lbl_minutes_b_lon = tk.Label(master=ortho_input, text="'")
ent_seconds_b_lon = tk.Entry(master=ortho_input, width=4)
ent_seconds_b_lon.insert(0,"000")
lbl_seconds_b_lon = tk.Label(master=ortho_input, text="''")


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

#COUNT_BUTTON
count_button = tk.Button(master=window, text="Count orthodrome lenght", command=click_ortho_button)

#MAIN_GRIPS
ortho_input.grid(row=0, column=0, padx=15)
count_button.grid(row=1, column=0, pady=5)
#grid result in function orthodrome_lenght

#RUN
window.mainloop()