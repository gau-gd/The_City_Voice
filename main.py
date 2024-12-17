from tkinter import *

root=Tk()
##root['background']='light blue'
##root.title("TheCityVoice")
##root.geometry('1000x1000')

frg = Frame(root, relief=RAISED, borderwidth=2)
frg.config(width=1000, height=1000)
frg.pack()
frg['background']='pink'

import mysql.connector

# Database initialization
db_conn=mysql.connector.connect(host='localhost',passwd='root',user='root')
c=db_conn.cursor()
c.execute('Create database if not exists mydb1;')
c.execute('use mydb1;')
db_conn.commit()

c.execute('''Create table if not exists users(
         user_id int primary key,
         name varchar(20) ,
         status varchar(3) ,
         password varchar(15)
         )''')

c.execute('''Create table if not exists complaints(
         complaint_id int primary key,
         content text ,
         user_id int ,
         status varchar(3),
         reply varchar(30)
         );''')
db_conn.commit()


def add_user(values,param='user_id,name,status,password'):
    c.execute('insert into users ({}) values {}'.format(param,tuple(values)))
    db_conn.commit()
    
def add_complaint(values,param='complaint_id,content,user_id,status,reply'):
    c.execute('insert into complaints ({}) values {}'.format(param,tuple(values))) 
    db_conn.commit()
def modify_user(user_id,value,param):
    c.execute('update users set =\'{}\'==\'{}\' where user_id=\'{}\''.format(param,value,user_id))
    db_conn.commit()
    
def modify_complaint(complaint_id,value,param):
    c.execute('update complaints set =\'{}\'==\'{}\' where complaint_id==\'{}\';'.format(param,value,user_id))
    db_conn.commit()
def verify_user(value):#users name,pswd
    c.execute('select count(*) from users where name=\'{}\' and password=\'{}\';'.format(value[0],value[1]))
    data =c.fetchall()
    return data[0][0]


def no_of_users():  
    c.execute('select count(*) from users')
    return c.fetchone()[0]

def no_of_complaints():  
    c.execute('select count(*) from complaints')
    return c.fetchone()[0]
# adding new user
#add_users((no_of_users()+1,..))
#add_complaint((no_of_complaints()+1,..))

#add_user([no_of_users()+1,'1','1','1'])
#add_complaint([no_of_complaints()+1,'1',0,'1',''])



uinfo=[]
issues=[]
username = StringVar()
password = StringVar()
problem = StringVar()
name = StringVar()
uname = StringVar()
pword = StringVar()

def issue():
    global issues
    pm=problem.get()
    issues+=[pm]
    add_complaint([no_of_complaints()+1,pm,data[0],'0',''])
    pdone = Label(frg, text="Thank you\n"+"Your problem has been reported", fg="black", bg="pink",font=("Helvetica",15)).grid(row=11, column=1)
    

    
def status():
    cleartable()
    urprob = Label(frg, text="Here are the problems you reported", fg="black", bg="pink",font=("Helvetica",15)).grid(row=1, column=1)
    c.execute('Select * from complaints where user_id={} order by complaint_id desc'.format(data[0]))
    l = c.fetchall()
    text=[]
    
    for i in l:
        
        text+=[i[1]]

    
    for i, txt in enumerate(text):
        lbl = Label(frg, text=txt, font=('Algerian', 15), bg="pink", fg="white", wraplength=400, justify=LEFT)
        lbl.grid(row=i+2, column=0, columnspan=2, padx=10, pady=10)
    
    
def status():
    cleartable()
    urprob_label = Label(frg, text="Here are the problems you reported", fg="black", bg="pink", font=("Helvetica", 15))
    urprob_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

    c.execute('Select * from complaints where user_id={} order by complaint_id desc'.format(data[0]))
    l = c.fetchall()
    text=[]
    print(l)
    for i in l:
        print(i)
        text+=[i[1]]
    print(text)

    for i, txt in enumerate(text):
        lbl = Label(frg, text=txt, font=('Algerian', 15), bg="pink", fg="white", wraplength=400, justify=LEFT)
        lbl.grid(row=i + 1, column=0, columnspan=2, padx=10, pady=10)

    b2 = Button(frg, text="Back", command=userpage, bg='light blue', font=("Helvetica", 15))
    b2.grid( column=0, columnspan=2, pady=10)

 
    
def inpproblem():
    global problem

    problemLabel = Label(frg, text="Problem", fg="black", bg="pink",font=("Helvetica",15)).grid(row=7, column=1)

    problemEntry = Entry(frg, textvariable=problem).grid(row=8, column=1)

    entry = Button(frg,text="Report", fg="black", bg="pink",font=("Helvetica",15),command=issue).grid(row=10, column=1)

def storeuser():
    global x
    n=name.get()
    u=uname.get()
    p=pword.get()
    #add name, username, password of new user to database:- hariharan

    tq=Label(frg,text='Thank you for submitting your response, you are now a member!',fg="black",bg="pink",font=("Algerian",30))
    tq.grid(row=8,column=3)

    home = Button(frg,text="Go back to login", fg="black", bg="pink",font=("Helvetica",15),command=user).grid(row=9, column=3)



