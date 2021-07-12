import webbrowser
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image   #FOR JPG image
import datetime as dt           #date time module
from tkcalendar import *            #calender module
from datetime import datetime as t
from tkinter import messagebox as mb     #for message box
import pymysql




class IRCTC:            #class for IRCTC

    def __init__(self,R):
        self.R=R
        R.title('IRCTC Next Generation eTicketing System')
        height=self.R.winfo_screenheight()
        width=self.R.winfo_screenwidth()
        R.geometry('350x250')
        self.R.maxsize(width = 1366,height = 768)
        self.R.minsize(width = 1280,height = 700)
        self.message_box = mb.showinfo('Alert','''Hon'ble Prime Minister message on "Public Health Response to COVID-19: Campaign for COVID-\n\n Get your favourite food at your train seat through e-Catering available at selected stations.\n\n COVID 19 Alert:\n\n Information on Covid 19 Vaccination Programme\n\n All passengers are hereby informed that downloading of Aarogya Setu App on their mobile phone, that they are carrying along, is advisable.\n\n All Passenger to kindly note that on arrival at their destination, the traveling passengers will have to adhere to such health protocols as are prescribed by the destination State/UT. Click Here to see state wise advisory on Arrival(As available). For other states, State Govt websites may be visited to ascertain the same.\n\n Though various State Governments' Advisories have been provided on IRCTC Website, Still Users are advised to surf Destination State Government URL/ Website for latest instructions on Covid-19 pandemic and Covid appropriate behaviour.\n\n Catering Service is not available and catering charges not included in the fare.\n\n No blanket and linen shall be provided in the train.\n''')
        self.bar = Scrollbar(self.R)
        self.bar.pack( side = RIGHT, fill = Y )
        self.img=ImageTk.PhotoImage(Image.open('C:\Python38\mariana-proenca-5o3ODxRQCfI-unsplash.jpg'))
        self.pl=Label(self.R,image=self.img)
        self.pl.place(x=0,y=155,width=1365,height=549)
        self.lbl=Label(R,text='INDIAN RAILWAYS',relief='groove',borderwidth=3.5,font=('times new roman',30,'bold'),fg='white',bg='blue')
        self.lbl.place(x=900,y=360,anchor=NW)
        self.logo_1=PhotoImage(file='C:\Python38\secondry-logo.png')
        self.lbl1=Label(R,image=self.logo_1)
        self.lbl1.place(x=0,y=0)
        self.logo_2=PhotoImage(file='C:\Python38\logo-irctc-removebg-preview.png')
        self.lbl2=Label(R,image=self.logo_2)
        self.lbl2.place(relx=1,x=40,y=-1,anchor=NE)
        
        #Button Creation
        
        self.login=Button(self.R,text='Login',width=7,height=1,bg='navy blue',fg='white',command=self.login,cursor='hand2')
        self.login.place(x=470,y=35)
        self.Reg=Button(self.R,text='Register',width=7,height=1,cursor='hand2')
        self.Reg.place(x=550,y=35)
        self.Age=Button(self.R,text='AgentLogin',width=9,height=1,command=self.agent,cursor='hand2')
        self.Age.place(x=630,y=35)
        self.us=Button(self.R,text='ContactUs',width=8,height=1,command=self.contact,cursor='hand2')
        self.us.place(x=720,y=35)
        self.ask=Button(self.R,text='AskDiksha',width=9,height=1,cursor='hand2')
        self.ask.place(x=800,y=35)
        self.date = Label(self.R, text=f"{dt.datetime.now():%d - %b - %Y [%H : %M : %S]}", fg="black",width=20,height=1)
        self.date.place(x=890,y=37)
        self.ask=Button(self.R,text='IRCTC EXCLUSIVE',font=('Times new roman',10,'bold'),width=17,height=1,bg='navy blue',fg='white',cursor='hand2')
        self.ask.place(x=300,y=80)
        self.ask=Button(self.R,text='Trains',width=6,height=1,cursor='hand2')
        self.ask.place(x=450,y=80)
        self.ask=Button(self.R,text='Buses',width=6,height=1,cursor='hand2')
        self.ask.place(x=520,y=80)
        self.ask=Button(self.R,text='Flight',width=6,height=1,cursor='hand2')
        self.ask.place(x=590,y=80)
        self.ask=Button(self.R,text='Hotels',width=6,height=1,cursor='hand2')
        self.ask.place(x=660,y=80)
        self.ask=Button(self.R,text='Holiday',width=6,height=1,cursor='hand2')
        self.ask.place(x=730,y=80)
        self.ask=Button(self.R,text='Loyalty',width=6,height=1,cursor='hand2')
        self.ask.place(x=800,y=80)
        self.ask=Button(self.R,text='Meals',width=6,height=1,cursor='hand2')
        self.ask.place(x=870,y=80)
        self.ask=Button(self.R,text='Promotions',width=9,height=1,cursor='hand2')
        self.ask.place(x=935,y=80)
        self.ask=Button(self.R,text='PREMIER PARTNER',font=('Times new roman',10,'bold'),width=17,height=1,bg='navy blue',fg='white',cursor='hand2')
        self.ask.place(x=1030,y=80)
        self.lbl4=Label(self.R,text='PNR   STATUS',relief='raised',borderwidth=3,font=('Arial',15,'bold'),bg='navy blue',fg='white')
        self.lbl4.place(x=height/4,y=300)
        self.lbl5=Label(self.R,text='BOOK TICKET',relief='raised',borderwidth=4,font=('times new roman',18,'bold'),fg='navy blue')
        self.lbl5.place(x=height/2.25,y=350)
        
        #Entry widgets
        
        self.e3=Entry(self.R)
        self.e3.place(x=height/4.7,y=400,width=200,height=30)
        self.f=Label(self.R,text='FROM',fg='white',font=('times new roman',10,'bold'),relief='raised',bg='blue')
        self.f.place(x=height/4.7,y=370)
        self.e4=Entry(self.R)
        self.e4.place(x=height/4.7,y=480,width=200,height=30)
        self.t=Label(self.R,text='TO',font=('times new roman',10,'bold'),fg='white',relief='raised',bg='blue')
        self.t.place(x=height/4.7,y=450)
        self.g=Label(self.R,text='General',font=('times new roman',10,'bold'),fg='white',relief='raised',bg='blue')
        self.g.place(x=height/4.7,y=530)

        #Combobox
        
        self.e5=ttk.Combobox(self.R)
        self.e5['values']=('GENERAL','LADIES','LOWER BIRTH/SR.CITIZEN','DIVYANG','TATKAL','PREMIUM TATKAL')
        self.e5['state'] = 'readonly'
        self.e5.current(0)
        self.e5.config(font=('Arial',10,'bold'))
        self.e5.place(x=height/4.7,y=560,width=200,height=30)
        self.d=Label(self.R,text='MM/DD/YYYY',font=('times new roman',10,'bold'),fg='white',relief='raised',bg='blue')
        self.d.place(x=height/1.15,y=420)
        self.date=DateEntry(self.R,width=20,background='blue',foreground='black',font=('Arial',12,'bold'))
        self.date.place(x=height/1.3,y=450)
        
        #Combobox 1
        
        self.e6=ttk.Combobox(self.R)
        self.e6['values']=('All Classes','Exec.Chair Car(EC)','AC 2 Tier(2A)','First Class(FC)','AC 3 Tier(3A)','AC 3 Economy','AC Chair Car(CC)','Sleeper(SL)','Second Sitting(2S)')
        self.e6['state'] = 'readonly'
        self.e6.current(0)
        self.e6.config(font=('Arial',10,'bold'))
        self.e6.place(x=height/1.3,y=520,width=200,height=30)                
        self.lbl4=Label(self.R,text='CHARTS / VACCANCY',relief='raised',borderwidth=3,font=('Arial',15,'bold'),bg='navy blue',fg='white')
        self.lbl4.place(x=height/1.5,y=300)
        
        
        #Check Box
        
        self.chk_state=BooleanVar()
        self.chk_state.set(True)
        self.chk_state1=BooleanVar()
        self.chk_state1.set(True)
        self.chk_state2=BooleanVar()
        self.chk_state2.set(True)
        self.chk_state3=BooleanVar()
        self.chk_state3.set(True)
        self.chk1=Checkbutton(self.R,text='Divyaag Concession',bg='white',relief='raised',var=self.chk_state)
        self.chk1.place(x=height/4.7,y=610)
        self.chk2=Checkbutton(self.R,text='Flexibile with Date',bg='white',relief='raised',var=self.chk_state1)
        self.chk2.place(x=height/2.2,y=610)
        self.chk3=Checkbutton(self.R,text='Train with Available Berth',bg='white',relief='raised',var=self.chk_state2)
        self.chk3.place(x=height/4.7,y=650)
        self.chk4=Checkbutton(self.R,text='Railway pass connection',bg='white',relief='raised',var=self.chk_state3)
        self.chk4.place(x=height/2.2,y=650)
        #Search button
        self.search=Button(self.R,text='Search',width=9,height=1,relief='groove',bg='blue',fg='white',cursor='hand2',command=self.get)
        self.search.place(x=height/1.2,y=650)

