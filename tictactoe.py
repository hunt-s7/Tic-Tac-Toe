import tkinter as tk
import sys

HEIGHT=500
WIDTH=500
turn=0
window=tk.Tk()
window.title('TIC-TAC-TOE')

canvas=tk.Canvas(window,height=HEIGHT,width=WIDTH)
canvas.pack()

p1=tk.StringVar()
p2=tk.StringVar()

def w_exit():
    exit()

def win1():
    set_frame=tk.Frame(window,bg='#00688B')
    set_frame.place(relwidth=1,relheight=1)
    frame=tk.Frame(set_frame,bg='#00688B',bd=5)
    frame.place(relx=0.2,rely=0.4,relwidth=0.6,relheight=0.6)
    frame1=tk.Frame(set_frame,bg='#00688B',bd=5)
    frame1.place(relx=0.1,rely=0.1,relwidth=0.8,relheight=0.25)

    label=tk.Label(frame1,text='TIC TAC TOE',font=("Cambria",40),bg='#8DB6CD',fg='#00688B')
    label.place(relwidth=1,relheight=1)

    start=tk.Button(frame,text='START',fg='#8DB6CD',font=("Cambria",30),bg='#00688B',command=win2)
    start.place(relx=0,rely=0,relwidth=1,relheight=1/3)
    abouts=tk.Button(frame,text='ABOUT',font=('Cambria',30),command=about,fg='#8DB6CD',bg='#00688B')
    abouts.place(relx=0,rely=1/3,relwidth=1,relheight=1/3)
    leave=tk.Button(frame,text='QUIT',fg='#8DB6CD',font=("Cambria",30),bg='#00688B',command=w_exit)
    leave.place(relx=0,rely=2/3,relwidth=1,relheight=1/3)

def win2():
    set_frame=tk.Frame(window,bg='#00688B')
    set_frame.place(relwidth=1,relheight=1)

    player1=tk.Label(set_frame,text='PLAYER 1',font=('Cambria',25),bg='#00688B',fg='#8DB6CD')
    player1.place(relx=0.3,rely=0.1,relwidth=0.4,relheight=0.1)
    player2=tk.Label(set_frame,text='PLAYER 2',font=('Cambria',25),bg='#00688B',fg='#8DB6CD')
    player2.place(relx=0.3,rely=0.4,relwidth=0.4,relheight=0.1)

    play1=tk.Entry(set_frame,textvariable=p1,bg='#00688B',fg='#8DB6CD',font=('Cambria',25))
    play1.place(relx=0.3,rely=0.25,relwidth=0.4,relheight=0.1)
    play2=tk.Entry(set_frame,textvariable=p2,bg='#00688B',fg='#8DB6CD',font=('Cambria',25))
    play2.place(relx=0.3,rely=0.55,relwidth=0.4,relheight=0.1)


    ok=tk.Button(set_frame,text='OK',font=('Cambria',25),command=win3,bg='#00688B',fg='#8DB6CD')
    ok.place(relx=0.3,rely=0.7,relwidth=0.4,relheight=0.1)



def about():
    l=tk.Label(window,text='DEVELOPED \nBY\nHUNT\n\n(SATYAM GOEL)\n\nPYTHON 3.7.4',font=(" Cambria",30),bg='#00688B',fg='#8DB6CD')
    l.place(relwidth=1 ,relheight=1)
    startpage=tk.Button(window,text='MAIN MENU',font='Cambria',command=win1,bg='#00688B',fg='#8DB6CD')
    startpage.place(relx=0.6,rely=0.85,relheight=0.1,relwidth=0.3)

