#setting up the interface
from tkinter import *
root =Tk()
root.geometry("1350x750")
root.title("Food Billing System")
root.configure(background='BLACK')

#editing the interface
Header = Frame(root,bg='WHITE',bd=3,relief=FLAT)
Header.pack(side=TOP)

lblTitle=Label(Header,font=('baskerville old face',40,'bold'),text='FOOD BILLING SYSTEM',bd=21,bg='LIGHT BLUE',
                fg='black',justify=CENTER)
lblTitle.grid(row=0, column=0)

Receipt_1 = Frame(root,bg='light blue',bd=12,relief=FLAT)
Receipt_1.pack(side=RIGHT)

Buttons_F=Frame(Receipt_1,bg='light blue',bd=3,relief=FLAT)
Buttons_F.pack(side=BOTTOM)

Receipt_2=Frame(Receipt_1,bg='light blue',bd=4,relief=FLAT)
Receipt_2.pack(side=BOTTOM)

MenuFrame = Frame(root,bg='light blue',bd=10,relief=FLAT)
MenuFrame.pack(side=LEFT)
Cost_F=Frame(MenuFrame,bg='light blue',bd=4)
Cost_F.pack(side=BOTTOM)
Drinks_F=Frame(MenuFrame,bg='light blue',bd=4)
Drinks_F.pack(side=TOP)


Drinks_F=Frame(MenuFrame,bg='light blue',bd=4,relief=FLAT)
Drinks_F.pack(side=LEFT)
Food_F=Frame(MenuFrame,bg='light blue',bd=4,relief=FLAT)
Food_F.pack(side=RIGHT)

#assigning the variables
PaidTax = StringVar()
SubTotal = StringVar()
TotalCost = StringVar()
CostofFood = StringVar()
CostofDrinks = StringVar()
ServiceCharge = StringVar()


E_Milkshake = StringVar()
E_Pepsi = StringVar()
E_DietCoke = StringVar()
E_IcedTea = StringVar()
E_Coffee = StringVar()
E_Fanta = StringVar()
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

E_Milkshake.set("0")
E_Pepsi.set("0")
E_DietCoke.set("0")
E_IcedTea.set("0")
E_Coffee.set("0")
E_Fanta.set("0")
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

#defining
def CostofItem():
    Item1=float(E_Milkshake.get())
    Item2=float(E_Pepsi.get())
    Item3=float(E_DietCoke.get())
    Item4=float(E_IcedTea.get())
    Item5=float(E_Coffee.get())
    Item6=float(E_Fanta.get())
    Item7=float(E_CocaCola.get())
    Item8=float(E_HotChocolate.get())

    Item9=float(E_Burger.get())
    Item10=float(E_Pizza.get())
    Item11=float(E_Pasta.get())
    Item12=float(E_Fries.get())
    Item13=float(E_Sandwich.get())
    Item14=float(E_Salad.get())
    Item15=float(E_Nachos.get())
    Item16=float(E_IceCream.get())

    PriceofDrinks =(Item1 * 150) + (Item2 * 50) + (Item3 * 80) + (Item4 * 100) + (Item5 * 50 ) + (Item6 * 30) + (Item7 * 70) + (Item8 * 160)

    PriceofFood =(Item9 * 100) + (Item10 * 350) + (Item11 * 280) + (Item12 * 60) + (Item13 * 150) + (Item14 * 200) + (Item15 * 90) + (Item16 * 25)



    DrinksPrice = "Rs.",str(PriceofDrinks)
    FoodPrice =  "Rs.",str(PriceofFood)
    CostofFood.set(FoodPrice)
    CostofDrinks.set(DrinksPrice)

    SubTotalofITEMS = "Rs.",str(PriceofDrinks + PriceofFood )
    SubTotal.set(SubTotalofITEMS)

    Tax = "Rs.",str((PriceofDrinks + PriceofFood  )* 0.1)
    PaidTax.set(Tax)

    TT=((PriceofDrinks + PriceofFood ) * 0.1)
    TC="Rs.",str(PriceofDrinks + PriceofFood+ TT )
    TotalCost.set(TC)