# Get value from user
    
    def get(self):
        From=str(self.e3.get())
        To=str(self.e4.get())
        H=str(self.e5.get())
        I=str(self.e6.get())
        C1=str(self.chk_state.get())
        C2=str(self.chk_state1.get())
        C3=str(self.chk_state2.get())
        C4=str(self.chk_state3.get())
        D=str(self.date.get())
            
      
        #print(height)
        #print(width)
        
        #Connect pymysql DB
        
        db=pymysql.connect(host='localhost',user='root',passwd='',db='irctc')
        cur=db.cursor()
        cur.execute("insert into railways values ('"+ From +"','"+ To +"','"+ H +"','"+ D +"','"+ I +"',"+ C1 +","+ C2 +","+ C3 +","+ C4 +")")
        cur.execute('select * from railways')
        data=cur.fetchall()
        cur.execute('commit')
        db.close()
        
        
    # Login info   
    def login(self):
        self.parent=Tk()
        self.parent.geometry('400x350')
        self.parent.maxsize(width = 350,height = 250)
        self.parent.minsize(width = 350,height = 250)
        self.parent.title('Creating New Credentials')
        self.e1=Entry(self.parent)
        self.e1.pack(ipadx=20,ipady=5)
        self.lbl3=Label(self.parent,text='USER NAME',font=('Arial',10,'bold'))
        self.lbl3.place(x=3,y=2)
        self.e2=Entry(self.parent,show='*')
        self.e2.pack(padx=4,pady=15,ipadx=20,ipady=5)
        self.lbl3=Label(self.parent,text='PASSWORD',font=('Arial',10,'bold'))
        self.lbl3.place(x=3,y=47)
        self.sub=Button(self.parent,text='Submit',relief='raised',borderwidth=2,height=1,width=15,cursor='hand2',command=self.submit).place(x=170,y=100)
        self.parent.mainloop()

        
