# ++++++++++++++++++++++++++++++++++
#
# Author: Kaspars
# 
# Version   Date        Info
#   1.0     2019    Initial version
#
# ++++++++++++++++++++++++++++++++++
from tkinter import *
import random
# Paštaisītās iznešanas atsevišķos moduļos ar importēšanu
from sveicienaTeksts import hello, words, alfabet

# Loga izveidošana
root = Tk()
# Nosakums logam
root.title("Karātavas")
canvas1 = Canvas(root, width=800, height=800)
canvas2 = Canvas(root)
root.minsize(800, 800)
root.resizable(False, False)
canvas1.pack()


# Rūtiņu zīmēšana 33 X 27
def but():
    y = 200
    while y < 799:
        x = 200
        while x < 799:
            canvas1.create_rectangle(x, y, x + 33, y + 27, fill="#ffffff", outline='#0A49E4')
            x = x + 33
        y = y + 27


def arr(*args):  # Tā kā nav zināms cik daudz argumentu nodos funkcijai tad lieto *args

    but()  # Secīgi jāizsauc, lai  sākumā ir  pamats, vēlāk uz tā ir saturs.
    # Lai izvēlētos kādu no gadījuma vārdiem, tad izsauc metodi random.choice un iegūto vērtību piešķir mainīgajam word
    word = random.choice(words)
    wo = word[1:-1]  # wo - vārda daļa (strings) ar burtiem, kuri netiks sākotnēji grafiski attēloti
    wor = []  # wor - neatspoguļojamo burtu saraksts(list)
    for i in wo:
        wor.append(i)
    pos_x = 502  # pos_x - x koordināta kur tiks izvadīts grafiski elements
    canvas1.create_text(502, 238, text=word[0], fill='#3203AE', font=('Helvetica', '16', 'bold'))  # Pirmā burta
    # izvadīšana
    for i in range(len(wo)):  # Pārējo burtu aizstāšana ar apakšstrīpām
        pos_x = pos_x + 35
        canvas1.create_text(pos_x, 238, text='_', fill='#3203AE', font=('Helvetica', '16', 'bold'))
    canvas1.create_text(pos_x + 35, 238, text=word[-1], fill='#3203AE', font=('Helvetica', '16', 'bold'))  # Beidzamā
    # burta izvadīšana
    # Minamo burtu saraksta izveidošana, kuru var aizvietot ar atminētiem burtiem.
    list1 = []
    for i in range(len(wo)):
        if i == len(wo):
            break
        list1.append(i)
    er = []  # Kļūdaini vadīto simbolu saraksts
    win = []  # Atminēto burtu saraksts
    print(word)

    # Funkcija, kura pēc indeksa nosaka kāds burts no saraksta ir izvēlēts
    def a(v):
        ind_alf = alfabet.index(v)
        key = alfabet[ind_alf]
        # Ja burts tiek atminēts un tā atrašanās vieta noteikta, tad tiek aizvietota sarakstā list1 attiecīgā vērtība
        if v in wor:
            win.append(v)
            ind2 = wor.index(v)
            ind = wor.index(v)
            b2 = list1[ind]
            wor[ind] = 1

            # Funkcija, kura nosaka izvadāmās vērtības atrašanās vietu pēc x un y koordinātēm:
            def koord():
                if b2 == 0:
                    x2 = 537
                if b2 == 1:
                    print(b2)
                    x2 = 572
                if b2 == 2:
                    print(b2)
                    x2 = 607
                if b2 == 3:
                    print(b2)
                    x2 = 642
                if b2 == 4:
                    print(b2)
                    x2 = 677
                if b2 == 5:
                    print(b2)
                    x2 = 712
                if b2 == 6:
                    print(b2)
                    x2 = 747
                return x2

            x2 = koord()  # Tā kā mainās tikai vārda x korrdinātes, tad no funkcijas arī tikai to izgūstam

            canvas1.create_text(x2, 238, text=wo[ind], fill='#3203AE', font=('Helvetica', '16',))
            btn[key]['bg'] = 'green'
            if v not in wor:
                btn[key]['state'] = ['disabled']

            if len(win) == len(wo):
                for i in alfabet:
                    btn[i]['state'] = ['disabled']
                canvas1.create_text(100, 600, text="Uzvara", fill='#3203AE', font=('Helvetica', '20',))

        else:  # Ja nav šāda burta vārdā, tad:
            er.append(v)
            if len(er) == 1:
                galva()
            elif len(er) == 2:
                bodijs()
            elif len(er) == 3:
                rokaLaba()
            elif len(er) == 4:
                rokaKreisa()
            elif len(er) == 5:
                kajaLaba()
            elif len(er) == 6:
                death()
            root.update()
            btn[key]['bg'] = 'red'
            btn[key]['state'] = 'disabled'

    btn = {}

    # Pašu izvēles burtu pogas uz kurām var kliķšķināt ar peli
    def gen(u, x, y):  # Vērtības funkcijā: pareizi/nepareizi, x un y koordinātes burtam
        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))

    x = 500
    y = 282
    for i in alfabet[0:8]:
        gen(i, x, y)
        x += 33
    tabula = 1
    while tabula <= 4:
        x = 500
        y = 282 + 27 * tabula
        for i in alfabet[0 + 8 * tabula:8 + 8 * tabula]:
            gen(i, x, y)
            x += 33
        tabula += 1

    def galva():
        canvas1.create_oval(90, 400, 160, 490, width=4, fill='#fff')

    def bodijs():
        canvas1.create_oval(115, 490, 135, 650, width=4, fill='#fff')

    def rokaLaba():
        canvas1.create_oval(130, 500, 200, 515, width=4, fill='#fff')

    def rokaKreisa():
        canvas1.create_oval(120, 500, 50, 515, width=4, fill='#fff')

    def kajaLaba():
        canvas1.create_oval(126, 645, 136, 745, width=4, fill='#fff')

    def death():
        canvas1.create_oval(124, 645, 114, 745, width=4, fill='#fff')
        canvas1.create_text(100, 760, text="Pakārts!", fill='#3203AE', font=('Helvetica', '20',))
        for i in alfabet:
            btn[i]['state'] = ['disabled']


canvas1.create_text(360, 165, text=hello, fill='#800094', font=('Helvetica', '14'))
# Poga, kura palaiž funkciju arr()  - pati spēle
btn01 = Button(root, text='Sākt spēli!', width=10, height='2', command=lambda: arr(words, alfabet))
btn01.place(x=100, y=340)
btn01["bg"] = '#0AE40D'

root.mainloop()
