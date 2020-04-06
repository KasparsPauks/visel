# ++++++++++++++++++++++++++++++++++
#
# Author: Kaspars
# 
# Version   Date        Info
#   1.0     2019    Initial version
#
# ++++++++++++++++++++++++++++++++++
"""
Fiksēts vārdu garums 8-i simboli
Darbi:
I  Importēt tkinter bibliotēku darbam ar grafiku:
    # from tkinter import * # nebūtu korekti
    import tkinter as tk
II Importēt biblitēkas nepieciēšamās darbam:
    import random - lai varētu atlasīt gadījuma vārdu no saraksta
III Palaist pamata programmas logu:
        root =Tk()
1. Izveidot logu, kurā palaist spēli:
        root.title("Karātavas")  # Nosakums logam
        canvas = Canvas(root, width = 800, height=800)
        canvas.pack()
        root.mainloop()  # Galvenā loga izmēri
2. Uzīmēt fonu ar rūtiņām:
        funkcija but()
3. Sasveicināties ar spēlētāju un izskaidrot spēlēs noteikumus:
        hello = ''''....'''
        canvas.create_text(310, 240, text=hello, fill= '#800094', font=('Helvetica', '14'))
        btn01 = Button(root, text='Sākt spēli!', width=10, height='2')
        btn01.place(x=150, y=542)
        btn01["bg"] = '#0AE40D'
4. Sastādīt vārdu sarasktu ko minēt:
        words = ['karātavas',...]
5. Katrā minēšanas gadījumā izvadīt vārda pirmo un pēdējo burtu uz ekrāna, pārējos aizstāt ar _:
            for a in word:
                a0 = canvas.create_text(282, 40, text=word[0], fill='#3203AE', font=('Helvetica', '16', 'bold'))
                a1 = canvas.create_text(315, 40, text='_', fill='#3203AE', font=('Helvetica', '16', 'bold'))
                ....
                a7 = canvas.create_text(510, 40, text=word[-1], fill='#3203AE', font=('Helvetica', '16', 'bold'))
                # if wor_len_x == 0:
                #     canvas.create_text(282, 40, text=word[0], fill='#3203AE', font=('Helvetica', '16', 'bold'))
                #     wor_len_x += 1
                #     pos_x = pos_x + 32
                # if wor_len_x == wor_len:
                #     canvas.create_text(pos_x, 40, text=word[-1], fill='#3203AE', font=('Helvetica', '16', 'bold'))
                # else:
                #     canvas.create_text(pos_x, 40, text='_', fill='#3203AE', font=('Helvetica', '16'))
                #     wor_len_x += 1
                #     pos_x = pos_x + 32
6. Nezināmiem burtiem izveidot vārdnīcu:
        er=[] Nekorektos burtus krāso srakanus un padara neaktīvus
        er.append(v)
7. Pārbaudīt korektumu atbildēm:
8. Karinam klientu pie staba:
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
"""
# herņa