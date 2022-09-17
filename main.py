from tkinter import *
import os

def restart():
    os.system('shutdown /r /t 1')
def restart_time():
    os.system('shutdown /r /t 20')
def logout():
    os.system('shutdown -1')
def shutdwon():
    os.system('shutdown /s /t 1')


st=Tk()
st.title('ShutDwon App')
st.geometry('500x500')
st.config(bg='Blue')

r_botton=Button(st,text='Restart',font=('Time New Roman',30,'bold'),relief=RAISED,cursor='plus',command=restart)
r_botton.place(x=150,y=60,height=50,width=200)

rt_botton=Button(st,text='Restart Time',font=('Time New Roman',20,'bold'),relief=RAISED,cursor='plus',command=restart_time)
rt_botton.place(x=150,y=170,height=50,width=200)

lg_botton=Button(st,text='Log out',font=('Time New Roman',20,'bold'),relief=RAISED,cursor='plus',command=logout)
lg_botton.place(x=150,y=270,height=50,width=200)

st_botton=Button(st,text='Shutdown',font=('Time New Roman',20,'bold'),relief=RAISED,cursor='plus',command=shutdwon)
st_botton.place(x=150,y=370,height=50,width=200)


st.mainloop()