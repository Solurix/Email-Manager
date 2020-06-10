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
    if password.get() == "TheBlossom":
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