def win4():
    
    l=tk.Label(window,text='PLAYER\n1\n WINS',font=(" Cambria",45),bg='#00688B',fg='#8DB6CD')
    l.place(relwidth=1 ,relheight=1)

    retry=tk.Button(window,text='RETRY',font='Cambria',command=win3,bg='#00688B',fg='#8DB6CD')
    retry.place(relx=0.6,rely=0.7,relheight=0.1,relwidth=0.3)
    quits=tk.Button(window,text='QUIT',font='Cambria',command=w_exit,bg='#00688B',fg='#8DB6CD')
    quits.place(relx=0.6,rely=0.85,relheight=0.1,relwidth=0.3)
    startpage=tk.Button(window,text='MAIN MENU',font='Cambria',command=win1,bg='#00688B',fg='#8DB6CD')
    startpage.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.3)
    abouts=tk.Button(window,text='ABOUT',font='Cambria',command=about,bg='#00688B',fg='#8DB6CD')
    abouts.place(relx=0.1,rely=0.85,relheight=0.1,relwidth=0.3)

def win5():

    l=tk.Label(window,text='PLAYER \n2\n WINS',font=(" Cambria",45),bg='#00688B',fg='#8DB6CD')
    l.place(relwidth=1 ,relheight=1)

    retry=tk.Button(window,text='RETRY',font='Cambria',command=win3,bg='#00688B',fg='#8DB6CD')
    retry.place(relx=0.6,rely=0.7,relheight=0.1,relwidth=0.3)
    quits=tk.Button(window,text='QUIT',font='Cambria',command=w_exit,bg='#00688B',fg='#8DB6CD')
    quits.place(relx=0.6,rely=0.85,relheight=0.1,relwidth=0.3)
    startpage=tk.Button(window,text='MAIN MENU',font='Cambria',command=win1,bg='#00688B',fg='#8DB6CD')
    startpage.place(relx=0.1,rely=0.7,relheight=0.1,relwidth=0.3)
    abouts=tk.Button(window,text='ABOUT',font='Cambria',command=about,bg='#00688B',fg='#8DB6CD')
    abouts.place(relx=0.1,rely=0.85,relheight=0.1,relwidth=0.3)

