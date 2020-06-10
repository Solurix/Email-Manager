"""
This is mail_menager.
It was my first ever project with python which I started without the even knowledge of classes.
This is the reason why there is so much of unnecessary code. However, it works.
I'am in the process of transforming this from hard coded to easily editable program.


"""

import pyperclip
import csv
import os
from tkinter import *
from tkinter import messagebox, ttk
from ttkthemes import ThemedStyle
from datetime import datetime, timedelta, date
from functools import partial

# TODO REORGANIZE THE WHOLE FILE: put all text for display in some csv, divide structure ang main functions

# TODO Create place for writing own name
# TODO Display the file's load name in more readable way
# TODO Add 追加情報 and　仮レート to save options
# TODO Check if reset button works well
# TODO Make it possible to change 追加情報 in change tab
# TODO (later) create a pdf with hotel reservation confirmation (宿泊証明書）based on saved file
# TODO Remove Polish text


today = date.today()

root = Tk()
root.title("Mail Manager 2 ver 0.1")
root.option_add("*Font", "helvetica 12")
root.state('zoomed')
style = ThemedStyle(root)
style.set_theme("radiance")

tabControl = ttk.Notebook(root)

tab1 = ttk.Frame(tabControl)

frame2 = Frame(tab1)
frame2.grid(row=0, column=1, rowspan=2)
# background_image = PhotoImage(file="logo2.png")
# background_label = Label(frame2, image=background_image)
# background_label.pack()

s = ttk.Style()
s.configure('.', font=('Helvetica', 13))
s.configure("TCheckbutton", font=('Helvetica', 20))
# s.configure("TMenubutton", font=('Helvetica', 40))


tab2 = ttk.Frame(tabControl)
tab3 = ttk.Frame(tabControl)

tabControl.add(tab1, text='宿泊料金計算')
tabControl.add(tab2, text='内容変更')
tabControl.add(tab3, text='ロード')

tabControl.pack(expand=1, fill="both")

tabControl_changes = ttk.Notebook(tab2)

tab_change_rates = ttk.Frame(tabControl_changes)
tab_change_info = ttk.Frame(tabControl_changes)

tabControl_changes.add(tab_change_rates, text='レート調整')
tabControl_changes.add(tab_change_info, text='追加情報')

tabControl_changes.pack(expand=1, fill="both")

###################################################################################################
############################################# Rooms ###############################################
###################################################################################################

rooms_number = 0
rooms = []
the_rooms = []


def delete_csv(name, row):
    os.remove(name)
    ttk.Label(load_frame, text="  削除済").grid(row=row, column=3)


def load_csv(name):
    with open(name, encoding="utf-8") as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for_load = dict(csv.reader(csvDataFile))
    r_count = 0
    for room in the_rooms:
        if for_load[str((room.name, "rank"))]:
            r_count += 1
    for _ in range(rooms_number - 1):
        remove_room()
    for _ in range(r_count - 1):
        add_room()
    for room in the_rooms:
        room.year = int(for_load[str((room.name, "year"))])
        room.month = int(for_load[str((room.name, "month"))])
        room.day = int(for_load[str((room.name, "day"))])
        room.adults = int(for_load[str((room.name, "adults"))])
        room.kids = int(for_load[str((room.name, "kids"))])
        room.babies = int(for_load[str((room.name, "babies"))])
        room.breakfast = bool(for_load[str((room.name, "breakfast"))])
        room.member = bool(for_load[str((room.name, "member"))])
        room.rank = for_load[str((room.name, "rank"))]
        room.r_type = for_load[str((room.name, "r_type"))]
    g_count = 0
    for gi in range(8):
        if for_load[str(("Guest_name ", gi + 1))]:
            g_count += 1
    for _ in range(guest_number):
        remove_guest()
    for _ in range(g_count):
        add_guest()
    for guest in range(8):
        e_guest_list[guest].delete(0, END)
        e_guest_list[guest].insert(0, for_load[str(("Guest_name ", guest + 1))])
        v_sex_list[guest + 1].set(int(for_load[str(("Guest_sex ", guest + 1))]))
        guest_rooms_list[guest].set(for_load[str(("Guest_room ", guest + 1))])
    e_representant.delete(0, END)
    e_representant.insert(0, for_load[str("representant_name")])
    res_number.delete(0, END)
    res_number.insert(0, int(for_load[str("res_number")]))

    checkyear.delete(0, END)
    checkyear.insert(END, Room1.year)
    checkmonth.delete(0, END)
    checkmonth.insert(END, Room1.month)
    checkday.delete(0, END)
    checkday.insert(END, Room1.day)
    v_adult.set(Room1.adults - 1)
    v_children.set(Room1.kids)
    v_baby.set(Room1.babies)
    v_tbf.set(Room1.breakfast)
    v_jrhm.set(Room1.member)
    e_ranks.delete(0, END)
    e_ranks.insert(END, Room1.rank)
    v_rtype.set(Room1.r_type)
    change_room()


### Load
files = []
load_frame = ttk.Frame(tab3)
load_frame.pack()
for r, d, f in os.walk("saves"):
    for file in f:
        if '.csv' in file:
            files.append(os.path.join(r, file))
nrx = 1
for save in files:
    name = save[6:-4]
    load_this = partial(load_csv, save)
    delete_this = partial(delete_csv, save, nrx)
    ttk.Label(load_frame, text=name).grid(row=nrx, column=0)
    ttk.Button(load_frame, text="ロード", command=load_this).grid(row=nrx, column=1)
    ttk.Button(load_frame, text="削除", command=delete_this).grid(row=nrx, column=2)
    nrx += 1

# <editor-fold desc="Change info">

tab_change_info_mf = ttk.Frame(tab_change_info)
tab_change_info_mf.grid(row=0, column=0)

with open('new_data.csv', encoding="utf-8") as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    data = list(csv.reader(csvDataFile))

rowx = 0
info_entry_list = []
info_entry_list_jap = []
for row in data:
    ttk.Label(tab_change_info_mf, text=row[0], width=17, anchor="center").grid(row=rowx, column=0, rowspan=2)
    x = ttk.Entry(tab_change_info_mf, width=120)
    x.insert(0, row[1])
    x.grid(row=rowx, column=1)
    info_entry_list.append(x)
    y = ttk.Entry(tab_change_info_mf, width=120)
    y.insert(0, row[2])
    y.grid(row=rowx + 1, column=1)
    info_entry_list_jap.append(y)
    rowx += 2


