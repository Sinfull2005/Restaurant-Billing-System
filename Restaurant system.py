from tkinter import *
import tkinter as ttk
import tkinter.messagebox

#first screen
win= Tk()
win.geometry("1000x800")
win.title("Login")
win.configure(background="black")
def opening():
    top =Toplevel(win)
    top.geometry("1000x1000")
    top.title("restaurant")
    top.configure(background="black")
    Header = Frame(top,bg='black',bd=3,relief=FLAT)
    Header.pack(side=TOP)
    lblTitle=Label(Header,font=('baskerville old face',40,'bold'),text='RESTAURANT MENU ',bd=21,bg='black',fg='white',justify=CENTER)
    lblTitle.grid(row=0, column=0)
    
    def drinks():
        #setting up 2nd screen
        drinks= Toplevel(top)
        drinks.geometry("500x500")
        drinks.title("drinks")
        drinks.configure(background="black")
        MenuFrame = Frame(drinks,bg='black',bd=50,relief=FLAT)
        MenuFrame.pack(side=TOP)
        Drinks_F=Frame(MenuFrame,bg='black',bd=4)
        #Drinkmoney_F=Frame(MenuFrame, bg='black',bd=2)
        Drinks_F.pack(side=TOP)
        #setting up labels and text
        Drinktitle= Label(Drinks_F,text='   DRINKS MENU',font=('baskerville old face',30,'bold'),bg='black',fg='orange').grid(row=0,sticky=W)
        Milkshake= Label(Drinks_F,text='Milkshake           Rs.150',font=('baskerville old face',24,'bold'),fg='orange',bg='black').grid(row=1,sticky=W)
        BubbleTea= Label(Drinks_F,text='BubbleTea          Rs.50',font=('baskerville old face',24,'bold'),fg='orange',bg='black').grid(row=2,sticky=W)
        DietCoke= Label(Drinks_F,text='DietCoke            Rs.80',font=('baskerville old face',24,'bold'),fg='orange',bg='black').grid(row=3,sticky=W)
        IcedTea= Label(Drinks_F,text='IcedTea               Rs.100',font=('baskerville old face',24,'bold'),fg='orange',bg='black').grid(row=4,sticky=W)
        Coffee= Label(Drinks_F,text='Coffee                 Rs.50',font=('baskerville old face',24,'bold'),fg='orange',bg='black').grid(row=5,sticky=W)
        Mocktail= Label(Drinks_F,text='Mocktail             Rs.80',font=('baskerville old face',24,'bold'),fg='orange',bg='black').grid(row=6,sticky=W)
        CocaCola= Label(Drinks_F,text='CocaCola             Rs.70',font=('baskerville old face',24,'bold'),fg='orange',bg='black').grid(row=7,sticky=W)
        HotChocolate= Label(Drinks_F,text='HotChocolate     Rs.160',font=('baskerville old face',24,'bold'),fg='orange',bg='black').grid(row=8,sticky=W)
    ttk.Button(top,text="Drinks Menu",fg="orange",font=("baskervile old face",16,"bold"),width=20,bg="black",command=drinks).pack(padx=10,pady=50)
    def food():
        #setting up 2nd screen
        food= Toplevel(top)
        food.geometry("500x500")
        food.title("food")
        food.configure(background="black")
        MenuFrame = Frame(food,bg='black',bd=50,relief=FLAT)
        MenuFrame.pack(side=TOP)
        Food_F=Frame(MenuFrame,bg='black',bd=4)
        Food_F.pack(side=TOP)
        #setting up labels and  text boxes
        Foodtitle= Label(Food_F,text='  FOOD MENU',font=('baskerville old face',30,'bold'),bg='black',fg='pink').grid(row=0,sticky=W)
        Burger = Label(Food_F,text="Burger          Rs.100 ",font=('baskerville old face',24,'bold'),bg='black',fg='pink').grid(row=1,sticky=W)
        Pizza =  Label(Food_F,text="Pizza           Rs.350",font=('baskerville old face',24,'bold'),bg='black',fg='pink').grid(row=2,sticky=W)
        Pasta =  Label(Food_F,text="Pasta           Rs.280 ",font=('baskerville old face',24,'bold'),bg='black',fg='pink').grid(row=3,sticky=W)
        Fries =  Label(Food_F,text="Fries            Rs.60 ",font=('baskerville old face',24,'bold'),bg='black',fg='pink').grid(row=4,sticky=W)
        Sandwich =  Label(Food_F,text="Sandwich     Rs.150",font=('baskerville old face',24,'bold'),bg='black',fg='pink').grid(row=5,sticky=W)
        Salad = Label(Food_F,text="Salad            Rs.200 ",font=('baskerville old face',24,'bold'),bg='black',fg='pink').grid(row=6,sticky=W)
        Nachos =  Label(Food_F,text="Nachos         Rs.90 ",font=('baskerville old face',24,'bold'),bg='black',fg='pink').grid(row=7,sticky=W)
        IceCream =  Label(Food_F,text="IceCream     Rs.25 ",font=('baskerville old face',24,'bold'),bg='black',fg='pink').grid(row=8,sticky=W)       
    ttk.Button(top,text="Food Menu",fg="pink",font=("baskervile old face",16,"bold"),width=20,bg="black",command=food).pack(padx=10,pady=50)
    def receipt():
        receipt= Toplevel(top)
        receipt.geometry("1000x1000")
        receipt.title("receipt")
        receipt.configure(background="black")
        Header1 = Frame(receipt,bg='black',bd=3,relief=FLAT)
        Header1.pack(side=TOP)
        lblTitle=Label(Header1,font=('baskerville old face',40,'bold'),text='RESTAURANT BILLING SYSTEM',bd=21,bg='black',fg='LIGHT BLUE',justify=CENTER)
        lblTitle.grid(row=0, column=0)

        Receipt_1 = Frame(receipt,bg='black',bd=12,relief=FLAT)
        Receipt_1.pack(side=RIGHT)

        Buttons_F=Frame(Receipt_1,bg='black',bd=3,relief=FLAT)
        Buttons_F.pack(side=BOTTOM)

        Receipt_2=Frame(Receipt_1,bg='black',bd=4,relief=FLAT)
        Receipt_2.pack(side=BOTTOM)

        MenuFrame = Frame(receipt,width=25,height=25,bg='black',bd=10,relief=FLAT)
        MenuFrame.pack(side=LEFT)
        Cost_F=Frame(MenuFrame,bg='black',bd=4)
        Cost_F.pack(side=BOTTOM)
        Drinks_F=Frame(MenuFrame,bg='black',bd=4)
        Drinks_F.pack(side=TOP)


        Drinks_F=Frame(MenuFrame,bg='black',bd=4,relief=FLAT)
        Drinks_F.pack(side=LEFT)
        Food_F=Frame(MenuFrame,bg='black',bd=4,relief=FLAT)
        Food_F.pack(side=RIGHT)

        #assign variables
        PaidTax = StringVar()
        SubTotal = StringVar()
        TotalCost = StringVar()
        CostofFood = StringVar()
        CostofDrinks = StringVar()
        ServiceCharge = StringVar()


        E_Milkshake = StringVar()
        E_BubbleTea = StringVar()
        E_DietCoke = StringVar()
        E_IcedTea = StringVar()
        E_Coffee = StringVar()
        E_Mocktail = StringVar()
        E_CocaCola = StringVar()
        E_HotChocolate = StringVar()

        E_Burger = StringVar()
        E_Pizza = StringVar()
        E_Pasta = StringVar()
        E_Fries = StringVar()
        E_Sandwich = StringVar()
        E_Salad = StringVar()
        E_Nachos = StringVar()
        E_IceCream = StringVar()


        #setting entries
        E_Milkshake.set("0")
        E_BubbleTea.set("0")
        E_DietCoke.set("0")
        E_IcedTea.set("0")
        E_Coffee.set("0")
        E_Mocktail.set("0")
        E_CocaCola.set("0")
        E_HotChocolate.set("0")

        E_Burger.set("0")
        E_Pizza.set("0")
        E_Pasta.set("0")
        E_Fries.set("0")
        E_Sandwich.set("0")
        E_Salad.set("0")
        E_Nachos.set("0")
        E_IceCream.set("0")

        #defining functions
        def Totaldrinks():
            Item1=float(E_Milkshake.get())
            Item2=float(E_BubbleTea.get())
            Item3=float(E_DietCoke.get())
            Item4=float(E_IcedTea.get())
            Item5=float(E_Coffee.get())
            Item6=float(E_Mocktail.get())
            Item7=float(E_CocaCola.get())
            Item8=float(E_HotChocolate.get())
            PriceofDrinks =(Item1 * 150) + (Item2 * 50) + (Item3 * 80) + (Item4 * 100) + (Item5 * 50 ) + (Item6 * 80) + (Item7 * 70) + (Item8 * 160)
            return PriceofDrinks

        def Totalfood():
            Item9=float(E_Burger.get())
            Item10=float(E_Pizza.get())
            Item11=float(E_Pasta.get())
            Item12=float(E_Fries.get())
            Item13=float(E_Sandwich.get())
            Item14=float(E_Salad.get())
            Item15=float(E_Nachos.get())
            Item16=float(E_IceCream.get())

            PriceofFood =(Item9 * 100) + (Item10 * 350) + (Item11 * 280) + (Item12 * 60) + (Item13 * 150) + (Item14 * 200) + (Item15 * 90) + (Item16 * 25)
            return PriceofFood

        def Tax():
            Tax1 = (Totaldrinks() + Totalfood())* 0.1
            return Tax1
        def subtotal():
            SubTotalofITEMS = Totaldrinks() + Totalfood()
            return SubTotalofITEMS
        def total():
            TT=subtotal()+Tax()
            return(TT)

        #setting calculated values for ui
        def CostofItem():
            DrinksPrice = "Rs."+str(Totaldrinks())
            FoodPrice =  "Rs."+str(Totalfood())
            Tax2="Rs."+str(Tax())
            TC="Rs."+str(total())
            subt="Rs."+str(subtotal())
            CostofFood.set(FoodPrice)
            CostofDrinks.set(DrinksPrice)
            SubTotal.set(subt)
            PaidTax.set(Tax2)
            TotalCost.set(TC)

        #receipt
        def Receipt():
            txtReceipt.delete("1.0","end")
            txtReceipt.insert(END,'Items:\t\t'+"Quantity \t\t"+"Price\n")
            if float(E_Milkshake.get())!=0:
                txtReceipt.insert(END,'Milkshake:\t\t' + E_Milkshake.get() +'\t\t 150\n')
            if float(E_BubbleTea.get())!=0:
                txtReceipt.insert(END,'BubbleTea:\t\t'+ E_BubbleTea.get()+'\t\t 50\n')
            if float(E_DietCoke.get())!=0:
                txtReceipt.insert(END,'DietCoke:\t\t'+ E_DietCoke.get()+'\t\t 80\n')
            if float(E_IcedTea.get()) !=0:
                txtReceipt.insert(END,'IcedTea:\t\t'+ E_IcedTea.get()+'\t\t 100\n')
            if float(E_Coffee.get()) !=0:
                txtReceipt.insert(END,'Coffee:\t\t'+ E_Coffee.get()+'\t\t 50\n')
            if float(E_Mocktail.get()) !=0:
                txtReceipt.insert(END,'Mocktail:\t\t'+ E_Mocktail.get()+'\t\t 80\n')
            if float(E_CocaCola.get()) !=0:
                txtReceipt.insert(END,'CocaCola:\t\t'+ E_CocaCola.get()+'\t\t 70\n')
            if float(E_HotChocolate.get()) !=0:
                txtReceipt.insert(END,'HotChocolate:\t\t'+ E_HotChocolate.get()+'\t\t 160\n')
            if float(E_Burger.get()) !=0:
                txtReceipt.insert(END,'Burger:\t\t'+ E_Burger.get()+'\t\t 100\n')
            if float(E_Pizza.get()) !=0:
                txtReceipt.insert(END,'Pizza:\t\t'+ E_Pizza.get()+'\t\t 350\n')
            if float(E_Pasta.get()) !=0:
                txtReceipt.insert(END,'Pasta:\t\t'+ E_Pasta.get()+'\t\t 280\n')
            if float(E_Fries.get()) !=0:
                txtReceipt.insert(END,'Fries:\t\t'+ E_Fries.get()+'\t\t 60\n')
            if float(E_Sandwich.get()) !=0:
                txtReceipt.insert(END,'Sandwich:\t\t'+ E_Sandwich.get()+'\t\t 150\n')
            if float(E_Salad.get()) !=0:
                txtReceipt.insert(END,'Salad:\t\t'+ E_Salad.get()+'\t\t 200\n')
            if float(E_Nachos.get()) !=0:
                txtReceipt.insert(END,'Nachos:\t\t'+ E_Nachos.get()+'\t\t 90\n')
            if float(E_IceCream.get()) !=0:
                txtReceipt.insert(END,'IceCream:\t\t'+ E_IceCream.get()+'\t\t 25\n')
            txtReceipt.insert(END,'\nCost of Drinks:\t\t\t\t'+ CostofDrinks.get()+'\nCost of Food:\t\t\t\t'+ CostofFood.get())
            txtReceipt.insert(END,'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\nTotal:\t\t\t\t"+str(TotalCost.get())+'\n')

        def AddRecord():
            txtReceipt.delete("1.0","end")
            if total()==0:
                txtReceipt.insert(END, "No records chosen")
            else:
                import mysql.connector as mc
                con=mc.connect(host='localhost', user='root', password='Sql_2005@', database='restaurant')
                cursor=con.cursor()
                q1="create table if not exists bill(Totaldrinks integer, Totalfood integer, Tax integer, Subtotal integer, Total integer)"
                query=" insert into bill values({},{},{},{},{})".format(Totaldrinks(),Totalfood(),Tax(),subtotal(),total())
                cursor.execute(q1)
                cursor.execute(query)
                txtReceipt.insert(END, "Record successfully added")
                con.commit()
        def DisplayRecord():
            txtReceipt.delete("1.0","end")
            import mysql.connector as mc
            con=mc.connect(host='localhost', user='root', password='Sql_2005@', database='restaurant')
            cursor=con.cursor()
            query="select * from bill "
            cursor.execute(query)
            a=cursor.fetchall()
            i=0
            txtReceipt.insert(END,'Drinks\t'+' '+'Food\t'+' ' +'Tax\t'+' '+ 'Subtotal\t'+' '+'Total\n')
            for i in a:
                for j in i :
                    txtReceipt.insert(END, str(j)+'\t'+' ')
                txtReceipt.insert(END,'\n')
                con.commit()
            '''for bill in cursor:
                for j in range(len(bill)):
                    txtReceipt.grid(row=i, column=j)
                    txtReceipt.insert(END, str(bill[j])+'\t'+' ')
                    #txtReceipt.insert(END,'\n')
                    #i=i+1
                    con.commit()'''


        #menu labels
        Milkshake= Label(Drinks_F,text='Milkshake',font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=0,sticky=W)
        BubbleTea= Label(Drinks_F,text='BubbleTea',font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=1,sticky=W)
        DietCoke= Label(Drinks_F,text='DietCoke',font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=2,sticky=W)
        IcedTea= Label(Drinks_F,text='IcedTea',font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=3,sticky=W)
        Coffee= Label(Drinks_F,text='Coffee',font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=4,sticky=W)
        Mocktail= Label(Drinks_F,text='Mocktail',font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=5,sticky=W)
        CocaCola= Label(Drinks_F,text='CocaCola',font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=6,sticky=W)
        HotChocolate= Label(Drinks_F,text='HotChocolate',font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=7,sticky=W)
        Burger = Label(Food_F,text="Burger\t\t\t ",font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=0,sticky=W)
        Pizza =  Label(Food_F,text="Pizza",font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=1,sticky=W)
        Pasta =  Label(Food_F,text="Pasta ",font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=2,sticky=W)
        Fries =  Label(Food_F,text="Fries ",font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=3,sticky=W)
        Sandwich =  Label(Food_F,text="Sandwich ",font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=4,sticky=W)
        Salad =  Label(Food_F,text="Salad ",font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=5,sticky=W)
        Nachos =  Label(Food_F,text="Nachos ",font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=6,sticky=W)
        IceCream =  Label(Food_F,text="IceCream ",font=('baskerville old face',16,'bold'),bg='black',fg='light blue').grid(row=7,sticky=W)

        #text boxes(entries)
        txtMilkshake = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_Milkshake)
        txtMilkshake.grid(row=0,column=1)

        txtBubbleTea = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_BubbleTea)
        txtBubbleTea.grid(row=1,column=1)

        txtDietCoke = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_DietCoke)
        txtDietCoke.grid(row=2,column=1)

        txtIcedTea= Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_IcedTea)
        txtIcedTea.grid(row=3,column=1)

        txtCoffee = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_Coffee)
        txtCoffee.grid(row=4,column=1)

        txtMocktail = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_Mocktail)
        txtMocktail.grid(row=5,column=1)

        txtCocaCola = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_CocaCola)
        txtCocaCola.grid(row=6,column=1)

        txtHotChocolate = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_HotChocolate)
        txtHotChocolate.grid(row=7,column=1)

        txtBurger=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state=NORMAL,textvariable=E_Burger)
        txtBurger.grid(row=0,column=1)

        txtPizza=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state=NORMAL,textvariable=E_Pizza)
        txtPizza.grid(row=1,column=1)

        txtPasta=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_Pasta)
        txtPasta.grid(row=2,column=1)

        txtFries=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_Fries)
        txtFries.grid(row=3,column=1)

        txtSandwich=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_Sandwich)
        txtSandwich.grid(row=4,column=1)

        txtSalad=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_Salad)
        txtSalad.grid(row=5,column=1)

        txtNachos=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_Nachos)
        txtNachos.grid(row=6,column=1)

        txtIceCream=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,textvariable=E_IceCream)
        txtIceCream.grid(row=7,column=1)

        #labels and txtboxes for 'total' frame
        lblCostofDrinks=Label(Cost_F,font=('baskerville old face',14,'bold'),text='Cost of Drinks\t',bg='black',fg='light blue',justify=LEFT)
        lblCostofDrinks.grid(row=1,column=0,sticky=W)
        txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),insertwidth=2,justify=LEFT,textvariable=CostofDrinks)
        txtCostofDrinks.grid(row=1,column=1)

        lblCostofFood=Label(Cost_F,font=('baskerville old face',14,'bold'),text='Cost of Food  ',bg='black',fg='light blue',justify=LEFT)
        lblCostofFood.grid(row=2,column=0,sticky=W)
        txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),insertwidth=2,justify=LEFT,textvariable=CostofFood)
        txtCostofFood.grid(row=2,column=1)

        lblTax=Label(Cost_F,font=('baskerville old face',14,'bold'),text='\tTax',bg='black',bd=7,fg='light blue',justify=LEFT)
        lblTax.grid(row=0,column=2,sticky=W)
        txtTax=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),insertwidth=2,justify=LEFT,textvariable=PaidTax)
        txtTax.grid(row=0,column=3)

        lblSubTotal=Label(Cost_F,font=('baskerville old face',14,'bold'),text='\tSub Total',bg='black',bd=7,fg='light blue',justify=LEFT)
        lblSubTotal.grid(row=1,column=2,sticky=W)
        txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),insertwidth=2,justify=LEFT,textvariable=SubTotal)
        txtSubTotal.grid(row=1,column=3)

        lblTotalCost=Label(Cost_F,font=('baskerville old face',14,'bold'),text='\tTotal',bg='black',bd=7,fg='light blue',justify=LEFT)
        lblTotalCost.grid(row=2,column=2,sticky=W)
        txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),insertwidth=2,justify=LEFT,textvariable=TotalCost)
        txtTotalCost.grid(row=2,column=3)

        txtReceipt=Text(Receipt_2,width=40,height=21,bg='white',bd=4,font=('baskerville old face',12,'bold'))
        txtReceipt.grid(row=0,column=0)

        #buttons on receipt frame
        btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='light blue',font=('baskerville old face',16,'bold'),width=4,text='Total',bg='black',command=CostofItem).grid(row=0,column=0)
        btnAddRecord=Button(Buttons_F,padx=16,pady=1,bd=7,fg='light blue',font=('baskerville old face',16,'bold'),width=8,text='Add Record',bg='black',command=AddRecord).grid(row=0,column=2)
        btnDisplayRecords=Button(Buttons_F,padx=16,pady=1,bd=7,fg='light blue',font=('baskerville old face',16,'bold'),width=10,text='Display Records',bg='black',command=DisplayRecord).grid(row=0,column=3)
        btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='light blue',font=('baskerville old face',16,'bold'),width=4,text='Receipt',bg='black',command=Receipt).grid(row=0,column=1)
    ttk.Button(top,text="Receipt",fg="light blue",font=("baskervile old face",16,"bold"),width=20,bg="black",command=receipt).pack(padx=10,pady=50)
    
    def logout():
        win.destroy()
    ttk.Button(top,text="Logout",fg="red",font=("baskervile old face",16,"bold"),width=20,bg="black",command=logout).pack(padx=10,pady=50)
    
    top.mainloop()
    
#Create a button in the main Window to open the popup    
Label(win, text=" ENTER PASSWORD TO LOGIN", font=("baskervile old face",40),width=40,bg='black',fg='yellow').pack(pady=50)
password= ttk.StringVar()

pwd=ttk.Entry(win, width = 40,textvariable =password,show="*").pack(padx=50,pady=50)

def valid():
    paswd=password.get()
    if paswd=="Rest1205":
        opening()
    else:
        tkinter.messagebox.showinfo("Password Error",  "Invalid password")

ttk.Button(win, text= "ENTER", font=("baskervile old face",20,'bold'),width=20,
           command= valid,bg='black',fg='blue',activebackground='red').pack(padx=10,pady=10)
win.mainloop()