def win3():
    pp1='' + p1.get()
    pp2=''+p2.get()
    pp1=pp1.upper()
    pp2=pp2.upper()
    turn=0


    set_frame=tk.Frame(window,bg='#00688B')
    set_frame.place(relwidth=1,relheight=1)
    frame=tk.Frame(set_frame,bg='#00688B',bd=5)
    frame.place(relx=0.2,rely=0.35,relwidth=0.6,relheight=0.6)
    frame2=tk.Frame(set_frame,bg='#00688B',bd=5)
    frame2.place(relx=0.2,rely=0.13,relwidth=0.6,relheight=0.2)
    frame3=tk.Frame(set_frame,bg='#00688B',bd=5)
    frame3.place(relx=0.05,rely=0.01,relwidth=0.35,relheight=0.1)
    frame4=tk.Frame(set_frame,bg='#00688B',bd=5)
    frame4.place(relx=0.6,rely=0.01,relwidth=0.35,relheight=0.1)

    button_prev=tk.Button(set_frame,text='BACK',font='Cambria',fg='#8DB6CD',bg='#00688B',command=win1)
    button_prev.place(relx=0.05,rely=0.85,relwidth=0.1,relheight=0.1)

    label_p1=tk.Label(frame3,text=pp1,font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
    label_p1.place(relwidth=1,relheight=1)
    label_p2=tk.Label(frame4,text=pp2,font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
    label_p2.place(relwidth=1,relheight=1)
    l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
    l.place(relwidth=1,relheight=1)
    

    def click1():
        global turn
        if(bn1['text']==''):
            if(turn%2==0):
                bn1['text']='X'
                l=tk.Label(frame2,text='PLAYER 2 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            else:
                bn1['text']='O'
                l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            turn+=1
        if(turn==9):
            tie=tk.Label(frame2,text='DRAW',font=(' Cambria',40))
            tie.place(relwidth=1,relheight=1)
            turn=0
        result()

    def click2():
        global turn
        if(bn2['text']==''):
            if(turn%2==0):
                bn2['text']='X'
                l=tk.Label(frame2,text='PLAYER 2 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            else:
                bn2['text']='O'
                l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            turn+=1
        if(turn==9):
            tie=tk.Label(frame2,text='DRAW',font=(' Cambria',40))
            tie.place(relwidth=1,relheight=1)
            turn=0
        result()

    def click3():
        global turn
        if(bn3['text']==''):
            if(turn%2==0):
                bn3['text']='X'
                l=tk.Label(frame2,text='PLAYER 2 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            else:
                bn3['text']='O'
                l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            turn+=1
        if(turn==9):
            tie=tk.Label(frame2,text='DRAW',font=(' Cambria',40))
            tie.place(relwidth=1,relheight=1)
            turn=0
        result()

    def click4():
        global turn
        if(bn4['text']==''):
            if(turn%2==0):
                bn4['text']='X'
                l=tk.Label(frame2,text='PLAYER 2 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            else:
                bn4['text']='O'
                l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            turn+=1
        if(turn==9):
            tie=tk.Label(frame2,text='DRAW',font=(' Cambria',40))
            tie.place(relwidth=1,relheight=1)
            turn=0
        result()

    def click5():
        global turn
        if(bn5['text']==''):
            if(turn%2==0):
                bn5['text']='X'
                l=tk.Label(frame2,text='PLAYER 2 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            else:
                bn5['text']='O'
                l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            turn+=1
        if(turn==9):
            tie=tk.Label(frame2,text='DRAW',font=(' Cambria',40))
            tie.place(relwidth=1,relheight=1)
            turn=0
        result()

    def click6():
        global turn
        if(bn6['text']==''):
            if(turn%2==0):
                bn6['text']='X'
                l=tk.Label(frame2,text='PLAYER 2 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            else:
                bn6['text']='O'
                l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            turn+=1
        if(turn==9):
            tie=tk.Label(frame2,text='DRAW',font=(' Cambria',40))
            tie.place(relwidth=1,relheight=1)
            turn=0
        result()

    def click7():
        global turn
        if(bn7['text']==''):
            if(turn%2==0):
                bn7['text']='X'
                l=tk.Label(frame2,text='PLAYER 2 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            else:
                bn7['text']='O'
                l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            turn+=1
        if(turn==9):
            tie=tk.Label(frame2,text='DRAW',font=(' Cambria',40))
            tie.place(relwidth=1,relheight=1)
            turn=0
        result()

    def click8():
        global turn
        if(bn8['text']==''):
            if(turn%2==0):
                bn8['text']='X'
                l=tk.Label(frame2,text='PLAYER 2 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            else:
                bn8['text']='O'
                l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            turn+=1
        if(turn==9):
            tie=tk.Label(frame2,text='DRAW',font=(' Cambria',40))
            tie.place(relwidth=1,relheight=1)
            turn=0
        result()

    def click9():
        global turn
        if(bn9['text']==''):
            if(turn%2==0):
                bn9['text']='X'
                l=tk.Label(frame2,text='PLAYER 2 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            else:
                bn9['text']='O'
                l=tk.Label(frame2,text='PLAYER 1 TURN',font=(" Cambria",20),bg='#8DB6CD',fg='#00688B')
                l.place(relwidth=1,relheight=1)
            turn+=1
        if(turn==9):
            tie=tk.Label(frame2,text='DRAW',font=(' Cambria',40))
            tie.place(relwidth=1,relheight=1) 
            turn=0
        result()          

    
    def result():
        #1
        global turn
        if(bn1['text']==bn2['text'] and bn1['text']==bn3['text'] and bn1['text']=='X'):
            turn=0
            win4()

        if(bn1['text']==bn2['text'] and bn1['text']==bn3['text'] and bn1['text']=='O'):
            turn=0
            win5()

        #2
        if(bn4['text']==bn5['text'] and bn4['text']==bn6['text'] and bn4['text']=='X'):
            turn=0
            win4()
        if(bn4['text']==bn5['text'] and bn4['text']==bn6['text'] and bn4['text']=='O'):
            turn=0
            win5()
        #3
        if(bn7['text']==bn8['text'] and bn7['text']==bn9['text'] and bn7['text']=='X'):
            turn=0
            win4()
        if(bn7['text']==bn8['text'] and bn7['text']==bn9['text'] and bn7['text']=='O'):
            turn=0
            win5()

        #4
        if(bn1['text']==bn5['text'] and bn1['text']==bn9['text'] and bn1['text']=='X'):
            turn=0
            win4()
        if(bn1['text']==bn5['text'] and bn1['text']==bn9['text'] and bn1['text']=='O'):
            turn=0
            win5()

        #5
        if(bn7['text']==bn5['text'] and bn7['text']==bn3['text'] and bn7['text']=='X'):
            turn=0
            win4()
        if(bn7['text']==bn5['text'] and bn7['text']==bn3['text'] and bn7['text']=='O'):
            turn=0
            win5()

        #6
        if(bn1['text']==bn4['text'] and bn1['text']==bn7['text'] and bn1['text']=='X'):
            turn=0
            win4()
        if(bn1['text']==bn4['text'] and bn1['text']==bn7['text'] and bn1['text']=='O'):
            turn=0
            win5()

        #7
        if(bn2['text']==bn5['text'] and bn2['text']==bn8['text'] and bn2['text']=='X'):
            turn=0
            win4()
        if(bn2['text']==bn5['text'] and bn2['text']==bn8['text'] and bn2['text']=='O'):
            turn=0
            win5()

        #8
        if(bn3['text']==bn6['text'] and bn3['text']==bn9['text'] and bn3['text']=='X'):
            turn=0
            win4()
        if(bn3['text']==bn6['text'] and bn3['text']==bn9['text'] and bn3['text']=='O'):
            turn=0
            win5()
            


    
    
    bn1=tk.Button(frame,text='',fg='#8DB6CD',bg='#00688B',font=(' Cambria',40),command=click1)
    bn1.place(x=0,y=0,relx=0,rely=0,relwidth=1/3,relheight=1/3)
    bn2=tk.Button(frame,text='',fg='#8DB6CD',bg='#00688B',font=(' Cambria',40),command=click2)
    bn2.place(y=0,relx=1/3,rely=0,relwidth=1/3,relheight=1/3)
    bn3=tk.Button(frame,text='',fg='#8DB6CD',bg='#00688B',font=(' Cambria',40),command=click3)
    bn3.place(y=0,relx=2/3,rely=0,relwidth=1/3,relheight=1/3)
    bn4=tk.Button(frame,text='',fg='#8DB6CD',bg='#00688B',font=(' Cambria',40),command=click4)
    bn4.place(relx=0,rely=1/3,relwidth=1/3,relheight=1/3)
    bn5=tk.Button(frame,text='',fg='#8DB6CD',bg='#00688B',font=(' Cambria',40),command=click5)
    bn5.place(relx=1/3,rely=1/3,relwidth=1/3,relheight=1/3)
    bn6=tk.Button(frame,text='',fg='#8DB6CD',bg='#00688B',font=(' Cambria',40),command=click6)
    bn6.place(relx=2/3,rely=1/3,relwidth=1/3,relheight=1/3)
    bn7=tk.Button(frame,text='',fg='#8DB6CD',bg='#00688B',font=(' Cambria',40),command=click7)
    bn7.place(relx=0,rely=2/3,relwidth=1/3,relheight=1/3)
    bn8=tk.Button(frame,text='',fg='#8DB6CD',bg='#00688B',font=(' Cambria',40),command=click8)
    bn8.place(relx=1/3,rely=2/3,relwidth=1/3,relheight=1/3)
    bn9=tk.Button(frame,text='',fg='#8DB6CD',bg='#00688B',font=(' Cambria',40),command=click9)
    bn9.place(relx=2/3,rely=2/3,relwidth=1/3,relheight=1/3)

win1()


window.mainloop()