#Submit Button


    def submit(self):
        name=str(self.e1.get())
        password=self.e2.get()
        print('UserName : ' + name)
        print('PassWord : ' + password)


    def agent(self):
        self.win=Tk()
        self.win.title('Redirecting...')
        self.win.maxsize(width = 215,height = 95)
        self.win.minsize(width = 215,height = 95)
        self.btn6=Button(self.win,text='Agent Login with OTP \n\n DC  LOGIN',font=('bookman',15,'bold'),fg='blue',cursor='hand2')
        self.btn6.pack()
        
    # Contact info
    def contact(self):
        msg_b=mb.showinfo('You may contact us','Customer Care Numbers : 0755-6610661, 0755-4090600 (Language: Hindi and English)..\n\n For Railway tickets booked through IRCTC\n General Information\n I-tickets/e-tickets : ''care@irctc.co.in''\n For Cancellation E-tickets : etickets@irctc.co.in\n For IRCTC iMudra Prepaid Wallet & Card : imudracare@irctc.co.in\n\n For IRCTC SBI Card users who do not receive the card within 01 month from the date of application kindly call on the Railway SBI Card Helpline nos. at 0124-39021212 or 18001801295 (if calling from BSNL/MTNL line) or send email to customercare@sbicard.com. For other queries on your IRCTC SBI card account, kindly email at loyaltyprogram@irctc.co.in\n\n Registered Office / Corporate Office\n Indian Railway Catering and Tourism Corporation Ltd.,\n B-148, 11th Floor, Statesman House,\n Barakhamba Road, New Delhi 110001..')


def SUBMIT():
    #e1.delete(0,END)
    use=str(e1.get())
    #e1.insert(0,use)
    paw=str(e2.get())
    #e2.insert(0,paw)
    #db1=pymysql.connect(host='localhost',user='root',passwd='',db='irctc')
    #cur1=db1.cursor()
    #cur1.execute("insert into Login_Info values ('"+ use +"','"+ paw +"')")
    #cur1.execute('commit')
    #db1.close()    
    
    #Checking Username & Password
    
    if (use=='VENGATESH S' and paw=='12345'):
        root=Toplevel()
        my=IRCTC(root)
        e1.delete(0,END)
        e2.delete(0,END)
        #window.quit()
        root.mainloop()
    else:
        mb.askretrycancel('Invaid Credentials','Please check your username and password!!')
        e1.delete(0,END)
        e2.delete(0,END)

def close():
    win=window.destroy()
        
#Login window
    
window=Tk()
window.title('LOGIN')
window.geometry('400x350')
window.maxsize(width = 350,height = 250)
window.minsize(width = 350,height = 250)
e1=Entry(window)
e1.pack(ipadx=20,ipady=5)
lbl3=Label(window,text='USER NAME',font=('Arial',10,'bold'))
lbl3.place(x=3,y=2)
e2=Entry(window,show='*')
e2.pack(padx=4,pady=15,ipadx=20,ipady=5)
lbl3=Label(window,text='PASSWORD',font=('Arial',10,'bold'))
lbl3.place(x=3,y=47)
sub=Button(window,text='LOGIN',relief='raised',fg='white',bg='blue',borderwidth=2,height=1,width=15,cursor='hand2',command=SUBMIT).place(x=170,y=100)
cls=Button(window,text='Close',relief='raised',fg='white',bg='blue',borderwidth=2,height=1,width=15,cursor='hand2',command=close).place(x=170,y=150)



window.mainloop()



#root=Tk()
#my=IRCTC(root)
#root.mainloop()