def new_info():
    ## Reaction to click on change button
    if psw_entry.get() == "password":
        psw_entry.delete(0, END)
        psw_entry.insert(0, "変更済")
        with open('new_data.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=',')
            for z in range(len(data)):
                writer.writerow([data[z][0], info_entry_list[z].get(), info_entry_list_jap[z].get()])
    else:
        psw_entry.delete(0, END)
        psw_entry.insert(0, "パスワードが間違っている。")


tab_change_info_sf = Frame(tab_change_info)
tab_change_info_sf.grid(row=1, column=0)
ttk.Label(tab_change_info_sf, text='パスワード').grid(row=0, column=0)
psw_entry = ttk.Entry(tab_change_info_sf, width=40)
psw_entry.grid(row=0, column=1)
ttk.Button(tab_change_info_sf, text="変更", command=lambda: new_info()).grid(row=0, column=2)
# </editor-fold>

###  Below is definitely the worst part of this code.
###  Going to change it soon.
# <editor-fold desc="Tab 2 - Rates">
##############################################################
######## TAB 2 ### DO NOT TOUCH ##############################
##############################################################


rates_frame = ttk.Frame(tab_change_rates)
rates_frame.pack()

# Finding the position of rates in file with rates (rates.txt)
f = open("rates.txt", "r")
RATY = f.read()

# <editor-fold desc="Raty">
raty_NDY = [RATY.find("NDY A"), RATY.find("NDY B"), RATY.find("NDY C"), RATY.find("NDY D"), RATY.find("NDY E"),
            RATY.find("NDY F"), RATY.find("NDY G"), RATY.find("NDY H"), RATY.find("NDY I"), RATY.find("NDY J"),
            RATY.find("NDY K"), RATY.find("NDY L")]
raty_2DY = [RATY.find("2DY A"), RATY.find("2DY B"), RATY.find("2DY C"), RATY.find("2DY D"), RATY.find("2DY E"),
            RATY.find("2DY F"), RATY.find("2DY G"), RATY.find("2DY H"), RATY.find("2DY I"), RATY.find("2DY J"),
            RATY.find("2DY K"), RATY.find("2DY L")]
raty_NTY = [RATY.find("NTY A"), RATY.find("NTY B"), RATY.find("NTY C"), RATY.find("NTY D"), RATY.find("NTY E"),
            RATY.find("NTY F"), RATY.find("NTY G"), RATY.find("NTY H"), RATY.find("NTY I"), RATY.find("NTY J"),
            RATY.find("NTY K"), RATY.find("NTY L")]
raty_2TY = [RATY.find("2TY A"), RATY.find("2TY B"), RATY.find("2TY C"), RATY.find("2TY D"), RATY.find("2TY E"),
            RATY.find("2TY F"), RATY.find("2TY G"), RATY.find("2TY H"), RATY.find("2TY I"), RATY.find("2TY J"),
            RATY.find("2TY K"), RATY.find("2TY L")]
raty_NDS = [RATY.find("NDS A"), RATY.find("NDS B"), RATY.find("NDS C"), RATY.find("NDS D"), RATY.find("NDS E"),
            RATY.find("NDS F"), RATY.find("NDS G"), RATY.find("NDS H"), RATY.find("NDS I"), RATY.find("NDS J"),
            RATY.find("NDS K"), RATY.find("NDS L")]
raty_2DS = [RATY.find("2DS A"), RATY.find("2DS B"), RATY.find("2DS C"), RATY.find("2DS D"), RATY.find("2DS E"),
            RATY.find("2DS F"), RATY.find("2DS G"), RATY.find("2DS H"), RATY.find("2DS I"), RATY.find("2DS J"),
            RATY.find("2DS K"), RATY.find("2DS L")]
raty_NDD = [RATY.find("NDD A"), RATY.find("NDD B"), RATY.find("NDD C"), RATY.find("NDD D"), RATY.find("NDD E"),
            RATY.find("NDD F"), RATY.find("NDD G"), RATY.find("NDD H"), RATY.find("NDD I"), RATY.find("NDD J"),
            RATY.find("NDD K"), RATY.find("NDD L")]
raty_2DD = [RATY.find("2DD A"), RATY.find("2DD B"), RATY.find("2DD C"), RATY.find("2DD D"), RATY.find("2DD E"),
            RATY.find("2DD F"), RATY.find("2DD G"), RATY.find("2DD H"), RATY.find("2DD I"), RATY.find("2DD J"),
            RATY.find("2DD K"), RATY.find("2DD L")]
raty_NTD = [RATY.find("NTD A"), RATY.find("NTD B"), RATY.find("NTD C"), RATY.find("NTD D"), RATY.find("NTD E"),
            RATY.find("NTD F"), RATY.find("NTD G"), RATY.find("NTD H"), RATY.find("NTD I"), RATY.find("NTD J"),
            RATY.find("NTD K"), RATY.find("NTD L")]
raty_2TD = [RATY.find("2TD A"), RATY.find("2TD B"), RATY.find("2TD C"), RATY.find("2TD D"), RATY.find("2TD E"),
            RATY.find("2TD F"), RATY.find("2TD G"), RATY.find("2TD H"), RATY.find("2TD I"), RATY.find("2TD J"),
            RATY.find("2TD K"), RATY.find("2TD L")]
raty_3TD = [RATY.find("3TD A"), RATY.find("3TD B"), RATY.find("3TD C"), RATY.find("3TD D"), RATY.find("3TD E"),
            RATY.find("3TD F"), RATY.find("3TD G"), RATY.find("3TD H"), RATY.find("3TD I"), RATY.find("3TD J"),
            RATY.find("3TD K"), RATY.find("3TD L")]
raty_NDP = [RATY.find("NDP A"), RATY.find("NDP B"), RATY.find("NDP C"), RATY.find("NDP D"), RATY.find("NDP E"),
            RATY.find("NDP F"), RATY.find("NDP G"), RATY.find("NDP H"), RATY.find("NDP I"), RATY.find("NDP J"),
            RATY.find("NDP K"), RATY.find("NDP L")]
raty_2DP = [RATY.find("2DP A"), RATY.find("2DP B"), RATY.find("2DP C"), RATY.find("2DP D"), RATY.find("2DP E"),
            RATY.find("2DP F"), RATY.find("2DP G"), RATY.find("2DP H"), RATY.find("2DP I"), RATY.find("2DP J"),
            RATY.find("2DP K"), RATY.find("2DP L")]
raty_NTP = [RATY.find("NTP A"), RATY.find("NTP B"), RATY.find("NTP C"), RATY.find("NTP D"), RATY.find("NTP E"),
            RATY.find("NTP F"), RATY.find("NTP G"), RATY.find("NTP H"), RATY.find("NTP I"), RATY.find("NTP J"),
            RATY.find("NTP K"), RATY.find("NTP L")]
raty_2TP = [RATY.find("2TP A"), RATY.find("2TP B"), RATY.find("2TP C"), RATY.find("2TP D"), RATY.find("2TP E"),
            RATY.find("2TP F"), RATY.find("2TP G"), RATY.find("2TP H"), RATY.find("2TP I"), RATY.find("2TP J"),
            RATY.find("2TP K"), RATY.find("2TP L")]
raty_NSU = [RATY.find("NSU A"), RATY.find("NSU B"), RATY.find("NSU C"), RATY.find("NSU D"), RATY.find("NSU E"),
            RATY.find("NSU F"), RATY.find("NSU G"), RATY.find("NSU H"), RATY.find("NSU I"), RATY.find("NSU J"),
            RATY.find("NSU K"), RATY.find("NSU L")]
raty_NDU = [RATY.find("NDU A"), RATY.find("NDU B"), RATY.find("NDU C"), RATY.find("NDU D"), RATY.find("NDU E"),
            RATY.find("NDU F"), RATY.find("NDU G"), RATY.find("NDU H"), RATY.find("NDU I"), RATY.find("NDU J"),
            RATY.find("NDU K"), RATY.find("NDU L")]
raty_2DU = [RATY.find("2DU A"), RATY.find("2DU B"), RATY.find("2DU C"), RATY.find("2DU D"), RATY.find("2DU E"),
            RATY.find("2DU F"), RATY.find("2DU G"), RATY.find("2DU H"), RATY.find("2DU I"), RATY.find("2DU J"),
            RATY.find("2DU K"), RATY.find("2DU L")]
# </editor-fold>

# Rates names (A:L)
nazwy = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
rodzaje = ['NDY 1人', 'NDY 2人', 'NTY 1人', 'NTY 2人', 'NDS 1人', 'NDS 2人', 'NDD 1人', 'NDD 2人',
           'NTD 1人', 'NTD 2人', 'NTD 3人', 'NDP 1人', 'NDP 2人', 'NTP 1人', 'NTP 2人', 'NSU 1人', 'NDU 1人', 'NDU 2人']

# All labels
for l in range(18):
    ttk.Label(rates_frame, text=rodzaje[l], font='Helvetica 13 bold').grid(row=l + 1)

# <editor-fold desc="Names">
# Creating names for next formula
qNDY = ["ndyA", "ndyB", "ndyC", "ndyD", "ndyE", "ndyF", "ndyG", "ndyH", "ndyI", "ndyJ", "ndyK", "ndyL"]
q2DY = ["2dyA", "2dyB", "2dyC", "2dyD", "2dyE", "2dyF", "2dyG", "2dyH", "2dyI", "2dyJ", "2dyK", "2dyL"]
qNTY = ["ntyA", "ntyB", "ntyC", "ntyD", "ntyE", "ntyF", "ntyG", "ntyH", "ntyI", "ntyJ", "ntyK", "ntyL"]
q2TY = ["2tyA", "2tyB", "2tyC", "2tyD", "2tyE", "2tyF", "2tyG", "2tyH", "2tyI", "2tyJ", "2tyK", "2tyL"]
qNDS = ["ndsA", "ndsB", "ndsC", "ndsD", "ndsE", "ndsF", "ndsG", "ndsH", "ndsI", "ndsJ", "ndsK", "ndsL"]
q2DS = ["2dsA", "2dsB", "2dsC", "2dsD", "2dsE", "2dsF", "2dsG", "2dsH", "2dsI", "2dsJ", "2dsK", "2dsL"]
qNDD = ["nddA", "nddB", "nddC", "nddD", "nddE", "nddF", "nddG", "nddH", "nddI", "nddJ", "nddK", "nddL"]
q2DD = ["2ddA", "2ddB", "2ddC", "2ddD", "2ddE", "2ddF", "2ddG", "2ddH", "2ddI", "2ddJ", "2ddK", "2ddL"]
qNTD = ["ntdA", "ntdB", "ntdC", "ntdD", "ntdE", "ntdF", "ntdG", "ntdH", "ntdI", "ntdJ", "ntdK", "ntdL"]
q2TD = ["2tdA", "2tdB", "2tdC", "2tdD", "2tdE", "2tdF", "2tdG", "2tdH", "2tdI", "2tdJ", "2tdK", "2tdL"]
q3TD = ["3tdA", "3tdB", "3tdC", "3tdD", "3tdE", "3tdF", "3tdG", "3tdH", "3tdI", "3tdJ", "3tdK", "3tdL"]
qNDP = ["ndpA", "ndpB", "ndpC", "ndpD", "ndpE", "ndpF", "ndpG", "ndpH", "ndpI", "ndpJ", "ndpK", "ndpL"]
q2DP = ["2dpA", "2dpB", "2dpC", "2dpD", "2dpE", "2dpF", "2dpG", "2dpH", "2dpI", "2dpJ", "2dpK", "2dpL"]
qNTP = ["ntpA", "ntpB", "ntpC", "ntpD", "ntpE", "ntpF", "ntpG", "ntpH", "ntpI", "ntpJ", "ntpK", "ntpL"]
q2TP = ["2tpA", "2tpB", "2tpC", "2tpD", "2tpE", "2tpF", "2tpG", "2tpH", "2tpI", "2tpJ", "2tpK", "2tpL"]
qNSU = ["nsuA", "nsuB", "nsuC", "nsuD", "nsuE", "nsuF", "nsuG", "nsuH", "nsuI", "nsuJ", "nsuK", "nsuL"]
qNDU = ["nduA", "nduB", "nduC", "nduD", "nduE", "nduF", "nduG", "nduH", "nduI", "nduJ", "nduK", "nduL"]
q2DU = ["2duA", "2duB", "2duC", "2duD", "2duE", "2duF", "2duG", "2duH", "2duI", "2duJ", "2duK", "2duL"]

kolory1 = ['floral white', 'old lace', 'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque',
           'peach puff', 'navajo white', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4']
# </editor-fold>

# <editor-fold desc="Creating a table">
# Creating a table
for x in range(12):    ttk.Label(rates_frame, text=nazwy[x], font='Helvetica 13 bold').grid(row=0, column=2 * x + 2)
for x in range(12):
    qNDY[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    qNDY[x].config(width=7, font=('times', 14))
    qNDY[x].insert(0, RATY[raty_NDY[x] + 8:raty_NDY[x] + 14])
    qNDY[x].grid(row=1, column=2 * x + 2)
for x in range(12):
    q2DY[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    q2DY[x].config(width=7, font=('times', 14))
    q2DY[x].insert(0, RATY[raty_2DY[x] + 8:raty_2DY[x] + 14])
    q2DY[x].grid(row=2, column=2 * x + 2)
for x in range(12):
    qNTY[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    qNTY[x].config(width=7, font=('times', 14))
    qNTY[x].insert(0, RATY[raty_NTY[x] + 8:raty_NTY[x] + 14])
    qNTY[x].grid(row=3, column=2 * x + 2)
for x in range(12):
    q2TY[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    q2TY[x].config(width=7, font=('times', 14))
    q2TY[x].insert(0, RATY[raty_2TY[x] + 8:raty_2TY[x] + 14])
    q2TY[x].grid(row=4, column=2 * x + 2)
for x in range(12):
    qNDS[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    qNDS[x].config(width=7, font=('times', 14))
    qNDS[x].insert(0, RATY[raty_NDS[x] + 8:raty_NDS[x] + 14])
    qNDS[x].grid(row=5, column=2 * x + 2)
for x in range(12):
    q2DS[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    q2DS[x].config(width=7, font=('times', 14))
    q2DS[x].insert(0, RATY[raty_2DS[x] + 8:raty_2DS[x] + 14])
    q2DS[x].grid(row=6, column=2 * x + 2)
for x in range(12):
    qNDD[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    qNDD[x].config(width=7, font=('times', 14))
    qNDD[x].insert(0, RATY[raty_NDD[x] + 8:raty_NDD[x] + 14])
    qNDD[x].grid(row=7, column=2 * x + 2)
for x in range(12):
    q2DD[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    q2DD[x].config(width=7, font=('times', 14))
    q2DD[x].insert(0, RATY[raty_2DD[x] + 8:raty_2DD[x] + 14])
    q2DD[x].grid(row=8, column=2 * x + 2)
for x in range(12):
    qNTD[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    qNTD[x].config(width=7, font=('times', 14))
    qNTD[x].insert(0, RATY[raty_NTD[x] + 8:raty_NTD[x] + 14])
    qNTD[x].grid(row=9, column=2 * x + 2)
for x in range(12):
    q2TD[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    q2TD[x].config(width=7, font=('times', 14))
    q2TD[x].insert(0, RATY[raty_2TD[x] + 8:raty_2TD[x] + 14])
    q2TD[x].grid(row=10, column=2 * x + 2)
for x in range(12):
    q3TD[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    q3TD[x].config(width=7, font=('times', 14))
    q3TD[x].insert(0, RATY[raty_3TD[x] + 8:raty_3TD[x] + 14])
    q3TD[x].grid(row=11, column=2 * x + 2)
for x in range(12):
    qNDP[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    qNDP[x].config(width=7, font=('times', 14))
    qNDP[x].insert(0, RATY[raty_NDP[x] + 8:raty_NDP[x] + 14])
    qNDP[x].grid(row=12, column=2 * x + 2)
for x in range(12):
    q2DP[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    q2DP[x].config(width=7, font=('times', 14))
    q2DP[x].insert(0, RATY[raty_2DP[x] + 8:raty_2DP[x] + 14])
    q2DP[x].grid(row=13, column=2 * x + 2)
for x in range(12):
    qNTP[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    qNTP[x].config(width=7, font=('times', 14))
    qNTP[x].insert(0, RATY[raty_NTP[x] + 8:raty_NTP[x] + 14])
    qNTP[x].grid(row=14, column=2 * x + 2)
for x in range(12):
    q2TP[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    q2TP[x].config(width=7, font=('times', 14))
    q2TP[x].insert(0, RATY[raty_2TP[x] + 8:raty_2TP[x] + 14])
    q2TP[x].grid(row=15, column=2 * x + 2)
for x in range(12):
    qNSU[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    qNSU[x].config(width=7, font=('times', 14))
    qNSU[x].insert(0, RATY[raty_NSU[x] + 8:raty_NSU[x] + 14])
    qNSU[x].grid(row=16, column=2 * x + 2)
for x in range(12):
    qNDU[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    qNDU[x].config(width=7, font=('times', 14))
    qNDU[x].insert(0, RATY[raty_NDU[x] + 8:raty_NDU[x] + 14])
    qNDU[x].grid(row=17, column=2 * x + 2)
for x in range(12):
    q2DU[x] = Entry(rates_frame, bg=kolory1[x], fg="black")
    q2DU[x].config(width=7, font=('times', 14))
    q2DU[x].insert(0, RATY[raty_2DU[x] + 8:raty_2DU[x] + 14])
    q2DU[x].grid(row=18, column=2 * x + 2)

f.close()


# Creating a definition for a 'change' button = saving new rates to rates.exe

def zamiana():
    if password.get() == "password":
        nowe_raty = RATY

        for x in range(12):
            nowa_rata = "NDY " + nazwy[x] + " = " + qNDY[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_NDY[x]:raty_NDY[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "2DY " + nazwy[x] + " = " + q2DY[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_2DY[x]:raty_2DY[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "NTY " + nazwy[x] + " = " + qNTY[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_NTY[x]:raty_NTY[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "2TY " + nazwy[x] + " = " + q2TY[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_2TY[x]:raty_2TY[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "NDS " + nazwy[x] + " = " + qNDS[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_NDS[x]:raty_NDS[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "2DS " + nazwy[x] + " = " + q2DS[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_2DS[x]:raty_2DS[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "NDD " + nazwy[x] + " = " + qNDD[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_NDD[x]:raty_NDD[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "2DD " + nazwy[x] + " = " + q2DD[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_2DD[x]:raty_2DD[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "NTD " + nazwy[x] + " = " + qNTD[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_NTD[x]:raty_NTD[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "2TD " + nazwy[x] + " = " + q2TD[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_2TD[x]:raty_2TD[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "3TD " + nazwy[x] + " = " + q3TD[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_3TD[x]:raty_3TD[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "NDP " + nazwy[x] + " = " + qNDP[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_NDP[x]:raty_NDP[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "2DP " + nazwy[x] + " = " + q2DP[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_2DP[x]:raty_2DP[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "NTP " + nazwy[x] + " = " + qNTP[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_NTP[x]:raty_NTP[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "2TP " + nazwy[x] + " = " + q2TP[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_2TP[x]:raty_2TP[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "NSU " + nazwy[x] + " = " + qNSU[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_NSU[x]:raty_NSU[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "NDU " + nazwy[x] + " = " + qNDU[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_NDU[x]:raty_NDU[x] + 14], nowa_rata)
        for x in range(12):
            nowa_rata = "2DU " + nazwy[x] + " = " + q2DU[x].get() + "   "
            nowe_raty = nowe_raty.replace(RATY[raty_2DU[x]:raty_2DU[x] + 14], nowa_rata)

        ###########################################
        ### STILL TAB2 BUT YOU MAY TOUCH BELOW ####
        ###########################################

        ## Reaction to click on change button
        file = open("rates.txt", "w")
        file.write(nowe_raty)
        file.close()
        w = Message(tab2, text="変更完了!", width=700, bg="black", fg="red", font="times, 20")
        w.pack(fill=BOTH)
        password.config(fg="black")
        password.delete(first=0, last=22)
    else:
        password.config(fg="red")


button = ttk.Button(rates_frame, text="変更", command=zamiana)
button.grid(row=20, column=0)

haslo = ttk.Label(tab_change_rates, text='パスワード')
haslo.pack(side=BOTTOM)
password = Entry(tab_change_rates, font="Verdana 22")
password.pack(side=BOTTOM)
# </editor-fold>
# </editor-fold>


###################################################################################################
############################################# TAB 1 ###############################################
###################################################################################################

# <editor-fold desc="Left column">
#######################
###################### Left column
#####################


# Big frame
frame1 = ttk.Frame(tab1)
frame1.grid(column=0, row=0, sticky=N)

# Frame with buttons
miniframe = ttk.Frame(frame1)
miniframe.pack()

# <editor-fold desc="Check-in">
# Check-in date
check = ttk.Label(miniframe, text="Check-in")
check.pack()

# Check-in year
checkyear = Entry(miniframe)
checkyear.insert(0, today.year)
checkyear.config(width=5, font=('times', 18))
checkyear.pack(side=LEFT)
checkyear.focus_set()
ttk.Label(miniframe, text='年').pack(side=LEFT)

checkmonth = Entry(miniframe)
checkmonth.insert(0, today.month)
checkmonth.config(width=3, font=('times', 18))
checkmonth.pack(side=LEFT)
ttk.Label(miniframe, text='月').pack(side=LEFT)

# Check-in day
checkday = Entry(miniframe)
checkday.insert(0, today.day)
checkday.config(width=3, font=('times', 18))
checkday.pack(side=LEFT)
label = ttk.Label(miniframe, text='日')
label.pack(side=LEFT)
# </editor-fold>


# Number of adults
ttk.Label(frame1, text="""\n 大人""", justify=LEFT).pack()

miniframe2 = ttk.Frame(frame1)
miniframe2.pack()

v_adult = IntVar()
v_adult.set(1)
for val, language in enumerate(["1", "2", "3", ]):
    Radiobutton(miniframe2, text=language, indicatoron=0, overrelief="ridge", bg="#f6f4f2", fg="#62564f", width=5,
                variable=v_adult, value=val).pack(
        side=LEFT)

# Children 7-12 - counts as adult for room rate but have different price for breakfast
v_children = IntVar()
v_children.set(0)
ttk.Label(frame1, text="""\n 子供 7-12""", justify=LEFT).pack()

miniframe3 = ttk.Frame(frame1)
miniframe3.pack()

for val, language in enumerate(["0", "1", "2"]):
    Radiobutton(miniframe3, text=language, indicatoron=0, overrelief="ridge", bg="#f6f4f2", fg="#62564f", width=1,
                padx=20, variable=v_children,
                value=val).pack(side=LEFT)

# Children 0-6 - no changes in prices
v_baby = IntVar()
v_baby.set(0)
ttk.Label(frame1, text="""\n 添い寝 0-6""", justify=LEFT).pack()
miniframe4 = ttk.Frame(frame1)
miniframe4.pack()

for val, language in enumerate(["0", "1", "2", "3"]):
    Radiobutton(miniframe4, text=language, indicatoron=0, width=1, overrelief="ridge", bg="#f6f4f2", fg="#62564f",
                padx=20, variable=v_baby,
                value=val).pack(side=LEFT)

# Breakfast, JRHM (Yes/No)
TBFHM = ttk.Frame(frame1)
TBFHM.pack()
v_tbf = IntVar()
v_tbf.set(0)

ttk.Label(TBFHM, text="\n朝食", anchor=CENTER, width=10).grid(row=0, column=0, columnspan=2)

for val, language in enumerate(["無", "有"]):
    Radiobutton(TBFHM, text=language, indicatoron=0, width=1, overrelief="ridge", bg="#f6f4f2", fg="#62564f", padx=19,
                variable=v_tbf, value=val).grid(row=1, column=val, sticky=W)

ttk.Label(TBFHM, text="", width=3).grid(row=0, column=2)
ttk.Label(TBFHM, text="\nJRHM", anchor=CENTER, width=10).grid(row=0, column=3, columnspan=2)
v_jrhm = IntVar()
v_jrhm.set(0)

for val, language in enumerate(["無", "有"]):
    Radiobutton(TBFHM, text=language, indicatoron=0, width=1, padx=19, overrelief="ridge", bg="#f6f4f2", fg="#62564f",
                variable=v_jrhm, value=val).grid(row=1, column=val + 3, sticky=E)

# Entry for rates (A : L)
ttk.Label(frame1, text="\n ランク").pack()
e_ranks = Entry(frame1)
e_ranks.pack(ipadx=38)

# Label with room types
ttk.Label(frame1, text="Room type").pack()
OptionList = ["NDY", "NTY", "NDS", "NDD", "NTD", "NDP", "NTP", "NSU", "NDU"]
v_rtype = StringVar(frame1)
v_rtype.set(OptionList[0])

opt = ttk.OptionMenu(frame1, v_rtype, OptionList[1], *OptionList)
opt.config(width=8)
opt['menu'].configure(font=('Futura', 15))
opt.pack()

## Language
miniframe5 = ttk.Frame(frame1)

v_language = IntVar()
v_language.set(1)

ttk.Label(miniframe5, text="言語", width=6).grid(row=0, column=0)

for val, language in enumerate(["日本語", "English"]):
    ttk.Radiobutton(miniframe5, text=language, state=DISABLED, variable=v_language, padding=8,
                    command=lambda: unlock_radiobutton(r_btn_repr_sex),
                    value=val).grid(row=0, column=val + 1)


def unlock_radiobutton(r_btn_name):
    if str(r_btn_name[0].cget("state")) == "normal":
        for y in range(len(r_btn_name)):
            r_btn_name[y].config(state=DISABLED)
    else:
        for y in range(len(r_btn_name)):
            r_btn_name[y].config(state=NORMAL)


ttk.Label(miniframe5, text="目的", width=6).grid(row=1, column=0)
v_reserv = IntVar()
v_reserv.set(0)

for val, language in enumerate(["案内用", "確認用"]):
    ttk.Radiobutton(miniframe5, text=language, variable=v_reserv,
                    value=val).grid(row=1, column=val + 1)

miniframe6 = ttk.Frame(tab1, relief=GROOVE, borderwidth=1)
miniframe6.grid(column=0, sticky=N, row=1)
btn_add_room = ttk.Button(miniframe6, text="部屋追加", width=23,
                          command=lambda: add_room())
btn_add_room.grid(row=0, column=0)
miniframe66 = ttk.Frame(miniframe6, padding=21, borderwidth=2)
miniframe66.grid(column=0, row=1)

v_rooms = IntVar()
v_rooms.set(0)
x1 = (1, 1, 1, 1, 2, 2, 2, 2)
rooms_names = []
miniframe5.pack()
btn_rem_room = ttk.Button(miniframe6, text="部屋削除", width=23,
                          command=lambda: remove_room())
btn_rem_room.grid(row=3, column=0, sticky=S)


def add_room():
    global rooms_number, rooms, btn_add_room, rooms_names, v_g1_room, v_g2_room, v_g3_room, v_g4_room, v_g5_room
    global v_g6_room, v_g7_room, v_g8_room, miniframe66
    if rooms_number < 8:
        komunikat.delete('1.0', END)
        komunikat.insert(END, "部屋追加済")
        rooms_number += 1
        rooms.append(str(rooms_number))
        rooms_names.append("Room " + str(rooms_number))
        if rooms_number > 4:
            miniframe66.config(padding=7, borderwidth=0)
        elif rooms_number == 4:
            miniframe66.config(padding=20, borderwidth=0)
        else:
            miniframe66.config(padding=20, borderwidth=2)
        for val, language in enumerate(rooms):
            Radiobutton(miniframe66, text=language, indicatoron=0, width=2, overrelief="ridge", bg="#f6f4f2",
                        fg="#62564f", padx=10, variable=v_rooms,
                        command=lambda: change_room(), value=val).grid(row=x1[val], column=val % 4)

        for w in range(8):
            opt2 = OptionMenu(guest_frame_list[w], guest_rooms_list[w], *rooms_names)
            opt2.config(width=6, bg="#f6f4f2", fg="#62564f")
            opt2.grid(row=0, column=1, columnspan=4)
        for o in range(9 - rooms_number):
            guest_rooms_list[rooms_number - 1 + o].set(rooms_names[-1])

        the_rooms[rooms_number - 1].year = checkyear.get()
        the_rooms[rooms_number - 1].month = checkmonth.get()
        the_rooms[rooms_number - 1].day = checkday.get()
        the_rooms[rooms_number - 1].adults = v_adult.get() + 1
        the_rooms[rooms_number - 1].kids = v_children.get()
        the_rooms[rooms_number - 1].babies = v_baby.get()
        the_rooms[rooms_number - 1].breakfast = v_tbf.get()
        the_rooms[rooms_number - 1].member = v_jrhm.get()
        the_rooms[rooms_number - 1].rank = e_ranks.get()
        the_rooms[rooms_number - 1].r_type = v_rtype.get()

    activate_disable()


def remove_room():
    global rooms_number, rooms, miniframe66, btn_rem_room, btn_add_room
    if rooms_number > 0:
        rooms.remove(str(rooms_number))
        rooms_names.remove("Room " + str(rooms_number))
        rooms_number -= 1
    miniframe66.destroy()
    miniframe66 = ttk.Frame(miniframe6)
    if rooms_number > 4:
        miniframe66.config(padding=7, borderwidth=0)
    elif rooms_number == 4:
        miniframe66.config(padding=20, borderwidth=0)
    else:
        miniframe66.config(padding=20, borderwidth=2)
    miniframe66.grid(column=0, row=1)
    for val, language in enumerate(rooms):
        Radiobutton(miniframe66, text=language, indicatoron=0, width=2, overrelief="ridge", bg="#f6f4f2", fg="#62564f",
                    padx=10, variable=v_rooms,
                    command=lambda: change_room(), value=val).grid(row=x1[val], column=val % 4)
    for o in range(9 - rooms_number):
        guest_rooms_list[rooms_number - 1 + o].set(rooms_names[-1])
    for w in range(8):
        opt2 = OptionMenu(guest_frame_list[w], guest_rooms_list[w], *rooms_names)
        opt2.config(width=6, bg="#f6f4f2", fg="#62564f")
        opt2.grid(row=0, column=1, columnspan=4)
    activate_disable()


def activate_disable():
    if rooms_number == 1:
        btn_rem_room.config(state=DISABLED)
    elif rooms_number == 2:
        btn_rem_room.config(state=NORMAL)
    elif rooms_number == 8:
        btn_add_room.config(state=DISABLED)
    elif rooms_number == 7:
        btn_add_room.config(state=NORMAL)


# </editor-fold>

# <editor-fold desc="Middle column">
#######################
###################### Middle column - frame for text intended to copy
#####################


T = Text(frame2)
T.config(font=('times', 14), height=29, width=78)
T.pack()
# </editor-fold>

# <editor-fold desc="Right column">
#######################
###################### Right column
#####################

tabControl2 = ttk.Notebook(tab1)

tab11 = ttk.Frame(tabControl)
tab12 = ttk.Frame(tabControl)
tab13 = ttk.Frame(tabControl)
tab14 = ttk.Frame(tabControl)

tabControl2.add(tab11, text='お客様情報')
tabControl2.add(tab12, text='リクエスト')
tabControl2.add(tab13, text='追加情報')
tabControl2.add(tab14, text='仮レート')

tabControl2.grid(row=0, column=2, rowspan=3, sticky=N)

# <editor-fold desc="Frame 3　Guests">
frame3 = ttk.Frame(tab11)
frame3.pack()

# <editor-fold desc="Representant frame">
fr_representant = ttk.Frame(frame3)
fr_representant.grid(row=0, column=0, sticky=N)

ttk.Label(fr_representant, text="\n お客様情報", font=('Helvetica', 20)).grid(row=0, column=0)
ttk.Label(fr_representant, text="\n 予約者の名前").grid(row=1, column=0)
ttk.Label(fr_representant, text="\n 性別").grid(row=1, column=2)
ttk.Label(fr_representant, text="\n").grid(row=2, column=0)
ttk.Label(fr_representant, text="\n 予約番号 #").grid(row=0, column=0, sticky=S + E, columnspan=2)
res_number = Entry(fr_representant, width=10)
res_number.insert(0, "1000")
res_number.grid(row=0, column=2, sticky=S + E, columnspan=2, padx=6)

sama = False


def change_title():
    global sama
    if rooms_number > 0:
        if sama:
            btn_change_title.configure(text="Mr./Ms.")
            sama = False
            for R in range(len(r_btn_sex_list)):
                r_btn_sex_list[R].config(state=NORMAL)

        else:
            btn_change_title.configure(text="様")
            sama = True
            for R in range(len(r_btn_sex_list)):
                r_btn_sex_list[R].config(state=DISABLED)


btn_change_title = ttk.Button(fr_representant, text="Mr./Ms.", command=lambda: change_title())
btn_change_title.grid(row=3, column=1, columnspan=3)

e_representant = Entry(fr_representant)
e_representant.grid(ipadx=20, row=2, column=0)

v_sex_0 = IntVar()
v_sex_0.set(2)

r_btn_repr_sex = []
for val, language in enumerate(["男", "女", "不明"]):
    r_btn_repr_sex.append(ttk.Radiobutton(fr_representant, text=language, variable=v_sex_0,
                                          value=val))
    r_btn_repr_sex[-1].grid(row=2, column=val + 1)
# </editor-fold>

# <editor-fold desc="Guest Values">
v_sex_1 = IntVar()
v_sex_1.set(2)
v_sex_2 = IntVar()
v_sex_2.set(2)
v_sex_3 = IntVar()
v_sex_3.set(2)
v_sex_4 = IntVar()
v_sex_4.set(2)
v_sex_5 = IntVar()
v_sex_5.set(2)
v_sex_6 = IntVar()
v_sex_6.set(2)
v_sex_7 = IntVar()
v_sex_7.set(2)
v_sex_8 = IntVar()
v_sex_8.set(2)
# </editor-fold>

v_sex_list = (v_sex_0, v_sex_1, v_sex_2, v_sex_3, v_sex_4, v_sex_5, v_sex_6, v_sex_7, v_sex_8)

# <editor-fold desc="Guest frames">
fr_g1 = ttk.Frame(frame3)
fr_g2 = ttk.Frame(frame3)
fr_g3 = ttk.Frame(frame3)
fr_g4 = ttk.Frame(frame3)
fr_g5 = ttk.Frame(frame3)
fr_g6 = ttk.Frame(frame3)
fr_g7 = ttk.Frame(frame3)
fr_g8 = ttk.Frame(frame3)
# </editor-fold>

guest_frame_list = (fr_g1, fr_g2, fr_g3, fr_g4, fr_g5, fr_g6, fr_g7, fr_g8)

# <editor-fold desc="Guest entries">
e_guest1 = Entry(fr_g1)
e_guest2 = Entry(fr_g2)
e_guest3 = Entry(fr_g3)
e_guest4 = Entry(fr_g4)
e_guest5 = Entry(fr_g5)
e_guest6 = Entry(fr_g6)
e_guest7 = Entry(fr_g7)
e_guest8 = Entry(fr_g8)
e_guest1.grid(row=1, column=0, ipadx=20)
e_guest2.grid(row=1, column=0, ipadx=20)
e_guest3.grid(row=1, column=0, ipadx=20)
e_guest4.grid(row=1, column=0, ipadx=20)
e_guest5.grid(row=1, column=0, ipadx=20)
e_guest6.grid(row=1, column=0, ipadx=20)
e_guest7.grid(row=1, column=0, ipadx=20)
e_guest8.grid(row=1, column=0, ipadx=20)
# </editor-fold>
e_guest_list = (e_guest1, e_guest2, e_guest3, e_guest4, e_guest5, e_guest6, e_guest7, e_guest8)

# <editor-fold desc="Guest rooms">
v_g1_room = StringVar(fr_g1)
v_g2_room = StringVar(fr_g2)
v_g3_room = StringVar(fr_g3)
v_g4_room = StringVar(fr_g4)
v_g5_room = StringVar(fr_g5)
v_g6_room = StringVar(fr_g6)
v_g7_room = StringVar(fr_g7)
v_g8_room = StringVar(fr_g8)
# </editor-fold>

guest_rooms_list = (v_g1_room, v_g2_room, v_g3_room, v_g4_room, v_g5_room, v_g6_room, v_g7_room, v_g8_room)
r_btn_sex_list = []


# ("男", "女", "不明)

def assign_guests(room):
    this_room = []
    no = 0
    if sama:
        sex = ["", "", ""]
        after = "様"
    else:
        sex = ["Mr. ", "Ms. ", "Mr./Ms. "]
        after = ""
    for number in guest_rooms_list:
        if number.get() == room and e_guest_list[no].get() != "":
            this_room.append(sex[v_sex_list[no + 1].get()] + e_guest_list[no].get() + after)
        no += 1
    if len(this_room) > 1:
        new_list = ""
        no2 = 1
        for g in this_room:
            new_list += "\nGuest " + str(no2) + " : " + g
            no2 += 1
    elif len(this_room) == 1:
        new_list = "\nGuest : " + this_room[0]
    else:
        new_list = ""
    return new_list


for i in range(8):
    ttk.Label(guest_frame_list[i], text=("Guest " + str(i + 1))).grid(row=0, column=0)
    for val, language in enumerate(["男", "女", "不明"]):
        r_btn_sex_list.append(ttk.Radiobutton((guest_frame_list[i]), text=language,
                                              variable=v_sex_list[i + 1],
                                              value=val))
        r_btn_sex_list[-1].grid(row=1, column=val + 2)

guest_number = 0


def add_guest():
    global guest_number
    if guest_number < 8:
        global btn_g1, btn_g2
        btn_g1.grid_forget()
        if guest_number < 7:
            btn_g1 = ttk.Button(guest_frame_list[guest_number], text="お客様追加", command=lambda: add_guest())
            btn_g1.grid(row=3, column=0, columnspan=2)
        btn_g2.grid_forget()
        btn_g2 = ttk.Button(guest_frame_list[guest_number], text="削除", command=lambda: remove_guest())
        btn_g2.grid(row=3, column=2, columnspan=3)
        guest_frame_list[guest_number].grid(row=2 + guest_number, column=0)
        guest_number += 1


def remove_guest():
    global guest_number, btn_g2, btn_g1
    btn_g2.grid_forget()
    btn_g2 = ttk.Button(guest_frame_list[guest_number - 2], text="削除", command=lambda: remove_guest())
    btn_g2.grid(row=3, column=2, columnspan=3)
    guest_frame_list[guest_number - 1].grid_forget()
    e_guest_list[guest_number - 1].delete(0, END)
    btn_g1.grid_forget()
    btn_g1 = ttk.Button(guest_frame_list[guest_number - 2], text="お客様追加", command=lambda: add_guest())
    btn_g1.grid(row=3, column=0, columnspan=2)
    guest_number -= 1
    if guest_number == 0:
        btn_g2.grid_forget()
        btn_g1 = ttk.Button(fr_representant, text="お客様追加", command=lambda: add_guest())
        btn_g1.grid(row=4, column=0, columnspan=2)


btn_g1 = ttk.Button(fr_representant, text="お客様追加", command=lambda: add_guest())
btn_g2 = ttk.Button(frame3, text="削除", command=lambda: remove_guest())
btn_g1.grid(row=4, column=0, columnspan=2)

# </editor-fold>

# <editor-fold desc="Requests">
requests = ttk.Frame(tab12)
requests.pack()


def switch(x):
    if x:
        x.set(None)

ttk.Label(requests, text="Requests not enabled yet", font="Helvetica, 20").grid()

rq_highfloor = IntVar()
ttk.Checkbutton(requests, text="高層階", variable=rq_highfloor, command=lambda: switch(rq_lowfloor)).grid(
    row=1,
    sticky=W)
rq_lowfloor = IntVar()
ttk.Checkbutton(requests, text="低層階", variable=rq_lowfloor, command=lambda: switch(rq_highfloor)).grid(
    row=2,
    sticky=W)
rq_niceview = IntVar()
ttk.Checkbutton(requests, text="眺望", variable=rq_niceview).grid(row=3, sticky=W)
rq_close = IntVar()
ttk.Checkbutton(requests, text="T/W近く", variable=rq_close, command=lambda: switch(rq_not_close)).grid(
    row=4,
    sticky=W)
rq_not_close = IntVar()
ttk.Checkbutton(requests, text="T/W別の階", variable=rq_not_close, command=lambda: switch(rq_close)).grid(
    row=5,
    sticky=W)
rq_elv_close = IntVar()
ttk.Checkbutton(requests, text="EV近く", variable=rq_elv_close, command=lambda: switch(rq_elv_far)).grid(
    row=6,
    sticky=W)
rq_elv_far = IntVar()
ttk.Checkbutton(requests, text="EV遠く", variable=rq_elv_far, command=lambda: switch(rq_elv_close)).grid(
    row=7,
    sticky=W)
rq_quiet = IntVar()
ttk.Checkbutton(requests, text="静か", variable=rq_quiet).grid(row=8, sticky=W)
rq_nonsmoking = IntVar()
ttk.Checkbutton(requests, text="禁煙", variable=rq_nonsmoking).grid(row=9, sticky=W)

list_requests = [rq_highfloor, rq_lowfloor, rq_niceview, rq_close, rq_elv_close, rq_elv_far, rq_quiet, rq_nonsmoking]

# </editor-fold>

# <editor-fold desc="Additional information">
add_info = ttk.Frame(tab13)
add_info.pack()

info_button_list = {}

for x in range(len(data)):
    info_button_list[data[x][0]] = IntVar()
    ttk.Checkbutton(add_info, text=(data[x][0]), variable=(info_button_list[data[x][0]])).grid(row=x + 1, sticky=W)


def show_info():
    active_info = ""
    x = 0
    if v_language.get():
        w = 1
    else:
        w = 2
    for a in info_button_list:
        if info_button_list[a].get():
            active_info += data[x][w] + "\n"
        x += 1

    xi = "\nAdditional information :\n\n" + active_info

    if active_info == "":
        return ""
    else:
        return xi


# </editor-fold>

# <editor-fold desc="Temporary rates">
special_rates_list = ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
special_rates_frame = ttk.Frame(tab14)
ttk.Label(tab14, text="仮レート", font="Helvetica, 20").pack()
special_rates_frame.pack()

for X in range(len(special_rates_list)):
    ttk.Label(special_rates_frame, text=(special_rates_list[X] + "  "), borderwidth=12).grid(column=0, row=1 + X)
    special_rates_list[X] = ttk.Entry(special_rates_frame)
    special_rates_list[X].grid(column=1, row=1 + X)


# </editor-fold>


# </editor-fold>


#######################
###################### Creating a definition for calculating and creating the main text
#####################


class Room:

    def __init__(self, year, month, day, adults, kids, babies, breakfast, member, rank, r_type, name):
        self.year = year
        self.month = month
        self.day = day
        self.adults = adults
        self.kids = kids
        self.babies = babies
        self.breakfast = breakfast
        self.member = member
        self.rank = rank
        self.r_type = r_type
        self.name = name
        the_rooms.append(self)


Room1 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 1")
Room2 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 2")
Room3 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 3")
Room4 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 4")
Room5 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 5")
Room6 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 6")
Room7 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 7")
Room8 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 8")

active_room = the_rooms[v_rooms.get()]


def change_room():
    global active_room
    # T.insert(END, v_rooms.get())
    active_room.year = checkyear.get()
    active_room.month = checkmonth.get()
    active_room.day = checkday.get()
    active_room.adults = v_adult.get() + 1
    active_room.kids = v_children.get()
    active_room.babies = v_baby.get()
    active_room.breakfast = v_tbf.get()
    active_room.member = v_jrhm.get()
    active_room.rank = e_ranks.get().upper()
    active_room.r_type = v_rtype.get()
    active_room = the_rooms[v_rooms.get()]

    checkyear.delete(0, END)
    checkyear.insert(END, active_room.year)
    checkmonth.delete(0, END)
    checkmonth.insert(END, active_room.month)
    checkday.delete(0, END)
    checkday.insert(END, active_room.day)
    v_adult.set(active_room.adults - 1)
    v_children.set(active_room.kids)
    v_baby.set(active_room.babies)
    v_tbf.set(active_room.breakfast)
    v_jrhm.set(active_room.member)
    e_ranks.delete(0, END)
    e_ranks.insert(END, active_room.rank)
    v_rtype.set(active_room.r_type)


types_names = {
    "NTY": "Non-smoking Standard Twin room",
    "NTD": "Non-smoking Deluxe Twin room",
    "NTP": "Non-smoking Premium Twin room",
    "NDY": "Non-smoking Standard Double room",
    "NDD": "Non-smoking Deluxe Double room",
    "NDP": "Non-smoking Premium Double room",
    "NDS": "Non-smoking Superior Double room",
    "NDU": "Non-smoking Universal Double room",
    "NSU": "Non-smoking Universal Single room"}


class Confirmation:

    def __init__(self):
        self.total = 0
        self.groups = 0
        self.rooms_in_group = []
        self.room_type = []
        self.breakfast = []
        self.jrhm = []
        self.dates = []
        self.rates = []
        self.nights = []
        self.check_in_date = []
        self.check_out_date = []


con = Confirmation()


def create_excel():
    check_errors()
    with open('conf.csv', 'w', newline='', encoding="utf-8") as file:
        writer = csv.writer(file, delimiter=',')

        writer.writerow(["representant_name", e_representant.get()])
        writer.writerow(["representant_sex", v_sex_list[0].get()])
        writer.writerow(["res_number", res_number.get()])
        writer.writerow(["guest_number", guest_number])
        writer.writerow(["total", con.total])
        writer.writerow(["groups_no", con.groups])
        writer.writerow(["rooms_in_group", *con.rooms_in_group])
        writer.writerow(["room_type", *con.room_type])
        writer.writerow(["breakfast", *con.breakfast])
        writer.writerow(["jrhm", *con.jrhm])
        writer.writerow(["dates", *con.dates])
        writer.writerow(["rates", *con.rates])
        writer.writerow(["nights", *con.nights])
        writer.writerow(["check_in_date", *con.check_in_date])
        writer.writerow(["check_out_date", *con.check_out_date])

        for count, guest in enumerate(e_guest_list, 1):
            writer.writerow([("Guest_name ", count), guest.get()])
            writer.writerow([("Guest_sex ", count), v_sex_list[count].get()])
            writer.writerow([("Guest_room ", count), guest_rooms_list[count - 1].get()])


def check_errors():
    change_room()
    for nr in range(rooms_number):
        if not str(the_rooms[nr].month).isdigit() or (
                (int(the_rooms[nr].month) > 12) or (int(the_rooms[nr].month) < 1)):
            messagebox.showerror(("Room " + str(nr + 1) + " Error"), "月は1～12")
            break
        elif (int(the_rooms[nr].month) in (1, 3, 5, 7, 8, 10, 12)) and (not str(the_rooms[nr].day).isdigit() or
                                                                        (int(the_rooms[nr].day) > 31) or (
                                                                                int(the_rooms[nr].day) < 1)):
            messagebox.showerror(("Room " + str(nr + 1) + " Error"), (the_rooms[nr].month + "月は1～31"))
            break
        elif (int(the_rooms[nr].month) in (4, 6, 9, 11)) and (not str(the_rooms[nr].day).isdigit() or
                                                              (int(the_rooms[nr].day) > 30) or (
                                                                      int(the_rooms[nr].day) < 1)):
            messagebox.showerror(("Room " + str(nr + 1) + " Error"), (the_rooms[nr].month + "月は1～30"))
            break
        elif (int(the_rooms[nr].month) == 2) and (int(the_rooms[nr].year) % 4 != 0) and (
                not str(the_rooms[nr].day).isdigit()
                or (int(
            the_rooms[nr].day) > 28) or (int(the_rooms[nr].day) < 1)):
            messagebox.showerror(("Room " + str(nr + 1) + " Error"), (the_rooms[nr].month + "月は1～28"))
            break
        elif (int(the_rooms[nr].month) == 2) and (int(the_rooms[nr].year) % 4 == 0) and (
                not str(the_rooms[nr].day).isdigit()
                or (int(
            the_rooms[nr].day) > 29) or (int(the_rooms[nr].day) < 1)):
            messagebox.showerror(("Room " + str(nr + 1) + " Error"), (the_rooms[nr].month + "月は1～29"))
            break
        elif int(the_rooms[nr].adults) + int(the_rooms[nr].kids) > 3:
            messagebox.showerror(("Room " + str(nr + 1) + " Error"), "人数多すぎる")
            break
        elif (the_rooms[nr].r_type != "NTD") and (int(the_rooms[nr].adults) + int(the_rooms[nr].kids) > 2):
            messagebox.showerror(("Room " + str(nr + 1) + " Error"), "3人利用はNTDのみ")
            break
        elif re.search("[^a-zA-Z]", the_rooms[nr].rank):
            messagebox.showerror(("Room " + str(nr + 1) + " Error"), "ランクは A から Z までのローマ字、スペース無しで入力")
            break
    else:
        Mail()


def Mail():
    if True:
        change_room()
    sex = ["Mr. ", "Ms. ", "Mr./Ms. "]
    dear = "Dear " + sex[v_sex_0.get()] + e_representant.get() + ","
    thanks = ["taking interest in This Grand Hotel. \n\nBelow are detailed rates for the dates you have sent "
              "inquiry for:\n\n", "making reservation with This Grand Hotel. \n\nBelow is you reservation "
                                  "confirmation: \n\n"]
    thank_you = "\n\nThank you for " + thanks[v_reserv.get()]
    tbf_info = "\n>> Breakfast can be added for 2,750 JPY per person per day \n>>(1,650 JPY for children aged 7~12)."
    tax_info = "\n>> All prices are inclusive of tax."
    if rooms_number == 1:
        main_description = "Reservation for " + str(rooms_number) + " room. \nReservation number: #" + \
                           res_number.get()
    elif rooms_number > 0:
        main_description = "Reservation for " + str(rooms_number) + " rooms. \nReservation number: #" + \
                           res_number.get()

    else:
        main_description = "Reservation number: #" + res_number.get()
    # <editor-fold desc="Room groups">

    all_details = {"1": "", "2": "", "3": "", "4": "", "5": "", "6": "", "7": "", "8": ""}

    rm_groups = {1: [Room1], 2: "a", 3: "a", 4: "a", 5: "a", 6: "a", 7: "a", 8: "a"}
    groups = 0

    if rooms_number > 1:
        rm_list = []

        for i in range(rooms_number):
            rm_list.append(the_rooms[i])
        for r in range(rooms_number):
            u = 0
            temporary_group = []
            temporary_group.append(rm_list[0])
            rm_list.remove(rm_list[0])
            for k in range(len(rm_list)):
                if rm_list[u].year == temporary_group[0].year and rm_list[u].month == temporary_group[0].month and \
                        rm_list[u].day == temporary_group[0].day and rm_list[u].adults == temporary_group[0].adults and \
                        rm_list[u].kids == temporary_group[0].kids and rm_list[u].babies == temporary_group[
                    0].babies and rm_list[u].breakfast == temporary_group[0].breakfast and rm_list[u].member == \
                        temporary_group[0].member and rm_list[u].rank == temporary_group[0].rank and rm_list[
                    u].r_type == temporary_group[0].r_type:

                    temporary_group.append(rm_list[u])
                    rm_list.remove(rm_list[u])
                else:
                    u += 1
                if len(rm_list) == 0:
                    break
            groups += 1
            rm_groups[r + 1] = temporary_group
            if len(rm_list) == 0:
                break

    else:
        groups = 1
    con.groups = groups
    # </editor-fold>
    grand_total = 0
    for w in range(groups):
        current = ""

        ### Variables ###
        thisR = rm_groups[w + 1][0]
        adch = thisR.adults + thisR.kids
        count = 0
        room_charge = 0
        group_rooms = len(rm_groups[w + 1])
        con.rooms_in_group.append(group_rooms)
        con.breakfast.append(bool(thisR.breakfast))
        con.jrhm.append(bool(thisR.member))

        current += "\n\n~ ~ Room rate information for " + types_names[thisR.r_type] + " ~ ~"
        if 1 < group_rooms < 10:
            current += "\nNumber of rooms: " + str(group_rooms)
        cdate = datetime(year=int(thisR.year), month=int(thisR.month), day=int(thisR.day))
        current += "\nCheck-in: " + cdate.strftime("%B %d, %Y (%A)").lstrip("0").replace(" 0", " ") + ", 15:00"
        codate = cdate + timedelta(days=len(thisR.rank))
        cnights = len(thisR.rank)
        con.nights.append(cnights)
        con.check_in_date.append(cdate)
        con.check_out_date.append(codate)
        con.room_type.append(thisR.r_type)
        if thisR.member:
            current += "\nCheck-out: " + codate.strftime("%B %d, %Y (%A)").lstrip("0").replace(" 0", " ") + \
                       ", 12:00      (Staying for " + str(cnights) + " nigth(s))"
        else:
            current += "\nCheck-out: " + codate.strftime("%B %d, %Y (%A)").lstrip("0").replace(" 0", " ") + \
                       ", 11:00      (Staying for " + str(cnights) + " nigth(s))"
        if thisR.kids > 0:
            if thisR.babies > 0:
                people = str((thisR.kids + thisR.babies + thisR.adults)) + " (" + str(thisR.adults) + \
                         " adults (or children above 13), " + str(thisR.kids) + " children 7~12, " + \
                         str(thisR.babies) + " children below 6)"
            else:
                people = str((thisR.kids + thisR.babies + thisR.adults)) + " (" + str(thisR.adults) + \
                         " adults (or children above 13), " + str(thisR.kids) + " children 7~12)"
        elif (thisR.kids + thisR.babies + thisR.adults) == 0:
            people = "1 person"
        elif thisR.babies > 0:
            people = str((thisR.kids + thisR.babies + thisR.adults)) + " (" + str(thisR.adults) + \
                     " adults (or children above 13), " + str(thisR.babies) + " children below 6)"
        else:
            people = str((thisR.kids + thisR.babies + thisR.adults)) + " (adults or children above 13)"
        if group_rooms > 1:
            current += "\nNumber of person(s) per room: " + people.replace("1 children", "1 child")
        else:
            current += "\nNumber of person(s): " + people.replace("1 children", "1 child").replace(
                "1 adults (or children above 13)", "1 adult")
        if thisR.breakfast:
            current += "\nMeals: Breakfast included.\n"
        else:
            current += "\nMeals: Without meals.\n"
        # Add guests names if multiple rooms in the group.
        if group_rooms > 1:
            for room in rm_groups[w + 1]:
                xx = assign_guests(room.name)
                if xx != "":
                    current += "\n Guest(s) in " + room.name + xx
        # Add guests names if only one room in the group.
        else:
            for room in rm_groups[w + 1]:
                current += assign_guests(room.name)

        ### Charge ###
        for xday in thisR.rank:

            xdate = cdate + timedelta(days=count)
            count += 1
            if xday in ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"):
                if adch == 1:
                    xrate = RATY.find(thisR.r_type + " " + xday)
                elif adch == 3:
                    xrate = RATY.find("3TD " + xday)
                elif adch == 2:
                    xrate = RATY.find((thisR.r_type).replace("N", "2") + " " + xday)
                charge = RATY[xrate + 8:xrate + 14]
            else:
                xlist = ["M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
                charge = special_rates_list[xlist.index(xday)].get()

            room_charge = room_charge + int(charge)

            current += "\n" + str(xdate.strftime("%B %d")) + " : " + charge + " JPY"
            con.dates.append(str(xdate.strftime("%B %d")))
            con.rates.append(charge)

        if cnights > 1:
            current += "\n" + str(cnights) + " nights : " + str(room_charge) + " JPY"

        if thisR.member:
            current += "\n\nJR Hotel Members discount : 1200 JPY * " + str(cnights) + " nights = " + str(
                1200 * cnights) + " JPY"
            # room_charge = room_charge - (cnights * 600)
            discount = cnights * 1200
        else:
            discount = 0
        if thisR.breakfast:
            adult_TBF = 2750
            child_TBF = 1650
            TBF_total = cnights * (thisR.adults * adult_TBF + thisR.kids * child_TBF)
            room_total = TBF_total - discount + room_charge
            if thisR.kids == 0:
                current += '\nBreakfast: 2750 JPY* ' + str(thisR.adults) + " person(s) * " + str(cnights) \
                           + " night(s) = " + str(TBF_total) + " JPY"
            else:
                current += "\nBreakfast: ( 2750 JPY(adult) * " + str(thisR.adults) + " + 1650 JPY(child) * " \
                           + str(thisR.kids) + " ) * " + str(cnights) + " night(s) = " + str(TBF_total) + " JPY"
            if rooms_number > 1:
                if thisR.member:
                    current += "\nTotal for this room : " + str(room_charge) + " JPY - " + str(discount) + " JPY + " \
                               + str(TBF_total) + " JPY = " + str(room_total) + " JPY\n"
                else:
                    current += "\nTotal for this room : " + str(room_charge) + " JPY + " \
                               + str(TBF_total) + " JPY = " + str(room_total) + " JPY\n"
            else:
                if thisR.member:
                    current += "\nGrand total : " + str(room_charge) + " JPY - " + str(discount) + " JPY + " \
                               + str(TBF_total) + " JPY = " + str(room_total) + " JPY\n" + tax_info
                else:
                    current += "\nGrand total : " + str(room_charge) + " + " \
                               + str(TBF_total) + " JPY = " + str(room_total) + " JPY\n" + tax_info

        else:
            room_total = room_charge - discount
            if rooms_number > 1:
                if thisR.member:
                    current += "\nTotal for this room : " + str(room_charge) + " - " + str(discount) + " = " \
                               + str(room_total) + " JPY\n"
                else:
                    current += "\nTotal for this room : " + str(room_total) + " JPY\n"
            else:
                if thisR.member:
                    current += "\nGrand total : " + str(room_charge) + " JPY - " + str(discount) + " JPY " \
                               + " = " + str(room_total) + " JPY\n" + tax_info
                else:
                    current += "\nGrand total : " + str(room_total) + " JPY\n" + tax_info

        if group_rooms > 1:
            current += "\n" + str(group_rooms) + " rooms : " + str(group_rooms) + " * " + str(
                room_total) + " JPY = " + str((room_total * group_rooms)) + " JPY\n"

        grand_total += (room_total * group_rooms)
        con.total = grand_total

        # Add thousand's separator for prices.
        current = current.replace("0  ", "0 ")
        current = re.sub('(\d)(\d{3}\sJPY)', '\\1,\\2', current)
        current = re.sub('(\d)(\d{3},)', '\\1,\\2', current)

        all_details[str(w + 1)] = current

    if groups > 1:
        total = "\nGrand total : " + str(grand_total) + " JPY"
        total = total.replace("0  ", "0 ")
        total = re.sub('(\d)(\d{3}\sJPY)', '\\1,\\2', total)
        total = re.sub('(\d)(\d{3},)', '\\1,\\2', total)
        total = re.sub('(\d)(\d{3},)', '\\1,\\2', total)
    else:
        total = ""

    T.delete('1.0', END)
    T.insert(END,
             dear + thank_you + main_description + all_details["1"] + all_details["2"] + all_details["3"] + all_details[
                 "4"] + all_details["5"] + all_details["6"] + all_details["7"] + all_details["8"] + total + show_info())

    komunikat.delete('1.0', END)
    komunikat.insert(END, "生成済")


def save(name):
    if e_representant.get() == "":
        messagebox.showerror("Error", "セーブする為に予約者を記入ください。")
    else:
        change_room()
        the_nr = res_number.get()
        C_IN = str(Room1.month) + "／" + str(Room1.day) + "~" + str(len(Room1.rank)) + "N_#"
        R_NUM = str(res_number.get())
        if R_NUM == "1000":
            R_NUM = ""
        elif int(R_NUM) > 100000000:
            R_NUM = str(int(R_NUM) - 100000000)
        with open('saves/' + (str(name) + "_" + C_IN + R_NUM + '.csv'), 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=',')
            for room in the_rooms:
                writer.writerow([(room.name, "year"), room.year])
                writer.writerow([(room.name, "month"), room.month])
                writer.writerow([(room.name, "day"), room.day])
                writer.writerow([(room.name, "adults"), room.adults])
                writer.writerow([(room.name, "kids"), room.kids])
                writer.writerow([(room.name, "babies"), room.babies])
                writer.writerow([(room.name, "breakfast"), room.breakfast])
                writer.writerow([(room.name, "member"), room.member])
                writer.writerow([(room.name, "rank"), room.rank])
                writer.writerow([(room.name, "r_type"), room.r_type])
                writer.writerow([(room.name, "name"), room.name])
            writer.writerow(["representant_name", e_representant.get()])
            writer.writerow(["representant_sex", v_sex_list[0].get()])
            writer.writerow(["res_number", res_number.get()])
            writer.writerow(["guest_number", guest_number])
            for count, guest in enumerate(e_guest_list, 1):
                writer.writerow([("Guest_name ", count), guest.get()])
                writer.writerow([("Guest_sex ", count), v_sex_list[count].get()])
                writer.writerow([("Guest_room ", count), guest_rooms_list[count - 1].get()])
        komunikat.delete('1.0', END)
        komunikat.insert(END, "セーブ済")


###############################################################################################


###############################################################################################

# <editor-fold desc="Bottom">
##### BOTTOM BUTTONS #####
frame45 = ttk.Frame(frame2)
frame45.pack()
frame4 = ttk.Frame(frame45)
frame4.grid(row=2, column=1)

nohej = """Dear Ms./Mr. \n\nThank you for taking interest in THE BLOSSOM HIBIYA.
\nBelow are the detailed rates for dates you have sent inquiry for:\n\n"""

narazie = """\n\nIf you would like to make a reservation with above rates or have any questions,
please do not hesitate to write to us.
Sincerely,\n"""

# Adding the button for manipulating the main text

komunikat = Text(frame4, width=20, height=1)
komunikat.config(font=('arial', 14, "bold"), fg="dark green", bg="yellow")
komunikat.pack(side=LEFT)

#ttk.Button(frame4, text='計算', command=lambda: check_errors(), width=4).pack(side=LEFT)

#ttk.Button(frame4, text='予約証明書', command=lambda: create_excel(), width=4).pack(side=LEFT)

ttk.Button(frame4, text='生成', command=lambda: check_errors(), width=4).pack(side=LEFT)

ttk.Button(frame4, text='セーブ', command=lambda: save(e_representant.get()), width=6).pack(side=LEFT)


def sajonara():
    komunikat.delete('1.0', END)
    T.insert(END, narazie)
    komunikat.insert(END, "結び追加")


ttk.Button(frame4, text='結び', command=sajonara, width=4).pack(side=LEFT)


def kopiuj():
    komunikat.delete('1.0', END)
    pyperclip.copy(T.get('1.0', END))
    komunikat.insert(END, "内容コピー")


ttk.Button(frame4, text='コピー', command=kopiuj, width=5).pack(side=LEFT)


def usun():
    T.delete('1.0', END)
    komunikat.delete('1.0', END)
    komunikat.insert(END, "内容削除済")


ttk.Button(frame4, text='削除', command=usun, width=4).pack(side=LEFT)


def reset():
    while guest_number > 0:
        remove_guest()
    while rooms_number > 1:
        remove_room()
    global Room1, Room2, Room3, Room4, Room5, Room6, Room7, Room8, the_rooms
    the_rooms = []
    Room1 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 1")
    Room2 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 2")
    Room3 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 3")
    Room4 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 4")
    Room5 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 5")
    Room6 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 6")
    Room7 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 7")
    Room8 = Room(2020, 2, 13, 2, 0, 0, False, False, "", "NDY", "Room 8")
    checkyear.delete(0, END)
    checkmonth.delete(0, END)
    checkday.delete(0, END)
    checkyear.insert(0, today.year)
    checkmonth.insert(0, today.month)
    checkday.insert(0, today.day)
    e_ranks.delete(0, END)
    v_adult.set(1)
    v_rtype.set("NTY")
    v_children.set(0)
    v_baby.set(0)
    v_jrhm.set(0)
    v_language.set(1)
    v_reserv.set(0)
    v_tbf.set(0)
    e_representant.delete(0, END)

    komunikat.delete('1.0', END)
    komunikat.insert(END, "リセット済")


# Creating a free memo for NEHOPS
# def fmemo():
#     if gbaby.get() == 0:
#         soine = ""
#     else:
#         soine = "\n 添い寝 " + str(gbaby.get()) + "名"
#     today = date.today()
#     d1 = today.strftime("%m/%d")
#     d1.replace("0", "")
#     free = d1 + " ﾒｰﾙ BY \n   料金案内ｱﾘ\n " + rtype.get() + " " + str(checkmonth.get()) + "/" + str(
#         checkday.get()) + "~" + str(len(e1.get())) + """N
# \n   ﾗﾝｸ: """ + e1.get() + "\n   " + str(v.get() + 1 + gchildren.get()) + "名" + str(soine)
#     pyperclip.copy(free)
#     komunikat.delete('1.0', END)
#     komunikat.insert(END, "ﾌﾘｰﾒﾓ作成、ｺﾋﾟｰ済")


ttk.Button(frame4, text='Reset', command=lambda: reset(), width=5).pack(side=LEFT)
# </editor-fold>
add_room()

ttk.Label(text="made by Bartosz Lulka", font=('Helvetica', 7)).pack(side=RIGHT)

run = True
root.mainloop()