#receipt
def Receipt():

    
    txtReceipt.insert(END,'Items:\t\t'+"Quantity \t\t"+"Price\n")
    if float(E_Milkshake.get())!=0:
        txtReceipt.insert(END,'Milkshake:\t\t' + E_Milkshake.get() +'\t\t 150\n')
    if float(E_Pepsi.get())!=0:
        txtReceipt.insert(END,'Pepsi:\t\t'+ E_Pepsi.get()+'\t\t 50\n')
    if float(E_DietCoke.get())!=0:
        txtReceipt.insert(END,'DietCoke:\t\t'+ E_DietCoke.get()+'\t\t 80\n')
    if float(E_IcedTea.get()) !=0:
        txtReceipt.insert(END,'IcedTea:\t\t'+ E_IcedTea.get()+'\t\t 100\n')
    if float(E_Coffee.get()) !=0:
        txtReceipt.insert(END,'Coffee:\t\t'+ E_Coffee.get()+'\t\t 50\n')
    if float(E_Fanta.get()) !=0:
        txtReceipt.insert(END,'Fanta:\t\t'+ E_Fanta.get()+'\t\t 30\n')
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
    txtReceipt.insert(END,'Cost of Drinks:\t\t\t\t'+ CostofDrinks.get()+'\nTax Paid:\t\t\t\t'+PaidTax.get()+"\n")
    txtReceipt.insert(END,'Cost of Foods:\t\t\t\t'+ CostofFood.get()+'\nSubTotal:\t\t\t\t'+str(SubTotal.get())+"\nTotal:\t\t\t\t"+str(TotalCost.get())+'\n')
    


Milkshake= Label(Drinks_F,text='Milkshake',
                 font=('baskerville old face',18,'bold'),bg='light blue').grid(row=0,sticky=W)
Pepsi= Label(Drinks_F,text='Pepsi',font=('baskerville old face',18,'bold'),
                    bg='light blue').grid(row=1,sticky=W)
DietCoke= Label(Drinks_F,text='DietCoke',font=('baskerville old face',18,'bold'),
                    bg='light blue').grid(row=2,sticky=W)
IcedTea= Label(Drinks_F,text='IcedTea',font=('baskerville old face',18,'bold'),
                    bg='light blue').grid(row=3,sticky=W)
Coffee= Label(Drinks_F,text='Coffee',font=('baskerville old face',18,'bold'),
                    bg='light blue').grid(row=4,sticky=W)
Fanta= Label(Drinks_F,text='Fanta',font=('baskerville old face',18,'bold'),
                    bg='light blue').grid(row=5,sticky=W)
CocaCola= Label(Drinks_F,text='CocaCola',font=('baskerville old face',18,'bold'),
                    bg='light blue').grid(row=6,sticky=W)
HotChocolate= Label(Drinks_F,text='HotChocolate',font=('baskerville old face',18,'bold'),
                    bg='light blue').grid(row=7,sticky=W)
Burger = Label(Food_F,text="Burger\t\t\t ",
                        font=('baskerville old face',16,'bold'),bg='light blue').grid(row=0,sticky=W)
Pizza =  Label(Food_F,text="Pizza",
                        font=('baskerville old face',16,'bold'),bg='light blue').grid(row=1,sticky=W)
Pasta =  Label(Food_F,text="Pasta ",
                        font=('baskerville old face',16,'bold'),bg='light blue').grid(row=2,sticky=W)
Fries =  Label(Food_F,text="Fries ",
                        font=('baskerville old face',16,'bold'),bg='light blue').grid(row=3,sticky=W)
Sandwich =  Label(Food_F,text="Sandwich ",
                        font=('baskerville old face',16,'bold'),bg='light blue').grid(row=4,sticky=W)
Salad =  Label(Food_F,text="Salad ",
                        font=('baskerville old face',16,'bold'),bg='light blue').grid(row=5,sticky=W)
Nachos =  Label(Food_F,text="Nachos ",
                        font=('baskerville old face',16,'bold'),bg='light blue').grid(row=6,sticky=W)
IceCream =  Label(Food_F,text="IceCream ",
                        font=('baskerville old face',16,'bold'),bg='light blue').grid(row=7,sticky=W)

#text boxes
txtMilkshake = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL
                        ,textvariable=E_Milkshake)
txtMilkshake.grid(row=0,column=1)

txtPepsi = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL
                        ,textvariable=E_Pepsi)
txtPepsi.grid(row=1,column=1)