def signup():
  
    global name
    global uname
    global pword
    
    cleartable()
    
    l1= Label(frg, text='Sign Up Here!!', fg="black", bg="pink", font=("Algerian", 30))
    l1.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    nameLabel = Label(frg, text="Name", fg="black", bg="pink",font=("Helvetica",15)).grid(row=3, column=1)
    
    nameEntry = Entry(frg, textvariable=name).grid(row=3, column=2) 

    
    usernameLabel = Label(frg, text="User Name", fg="black", bg="pink",font=("Helvetica",15)).grid(row=4, column=1)
    
    usernameEntry = Entry(frg, textvariable=uname).grid(row=4, column=2)  

    passwordLabel = Label(frg,text="Password", fg="black", bg="pink",font=("Helvetica",15)).grid(row=5, column=1)  
    
    passwordEntry = Entry(frg, textvariable=pword, show='*').grid(row=5, column=2)  

    canv = Button(frg,text="Confirm and submit", fg="black", bg="pink",font=("Helvetica",15),command=storeuser).grid(row=6, column=2)
    

     

def userpage():
    cleartable()
    x = data[1]

    welcome_label = Label(frg, text='Welcome back', x, 'What can we do for you today?', fg="black", bg="pink", font=("Algerian", 30))
    welcome_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    report_problem_button = Button(frg, text="Report new problem", fg="black", bg="pink", font=("Helvetica", 15), command=inpproblem)
    report_problem_button.grid(row=1, column=1, padx=10, pady=10)

    view_status_button = Button(frg, text="View status of your problem", fg="black", bg="pink", font=("Helvetica", 15), command=status)
    view_status_button.grid(row=1, column=2, padx=10, pady=10)



def login():
    #author
    global data
    u=username.get()
    p=password.get()
    uinfo=[u,p]
    
    if verify_user(uinfo) != 0:
        c.execute('select * from users where name=\'{}\' and password=\'{}\';'.format(uinfo[0],uinfo[1]))
        data1=c.fetchall()[0]
        
        global data
        data=data1
        
        userpage()
             
def cleartable():
    for widgets in frg.winfo_children():
           widgets.destroy()

def user():
    cleartable()

    # Authorization
    payment = Label(frg, text="LOGIN", fg="black", bg="pink", font=("Algerian", 25))
    payment.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

    usernameLabel = Label(frg, text="User Name:", fg="black", bg="pink", font=("Helvetica", 15))
    usernameLabel.grid(row=1, column=0, padx=10, pady=10)
    usernameEntry = Entry(frg, textvariable=username, width=30)
    usernameEntry.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

    passwordLabel = Label(frg, text="Password:", fg="black", bg="pink", font=("Helvetica", 15))
    passwordLabel.grid(row=2, column=0, padx=10, pady=10)
    passwordEntry = Entry(frg, textvariable=password, show='*', width=30)
    passwordEntry.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

    entry = Button(frg, text="Enter", fg="black", bg="pink", font=("Helvetica", 15), command=login)
    entry.grid(row=3, column=1, columnspan=2, padx=10, pady=10)

    signupLabel = Label(frg, text='Not a part of the community yet? Sign up here!', fg="black", bg="pink", font=("Helvetica", 12))
    signupLabel.grid(row=4, column=0, columnspan=4, padx=10, pady=10)
    
    signupButton = Button(frg, text="Sign Up", fg="black", bg="pink", font=("Helvetica", 15),command=signup)
    signupButton.grid(row=5, column=1, columnspan=2, padx=10, pady=10)




def Introduction():
    
    lbl = Label(frg, text='A user-friendly app that allows the citizens of Bangalore to raise complaints with concerned authorities such as BESCOM, BBMP, etc.', font=('Algerian', 15), bg="pink", fg="white", wraplength=800, justify=LEFT)
    lbl.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

    lbl = Label(frg, text='The app provides two user login facilities for the official as well as the users themselves.', font=('Algerian', 15), bg="pink", fg="white", wraplength=800, justify=LEFT)
    lbl.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    lbl = Label(frg, text='The problems are given a fixed timeline to be rectified.', font=('Algerian', 15), bg="pink", fg="white", wraplength=800, justify=LEFT)
    lbl.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    lbl = Label(frg, text='If it is not satisfied within the given timeline, necessary action is provided to the user to take against the officials.', font=('Algerian', 15), bg="pink", fg="white", wraplength=800, justify=LEFT)
    lbl.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

    lbl = Label(frg, text='Since COVID, everything went online. After the return of employees into their busy lives of long commute to EGL or even Indiranagar, road rage went haywire.', font=('Algerian', 15), bg="pink", fg="white", wraplength=800, justify=LEFT)
    lbl.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    lbl = Label(frg, text='Moreover, even the government grew oblivious to the problems on the road. The situation had to be taken with careful consideration to reduce travel to the government offices.', font=('Algerian', 15), bg="pink", fg="white", wraplength=800, justify=LEFT)
    lbl.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

    lbl = Label(frg, text='The app allows users to upload images and share details of incidents such as accidents, road repairs, and other issues. The app then posts the complaints to social media app handles.', font=('Algerian', 15), bg="pink", fg="white", wraplength=800, justify=LEFT)
    lbl.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    lbl = Label(frg, text='The app will use a database that will store user registration, complaint ID, incident relation information such as location, time, etc.', font=('Algerian', 15), bg="pink", fg="white", wraplength=800, justify=LEFT)
    lbl.grid(row=8, column=0, columnspan=2, padx=10, pady=10)

    b2 = Button(frg, text="Open User Login", command=user, bg='light blue', font=("Helvetica", 15))
    b2.grid(row=9 , column=0, columnspan=2, pady=10)


Introduction()



