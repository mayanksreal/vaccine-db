import tkinter as t
from tkinter import ttk
from tkinter import messagebox
import mysql.connector


def gui():
    window = t.Tk()
    window.geometry('960x540')
    canva = t.Canvas(window,width=960,height=540)
    window.maxsize(960,540)
    window.minsize(960,540)
    window.title('Vaccination')
    window.config(bg='#f0f0ff')
    #E5E8E8
    #tabs
    tabs = ttk.Notebook()

    home_tab = ttk.Frame(tabs)  
    tabs.add(home_tab,text='      Home      ')

    view_tab = ttk.Frame(tabs)
    tabs.add(view_tab,text='   View Records    ')

    add_tab = ttk.Frame(tabs)
    tabs.add(add_tab,text='   Add Record    ')

    update_tab = ttk.Frame(tabs)
    tabs.add(update_tab,text='  Update Record  ')

    delete_tab = ttk.Frame(tabs)
    tabs.add(delete_tab,text=' Delete Record  ')

    tabs.place(x=260,y=0)

    #slate blue box

    def about():
        messagebox.showinfo('About VaxCheck','VaxCheck has been developed by Mayank Sharma. VaxCheck helps keeps a track of vaccination status of your organization')
    def support():
        messagebox.showinfo('Contact Us','Write to us at ......')
    
    sidebox = t.Label(width = 32, height = 30,font='calibri 12',bg='slateBlue',fg='white',highlightthickness=0,bd=0)
    sidebox.place(x=0,y=0)
    about = t.Button(text='About VaxCheck',fg='white',command=about,bg='slateblue',font=('DejaVu Sans Mono',10,'bold'),borderwidth=0,activebackground='slate blue',activeforeground='white')
    about.place(x=10,y=450)
    contact = t.Button(text='Feedback & Support',fg='white',command=support,bg='slateblue',font=('DejaVu Sans Mono',10,'bold'),borderwidth=0,activebackground='slate blue',activeforeground='white')
    contact.place(x=10,y=420)
    version = t.Label(text='VaxCheckv1.0 #GetVaccinated',font=('DejaVu sans mono',10),bg='slateblue',fg='dark grey')
    version.place(x=10,y=510)
    exit_ = t.Button(command=window.destroy,text='Exit VaxCheck',font=('DejaVu sans mono',10,'bold'),bg='slateblue',fg='Tomato',borderwidth=0,activebackground='slate Blue',activeforeground='white')
    exit_.place(x=10,y=480)

    img = t.PhotoImage(file='resources\\tick.png')
    logo_on_top = t.Label(image=img,background='slateblue')
    logo_on_top.place(x=0,y=0)

    name_on_top = t.Label(text='VaxCheck',background='Slateblue',fg='white',height=1,width=10,pady=10)
    name_on_top.config(font=('Arial Rounded MT Bold',18))
    name_on_top.place(x=40,y=-5)

    #main_table
    cols = ('Name','Status','Date','Employee-ID','Recommendation')
    table = ttk.Treeview(view_tab,columns=cols,show='headings',height=24)
    for x in cols:
        table.heading(x,text=x)

    table.column('Name',width=130,anchor='center')
    table.column('Status',width=165,anchor='center')
    table.column('Date',width=100,anchor='center')
    table.column('Employee-ID',width=80,anchor='center')
    table.column('Recommendation',width=218,anchor='center')

    #read
    mydb = mysql.connector.connect(
    host="localhost",
    user="USERNAME", #ex. root
    password="PASSWORD", #ex. pw
    database="vaccine")

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM vaccination ORDER BY EMPLOYEEID ASC")
    myresult = mycursor.fetchall()

    eids = []
    fully_vaccinated = 0
    unvaccinated = 0

    for x in myresult:
        x = list(x)
        eids.append(x[3])
        if x[1] == ('Not Vaccinated' or 'not vaccinated'):
            x.append('Stay At Home')
            unvaccinated+=1
        if x[1] == ('Partially Vaccinated' or 'partially vaccinated'):
            x.append('Come to Work: Wear a Mask')
        if x[1] == ('Fully Vaccinated' or 'fully vaccinated'):
            x.append('Come to Work')
            fully_vaccinated+=1
        table.insert('',t.END,values=x)

    table.pack()
    if len(eids) != 0:
        vaccinated_per = (fully_vaccinated/len(eids))*100 
        unvaccinated_per = (unvaccinated/len(eids))*100
    else:
        vaccinated_per =0
        unvaccinated_per = 0

    vaccinated1 = t.Label(text=f'{round(vaccinated_per,2)}%',bg='slate blue',fg='light grey',font=('Arial Rounded mt bold',24,'bold'))
    vaccinated2 = t.Label(font=('DejaVu sans mono',9,'italic'),text='Employs have been fully vaccinated and can\ncome to work. However it is adviced to carry\nMask, Sanitizer and take other neccessary \nPrecautions. Avoid Contact with co-workers',bg='slateblue',fg='light grey')
    vaccinated1.place(x=10,y=70)
    vaccinated2.place(x=4,y=110)

    #HOME TAB
    welcome_text = t.Label(home_tab,text='Welcome to VaxCheck Desktop',font = ('DejaVu Sans Mono',20),fg='#333')
    welcome_text.place(x=160,y=70)
    welcome_text2 = t.Label(home_tab,text='Use this tutorial to get confortable with VaxCheck',font = ('calibri',12),fg='#333')
    welcome_text2.place(x=180,y=100)

    view_img = t.PhotoImage(file='resources\\view.png')
    add_img = t.PhotoImage(file='resources\\add.png')
    update_img = t.PhotoImage(file='resources\\update.png')
    delete_img = t.PhotoImage(file='resources\\delete.png')

    view_img1 = t.Label(home_tab,image=view_img)
    view_img1.place(x=80,y=180)
    view_txt_head = t.Label(home_tab,text='View Record',font = ('DejaVu Sans Mono',11,'bold'),fg='blue')
    view_txt_head.place(x=65,y=270)
    view_txt = t.Label(home_tab,text='View all the records\nsimulnateously',font = ('DejaVu Sans Mono',11,'italic'),fg='#333')
    view_txt.place(x=50,y=290)

    add_img1 = t.Label(home_tab,image=add_img)
    add_img1.place(x=230,y=200)
    add_txt_head = t.Label(home_tab,text='Add Record',font = ('DejaVu Sans Mono',11,'bold'),fg='blue')
    add_txt_head.place(x=220,y=290)
    add_txt = t.Label(home_tab,text='Make a new\nentry',font = ('DejaVu Sans Mono',11,'italic'),fg='#333')
    add_txt.place(x=220,y=310)


    update_img1 = t.Label(home_tab,image=update_img)
    update_img1.place(x=385,y=200)
    update_txt_head = t.Label(home_tab,text='Update Record',font = ('DejaVu Sans Mono',11,'bold'),fg='blue')
    update_txt_head.place(x=365,y=290)
    update_txt = t.Label(home_tab,text='Overwrite an\nalready existing\nrecord',font = ('DejaVu Sans Mono',11,'italic'),fg='#333')
    update_txt.place(x=370,y=310)


    delete_img1 = t.Label(home_tab,image=delete_img)
    delete_img1.place(x=540,y=180)
    delete_txt_head = t.Label(home_tab,text='Delete Record',font = ('DejaVu Sans Mono',11,'bold'),fg='blue')
    delete_txt_head.place(x=530,y=270)
    delete_txt = t.Label(home_tab,text='Delete a\npre-existing record',font = ('DejaVu Sans Mono',11,'italic'),fg='#333')
    delete_txt.place(x=520,y=290)

    #add_screen
    add_background = t.Label(add_tab,bg='white',height=34,width=99)
    add_background.place(x=0,y=0)
    add_ico_img = t.PhotoImage(file='resources\\add 2.png')
    add_ico = t.Label(add_tab,image = add_ico_img,bg='white')
    add_ico.place(x=190,y=10)
    add_title = t.Label(add_tab,text='Add A New Record',font=('DejaVuSansMono',18),fg='#333',bg='white')
    add_title.place(x=260,y=20)
    vac_img = t.PhotoImage(file='resources\\vacc.png')
    vacc_img = t.Label(add_tab,image=vac_img,bg='white',fg='white',borderwidth=0)
    vacc_img.place(x=270,y=200)

    fg_color = 'black'
    
    fname = t.Label(add_tab,text='First Name',bg='white',fg='#333',font=('DejaVu Sans Mono',11))
    fname.place(x=30,y=110)
    fname_entry_img = t.PhotoImage(file='resources\\label.png')
    fname_entry_bg = t.Label(add_tab,image=fname_entry_img,bg='white')
    fname_entry_bg.place(x=120,y=103)
    fname_entry = t.Entry(add_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=10)
    fname_entry.place(x=145,y=113)

    lname = t.Label(add_tab,text='Last Name',bg='white',fg='#333',font=('DejaVuSansMono',11))
    lname.place(x=30,y=163)
    lname_entry_img = t.PhotoImage(file='resources\\label.png')
    lname_entry_bg = t.Label(add_tab,image=fname_entry_img,bg='white')
    lname_entry_bg.place(x=120,y=155)
    lname_entry = t.Entry(add_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=10)
    lname_entry.place(x=145,y=165)

    eid = t.Label(add_tab,text='Employee-ID',bg='white',fg='#333',font=('DejaVuSansMono',11))
    eid.place(x=30,y=213)
    eid_entry_img = t.PhotoImage(file='resources\\half_label.png')
    eid_entry_bg = t.Label(add_tab,image=eid_entry_img,bg='white')
    eid_entry_bg.place(x=120,y=205)
    eid_entry = t.Entry(add_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=5)
    eid_entry.place(x=140,y=215)

    date = t.Label(add_tab,text='Date of Vaccination',bg='white',fg='#333',font=('DejaVuSansMono',11))
    date.place(x=28,y=275)
    date_entry_img = t.PhotoImage(file='resources\\quarter_label.png')
    date_entry_bg = t.Label(add_tab,image=date_entry_img,bg='white')