txtDietCoke = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL
                        ,textvariable=E_DietCoke)
txtDietCoke.grid(row=2,column=1)

txtIcedTea= Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL
                        ,textvariable=E_IcedTea)
txtIcedTea.grid(row=3,column=1)

txtCoffee = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL
                        ,textvariable=E_Coffee)
txtCoffee.grid(row=4,column=1)

txtFanta = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL
                        ,textvariable=E_Fanta)
txtFanta.grid(row=5,column=1)

txtCocaCola = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL
                        ,textvariable=E_CocaCola)
txtCocaCola.grid(row=6,column=1)

txtHotChocolate = Entry(Drinks_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL
                        ,textvariable=E_HotChocolate)
txtHotChocolate.grid(row=7,column=1)

txtBurger=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state=NORMAL,
                        textvariable=E_Burger)
txtBurger.grid(row=0,column=1)

txtPizza=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state=NORMAL,
                        textvariable=E_Pizza)
txtPizza.grid(row=1,column=1)

txtPasta=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,
                        textvariable=E_Pasta)
txtPasta.grid(row=2,column=1)

txtFries=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,
                        textvariable=E_Fries)
txtFries.grid(row=3,column=1)

txtSandwich=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,
                        textvariable=E_Sandwich)
txtSandwich.grid(row=4,column=1)

txtSalad=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,
                        textvariable=E_Salad)
txtSalad.grid(row=5,column=1)

txtNachos=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,
                        textvariable=E_Nachos)
txtNachos.grid(row=6,column=1)

txtIceCream=Entry(Food_F,font=('baskerville old face',16,'bold'),bd=8,width=6,justify=LEFT,state= NORMAL,
                        textvariable=E_IceCream)
txtIceCream.grid(row=7,column=1)


#labels
lblCostofDrinks=Label(Cost_F,font=('baskerville old face',14,'bold'),text='Cost of Drinks\t',bg='light blue',
                fg='black',justify=CENTER)
lblCostofDrinks.grid(row=1,column=0,sticky=W)
txtCostofDrinks=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofDrinks)
txtCostofDrinks.grid(row=1,column=1)


lblCostofFood=Label(Cost_F,font=('baskerville old face',14,'bold'),text='Cost of Foods  ',bg='light blue',
                fg='black',justify=CENTER)
lblCostofFood.grid(row=2,column=0,sticky=W)
txtCostofFood=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=CostofFood)
txtCostofFood.grid(row=2,column=1)


lblTax=Label(Cost_F,font=('baskerville old face',14,'bold'),text='\tTax',bg='light blue',bd=7,
                fg='black',justify=CENTER)
lblTax.grid(row=0,column=2,sticky=W)
txtTax=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=PaidTax)
txtTax.grid(row=0,column=3)

lblSubTotal=Label(Cost_F,font=('baskerville old face',14,'bold'),text='\tSub Total',bg='light blue',bd=7,
                fg='black',justify=CENTER)
lblSubTotal.grid(row=1,column=2,sticky=W)
txtSubTotal=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=SubTotal)
txtSubTotal.grid(row=1,column=3)

lblTotalCost=Label(Cost_F,font=('baskerville old face',14,'bold'),text='\tTotal',bg='light blue',bd=7,
                fg='black',justify=CENTER)
lblTotalCost.grid(row=2,column=2,sticky=W)
txtTotalCost=Entry(Cost_F,bg='white',bd=7,font=('baskerville old face',14,'bold'),
                        insertwidth=2,justify=RIGHT,textvariable=TotalCost)
txtTotalCost.grid(row=2,column=3)

txtReceipt=Text(Receipt_2,width=52,height=21,bg='white',bd=4,font=('baskerville old face',12,'bold'))
txtReceipt.grid(row=0,column=0)

#buttons
btnTotal=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('baskerville old face',16,'bold'),width=4,text='Total',
                        bg='light blue',command=CostofItem).grid(row=0,column=0)
btnReceipt=Button(Buttons_F,padx=16,pady=1,bd=7,fg='black',font=('baskerville old face',16,'bold'),width=4,text='Receipt',
                        bg='light blue',command=Receipt).grid(row=0,column=1)

#DONE BY MANASVI ,SHRIYA , SINCHANA , TANISHA
root.mainloop()