#
    date_entry_bg.place(x=180,y=265)
    date_entry = t.Entry(add_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=3)
    date_entry.place(x=197,y=275)
    date_label = t.Label(add_tab,text='(DD)',font=('DejaVuSansMono',9),fg=fg_color,bg='white')
    date_label.place(x=190,y=305)

    month_entry_bg = t.Label(add_tab,image=date_entry_img,bg='white')
#
    month_entry_bg.place(x=250,y=265)
    month_entry = t.Entry(add_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=3)
    month_entry.place(x=267,y=275)
    month_label = t.Label(add_tab,text='(MM)',font=('DejaVuSansMono',9),fg=fg_color,bg='white')
    month_label.place(x=262,y=305)

    year_entry_img = t.PhotoImage(file='resources\\half_label.png')
    year_entry_bg = t.Label(add_tab,image=year_entry_img,bg='white')
#
    year_entry_bg.place(x=320,y=265)
    year_entry = t.Entry(add_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=5)
    year_entry.place(x=340,y=275)
    year_label = t.Label(add_tab,text='(YYYY)',font=('DejaVuSansMono',9),fg=fg_color,bg='white')
    year_label.place(x=340,y=305)

    vac_status = t.Label(add_tab,text = 'Choose Your Vaccination Status',font=('DejaVuSansMono',12),bg='white',fg='#333')
    vac_status.place(x=380,y=85)
    vac_var = t.IntVar()
    unvaccinated = t.Radiobutton(add_tab,bg='white',text='Unvaccinated',var=vac_var,value=1,fg='red',font=('DejaVuSansMono',11))
    shot1 = t.Radiobutton(add_tab,bg='white',text='1st Shot',var=vac_var,value=2,fg='black',font=('DejaVuSansMono',11))
    shot2 = t.Radiobutton(add_tab,bg='white',text='2nd Shot',var=vac_var,value=3,fg='black',font=('DejaVuSansMono',11))
    unvaccinated.place(x=400,y=110)
    shot1.place(x=400,y=140)
    shot2.place(x=400,y=170)

    def add_values():
        vals = []
        fname= fname_entry.get()
        lname= lname_entry.get()
        vals.append(fname+' '+lname)
        status = vac_var.get()
        if status == 1:
            vals.append('Not Vaccinated')
        elif status == 2:
            vals.append('Partially Vaccinated')
        elif status == 3:
            vals.append('Fully Vaccinated')
        try:
            vac_date = int(date_entry.get())
            vac_month = int(month_entry.get())
            vac_year = int(year_entry.get())
            vals.append(str(vac_date)+'-'+str(vac_month)+'-'+str(vac_year))
        except ValueError:
            messagebox.showerror('Error','Please Fill all the Fields')
        eid = int(eid_entry.get())
        vals.append(eid)
        while True:
            if fname=='':
                messagebox.showerror('Error','Please Fill all the Fields')
                break
            elif status==0:
                messagebox.showerror('Error','Please Fill all the Fields')
                break
            elif eid == '':
                messagebox.showerror('Error','Please Fill all the Fields')
                break
            elif vac_date > 31:
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif vac_date < 0:
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif (vac_month > 12):
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif (vac_month < 0):
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            # Optional upper date
            # elif (vac_year > 2030):
            #   messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif (vac_year < 2020):
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif eid in eids:
                messagebox.showerror('Error','Record for Specified Employee-ID already exists')
                break
            else:
                print(vals,'added to database!')
                mcsr = mydb.cursor()
                cmd = 'INSERT INTO vaccination (NAME, STATUS, DATE, EMPLOYEEID) values (%s, %s, %s, %s)'
                mcsr.execute(cmd, vals)
                mydb.commit()
                messagebox.showinfo('Record added!','Record has been added!')
                window.destroy()
                gui()
                break

    #update_tab
    update_background = t.Label(update_tab,bg='white',height=34,width=99)
    update_background.place(x=0,y=0)
    update_ico_img = t.PhotoImage(file='resources\\update 2.png')
    update_ico = t.Label(update_tab,image = update_ico_img,bg='white')
    update_ico.place(x=170,y=10)
    update_title = t.Label(update_tab,text='Update A Current Record',font=('DejaVuSansMono',18),fg='#333',bg='white')
    update_title.place(x=240,y=20)
    vac_img1 = t.PhotoImage(file='resources\\vacc1.png')
    vacc_img1 = t.Label(update_tab,image=vac_img1,bg='white',fg='white',borderwidth=0)
    vacc_img1.place(x=375,y=210)

    fname1 = t.Label(update_tab,text='First Name',bg='white',fg='#333',font=('DejaVu Sans Mono',11))
    fname1.place(x=30,y=150)
    fname_entry_img1 = t.PhotoImage(file='resources\\label.png')
    fname_entry_bg1 = t.Label(update_tab,image=fname_entry_img1,bg='white')
    fname_entry_bg1.place(x=120,y=145)
    fname_entry1 = t.Entry(update_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=10)
    fname_entry1.place(x=145,y=153)

    lname1 = t.Label(update_tab,text='Last Name',bg='white',fg='#333',font=('DejaVuSansMono',11))
    lname1.place(x=30,y=203)
    lname_entry_img1 = t.PhotoImage(file='resources\\label.png')
    lname_entry_bg1 = t.Label(update_tab,image=fname_entry_img1,bg='white')
    lname_entry_bg1.place(x=120,y=195)
    lname_entry1 = t.Entry(update_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=10)
    lname_entry1.place(x=145,y=205)

    eid1 = t.Label(update_tab,text='Employee-ID',bg='white',fg='#333',font=('DejaVuSansMono',11))
    eid1.place(x=30,y=100)
    eid_entry_img1 = t.PhotoImage(file='resources\\half_label.png')
    eid_entry_bg1 = t.Label(update_tab,image=eid_entry_img1,bg='white')
    eid_entry_bg1.place(x=130,y=90)
    eid_entry1 = t.Entry(update_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=5)
    eid_entry1.place(x=150,y=99)

    date1 = t.Label(update_tab,text='Date of Vaccination',bg='white',fg='#333',font=('DejaVuSansMono',11))
    date1.place(x=28,y=275)
    date_entry_img1 = t.PhotoImage(file='resources\\quarter_label.png')
    date_entry_bg1 = t.Label(update_tab,image=date_entry_img1,bg='white')
    date_entry_bg1.place(x=180,y=265)
    date_entry1 = t.Entry(update_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=3)
    date_entry1.place(x=197,y=275)
    date_label1 = t.Label(update_tab,text='(DD)',font=('DejaVuSansMono',9),fg=fg_color,bg='white')
    date_label1.place(x=190,y=305)

    month_entry_bg1 = t.Label(update_tab,image=date_entry_img1,bg='white')
    month_entry_bg1.place(x=250,y=265)
    month_entry1 = t.Entry(update_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=3)
    month_entry1.place(x=267,y=275)
    month_label1 = t.Label(update_tab,text='(MM)',font=('DejaVuSansMono',9),fg=fg_color,bg='white')
    month_label1.place(x=262,y=305)

    year_entry_img1 = t.PhotoImage(file='resources\\half_label.png')
    year_entry_bg1 = t.Label(update_tab,image=year_entry_img1,bg='white')
    year_entry_bg1.place(x=320,y=265)
    year_entry1 = t.Entry(update_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color, width=5)
    year_entry1.place(x=340,y=275)
    year_label1 = t.Label(update_tab,text='(YYYY)',font=('DejaVuSansMono',9),fg=fg_color,bg='white')
    year_label1.place(x=340,y=305)

    vac_status1 = t.Label(update_tab,text = 'Choose New Vaccination Status',font=('DejaVuSansMono',12),bg='white',fg='black')
    vac_status1.place(x=380,y=85)
    vac_var1 = t.IntVar()
    unvaccinated_1 = t.Radiobutton(update_tab,bg='white',text='Unvaccinated',var=vac_var1,value=1,fg='red',font=('DejaVuSansMono',11))
    shot_1 = t.Radiobutton(update_tab,bg='white',text='1st Shot',var=vac_var1,value=2,fg='black',font=('DejaVuSansMono',11))
    shot_2 = t.Radiobutton(update_tab,bg='white',text='2nd Shot',var=vac_var1,value=3,fg='black',font=('DejaVuSansMono',11))
    unvaccinated_1.place(x=400,y=110)
    shot_1.place(x=400,y=140)
    shot_2.place(x=400,y=170)

    def delete_values():
        my_eid = eid_entry2.get()
        while True:
            try:
                my_eid = int(my_eid)
            except ValueError:
                messagebox.showerror('Error','Please Enter Employee-ID')
                break
            else:
                mcsr = mydb.cursor()
                cmd = f"DELETE FROM vaccination WHERE EMPLOYEEID = {my_eid}"
                mcsr.execute(cmd)
                mydb.commit()
                print(f'{eid} has been removed!')
                messagebox.showinfo('Removed!','Record has been removed!')
                window.destroy()
                gui()
                break
                
    def update_values():
        vals = []
        fname= fname_entry1.get()
        lname= lname_entry1.get()
        vals.append(fname+' '+lname)
        status = vac_var1.get()
        if status == 1:
            vals.append('Not Vaccinated')
        elif status == 2:
            vals.append('Partially Vaccinated')
        elif status == 3:
            vals.append('Fully Vaccinated')
        try:
            vac_date = int(date_entry1.get())
            vac_month = int(month_entry1.get())
            vac_year = int(year_entry1.get())
            vals.append(str(vac_date)+'-'+str(vac_month)+'-'+str(vac_year))
        except ValueError:
            messagebox.showerror('Error','Please Fill all the Fields')
        eid = int(eid_entry1.get())
        vals.append(eid)
        while True:
            if fname=='':
                messagebox.showerror('Error','Please Fill all the Fields')
                break
            elif status==0:
                messagebox.showerror('Error','Please Fill all the Fields')
                break
            elif eid == '':
                messagebox.showerror('Error','Please Fill all the Fields')
                break
            elif vac_date > 31:
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif vac_date < 0:
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif (vac_month > 12):
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif (vac_month < 0):
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif (vac_year > 2023):
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif (vac_year < 2020):
                messagebox.showerror('Error','Please Input Correct Date of Vaccination')
                break
            elif eid not in eids:
                messagebox.showerror('Error','Record for Specified Employee-ID does not Exist')
                break
            else:
                print(vals,' updated on database!')
                mycursor = mydb.cursor()

                sql = f'''UPDATE vaccination SET NAME = '{vals[0]}' WHERE EMPLOYEEID = {eid}'''
                mycursor.execute(sql)
                mydb.commit()

                sql = f'''UPDATE vaccination SET STATUS = '{vals[1]}' WHERE EMPLOYEEID = {eid}'''
                mycursor.execute(sql)
                mydb.commit()

                sql = f'''UPDATE vaccination SET DATE = '{vals[2]}' WHERE EMPLOYEEID = {eid}'''
                mycursor.execute(sql)
                mydb.commit()
                
                messagebox.showinfo('Updated!','Record has been upated!')
                window.destroy()
                gui()
                break

    #delete tab
    delete_background = t.Label(delete_tab,bg='white',height=34,width=99)
    delete_background.place(x=0,y=0)
    delete_ico_img = t.PhotoImage(file='resources\\delete 2.png')
    delete_ico = t.Label(delete_tab,image = delete_ico_img,bg='white')
    delete_ico.place(x=170,y=10)
    delete_title = t.Label(delete_tab,text='Delete A Current Record',font=('DejaVuSansMono',18),fg='#333',bg='white')
    delete_title.place(x=240,y=20)
    vac_img2 = t.PhotoImage(file='resources\\vacc2.png')
    vacc_img2 = t.Label(delete_tab,image=vac_img2,bg='white',fg='white',borderwidth=0)
    vacc_img2.place(x=375,y=210)
    eid2 = t.Label(delete_tab,text='Employee-ID',bg='white',fg='#333',font=('DejaVuSansMono',11))
    eid2.place(x=30,y=120)
    eid_entry_img2 = t.PhotoImage(file='resources\\half_label.png')
    eid_entry_bg2 = t.Label(delete_tab,image=eid_entry_img2,bg='white')
    eid_entry_bg2.place(x=130,y=110)
    eid_entry2 = t.Entry(delete_tab,bg='Light Grey',borderwidth=0,font=('DejaVuSansMono',12),fg=fg_color,width=5)
    eid_entry2.place(x=150,y=119)
    warning_img = t.PhotoImage(file='resources\\warning.png')
    warning = t.Label(delete_tab,image=warning_img,bg='white')
    warning.place(x=50,y=200)
    warningtxt = t.Label(delete_tab,text='Warning! This Process is Irrevesible',bg='white',font=('Arial ROUNDED MT BOLD',12))
    warningtxt.place(x=90,y=205)
    
    submit_img = t.PhotoImage(file='resources\\submit.png')
    submit_button = t.Button(add_tab,image=submit_img,height=60,width=190,borderwidth=0,bg='white',command=add_values)
    submit_button.place(x=230,y=350)
    
    submit_img1 = t.PhotoImage(file='resources\\submit.png')
    submit_button1 = t.Button(update_tab,image=submit_img1,height=60,width=190,borderwidth=0,bg='white',command=update_values)
    submit_button1.place(x=230,y=350)

    submit_img2 = t.PhotoImage(file='resources\\submit.png')
    submit_button2 = t.Button(delete_tab,image=submit_img2,height=60,width=190,borderwidth=0,bg='white',command=delete_values)
    submit_button2.place(x=230,y=350)
    
    
    window.mainloop()
    
gui()
