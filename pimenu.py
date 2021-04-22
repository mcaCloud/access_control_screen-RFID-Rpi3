#!/usr/bin/python2
# -*- coding: utf-8 -*-
#--------------------------------------------------------
#--------       Libraries     ---------------------------
#--------------------------------------------------------
import Tkconstants as TkC
import os
import subprocess
import sys
import PIL
import time

import numpy as np
#from Tkinter import Tk, Frame, Button, Label, PhotoImage
from Tkinter import *
import tkMessageBox
from math import sqrt, floor, ceil
from PIL import Image, ImageTk
import yaml
#Para generar numeros aleatorio de facturas
import random
# ------------------------------------------
#--------------- TK()---------------------
#
#
# En Este programa no tengo una clase que inicializa,
#sino que lo hago sin clase. Por eso el Objeto de Tk() tiene que ir primero

root = Tk()
# ------------------------------------------
#--------------- VARIABLES ------------------
#
#---------ENTRY-----------
#Aqui recojemos y convertimos el numero que llega del ENTRY
entry_content = IntVar()
#Para poder hacer recuperar el numero de target es necesario utilizar TEXT
entry = Text(root,width = 0,height = 0)
entry.pack(side = RIGHT)
entry.focus()
#
#---------FUN-LABEL-----------
#Para poder hacer recuperar el numero de target es necesario utilizar TEXT
l = Label(root,
          text = "Demon Slayer Corps ",
          height = 1,
          font = ('Gothic',30,'bold'),
          bg = 'white',
          fg = 'red',
          bd = 20
          )
l.pack(side = BOTTOM)

#
#---------PSW-----------
#Esta variable Global nos guarda la targeta autorizada
password = IntVar()
#---------PATH-----------
#Este es el PATH del projecto para no tener que escribir siempre la ruta
path = os.path.dirname(os.path.realpath(sys.argv[0]))

# ------------------------------------------
#--------------- Frame ---------------------
#
#
marco = Frame(root, bg ='white')
marco.pack()

# -----------------------------------------------
#--------------- COVER-IMAGE ---------------------
#
#
image = Image.open(path + "/img/inosuke.png")
image = image.resize((560,340), Image.ANTIALIAS)
photo= ImageTk.PhotoImage(image)

lblTitle = Label(marco, image = photo, bg='white')
#SI no pongo esto para inicializar la imagen, no display
lblTitle.image = photo
lblTitle.config(bg = "white", fg = "white")
lblTitle.grid(row = 1, column =0,pady = 20, padx = 20)

# -----------------------------------------------
#--------------- EXIT FUNC ---------------------
#
#
# La funcion tiene que creanse antes de poder ser llamada por el objeto
def iExit():
    salida = tkMessageBox.askyesno("ATTENCION", "¿Desea cerrar el programa?")
    if salida > 0:
        root.destroy()
    else:
        return
# -----------------------------------------------
#--------------- EXIT BUTTON ---------------------
#
#
image_B = Image.open(path + '/ico/close.gif')
image_B = image_B.resize((10, 10), Image.ANTIALIAS)
photo= ImageTk.PhotoImage(image_B)

B = Button(
            marco,
            text='Exit',
            #width=10,
            image= photo,
            font=('arial', 25, 'bold'),
            command = iExit
            )
B.grid(row=0, column=0, padx=1, pady=1, sticky=TkC.W)

# -----------------------------------------------
#--------------- CHECK-TAG ---------------------
#
#
#Esto es lo que nos ayuda con el BIND del Root
#Cada vez que ocurra un evento en ROOT corre esta funcion que llama al metodo login
def checkRFidTag(event):
    Login_System()


def new_window():

    newWindow = Toplevel(root)
    newWindow.attributes('-fullscreen', True)

    app = PiMenu(newWindow)

    app.pack(fill=TkC.BOTH, expand=1)
# -----------------------------------------------
#--------------- CHECK-TAG ---------------------
#
#
def Login_System():
    #To get Tkinter input from the text box, you must add a few more attributes to the normal
        #"1.0"
            #means that the input should be read from line one, character zero (ie: the very first character).
        #end-1c
            #part means to read until the end of the text box is reached.
            #Pero como agrega una nueva linea es necesario removerla
            #-1c significa que remove one caracter
    pss = entry.get(1.0,"end-1c")

    #Convertimos el ENTRY a un ENTERO
    #Llamo ala variable global y asigno lo que recibi del ENTRY
    entry_content.set(pss)
    #Para que no me salga PY_VAR0
    #Necesito un GET() del contenido de la variable. Sino NO funciona
    test = entry_content.get()

    #----------LOGIN-VERIFICATION -----------
    if test == 5388914:
        #tkMessageBox.showinfo("Rest","Bienvenido Juan!"+pss)
        #password.set(test)
        new_window()
    else:
        tkMessageBox.showinfo("DEMON SLAYER CORPS","We know you are DOMA´s follower!!!. You better get da fuck out here, or we will rip the shit out you right now!")

    #Como es una caja de texto , cada vez que paso una targeta crea una linea nueva
    #Tengo que borrar cada linea pq sino se acumulan
    entry.delete('1.0', END)
    #Tambien tengo que borra el contenido que tengo asignado del ENTRY
    entry_content.set()

class FlatButton(Button):
    # INIT siempre es el primer metodo de una clase.
    #El mas importante es el método constructor;  inicializar los atributos del objeto creado a partir  de la clase que lo posea.
    # Le dice al interprete de Python que debe de asignarle los argumentos que nosotros le pasamos

    # El método __init__ NO RETORNA NINGÚN DATO Y ES OPCIONAL.
    # No retorna ningún dato significa que a diferencia de otros métodos este no puede retornar valores luego de ejecutado.
    #el método __init__() puede tener argumentos para mayor flexibilidad.
    #En ese caso, los argumentos que se pasen al operador de instanciación de la clase van a parar al método __init__()

    # El primer argumento de un método se llama self (uno mismo).
    # Defino los atributos que deeso que tenga
    def __init__(self, master=None, cnf=None, **kw):
        Button.__init__(self, master, cnf, **kw)

        self.config(
            compound=TkC.TOP,
            relief=TkC.FLAT,
            bd=0,
            # Con esto cambio la info del ultimo boton con toda la Info
            #Lo pongo en blanco para poder poner imagenes con transparencia

            bg="#fafafa",  #
            fg="white",
            activebackground="#fafafa",  #
            activeforeground="white",
            highlightthickness=0
        )

    def set_color(self, color):
        self.configure(
            bg=color,
            fg="white",
            activebackground=color,
            activeforeground="white"
        )
#--------------------------------------------------------
#--------       PIMENU     -----------------------------
#--------------------------------------------------------
"""
Para crear una clase recurrimos a la expresión class seguida del nombre de la clase y
entre paréntesis la clase de la cual hereda (una clase puede recibir atributos y métodos de otra).
Al momento de crear una clase si este parámetro entre paréntesis no se declara;
la clase automáticamente heredara de Object (que es una clase predefinida osea existente en el propio lenguaje por defecto.)
"""
class PiMenu(Frame):

    # Estos son atributos que van a compartir todos los objetos de esta clase.
    framestack = []
    icons = {}
    path = ''
    lastinit = 0
    # INIT siempre es el primer metodo de una clase.
    #El mas importante es el método constructor;  inicializar los atributos del objeto creado a partir  de la clase que lo posea.
    # Le dice al interprete de Python que debe de asignarle los argumentos que nosotros le pasamos

    # El método __init__ NO RETORNA NINGÚN DATO Y ES OPCIONAL.
    # No retorna ningún dato significa que a diferencia de otros métodos este no puede retornar valores luego de ejecutado.
    #el método __init__() puede tener argumentos para mayor flexibilidad.
    #En ese caso, los argumentos que se pasen al operador de instanciación de la clase van a parar al método __init__()

    # El primer argumento de un método se llama self (uno mismo).
    # Defino los atributos que deeso que tenga
    def __init__(self, parent):

        Frame.__init__(self, parent, background="black")
        self.parent = parent

        self.pack(fill=TkC.BOTH, expand=1)

        self.path = os.path.dirname(os.path.realpath(sys.argv[0]))

        self.initialize()
        # ============================================================
        # ============================================================
        # ==================   Variables PRUEBA PRODUCTOS    =========
        # ============================================================
        # ============================================================
        #Me guarda el numero de factura que genero aleatoriamente
        self.PaymentRef = StringVar()
        # Número de referencia
        x =  random.randint(10034, 699812)
        randomRef= str(x)
        self.PaymentRef.set("XIANG"+randomRef)
        # ============================================================
        # ============================================================
        # ==================   Variables factura             =========
        # ============================================================
        # ============================================================
        #Fecha
        self.dateRef = StringVar()
        self.subTotal = StringVar()
        self.totalP = StringVar()
        self.totalIva = StringVar()

        # ===========   Variables SET  ===============
        #Inicializo la variable con la fecha actual
        self.dateRef.set(time.strftime("%d/%m/%y"))

        # ============================================================
        # ============================================================
        # ==================   Variables Orden               =========
        # ============================================================
        # ============================================================
        #Inicializo el contador en 1 por defecto. Obvio que minimo es un producto
        self.count = 1
        #Esta es la variable que me guarda el resultado del contador
        # le pongo un valor por defecto de 1. Pero es un string , por eso el contador tiene que estar en 1
        # Reseteo la variable cada vez que se selecciona
        self.var = StringVar(value='1')

        #---------Ingridients -----------------------
        self.deleteIng = []
        #Este array lo utilizo dentro de def order() para mostrar los ingredientes del Producto
        #Lo borro cada vez que salgo o le doy back.
        self.showIng = []
        self.confirmedIngredients = []

        self.confirmedItems = []

        # About the price
        self.confirmedPrice = []
        self.totalPrice = []

        self.confirmedQuantity = []
        self.confirmedLabels = []

        self.confirmedAll = []


        # ============================================================
        # ============================================================
        # ==================   RESET YAML FILES              =========
        # ============================================================
        # ============================================================
        #Cuando comienza el programa borra todos los archivos para empezar de cero.
        if os.path.exists(self.path + '/qtyXprice.yaml'):
            os.remove(self.path + '/qtyXprice.yaml')

        if os.path.exists(self.path + '/orderConfirmed.yaml'):
            os.remove(self.path + '/orderConfirmed.yaml')

        if os.path.exists(self.path + '/qtyXprice.yaml'):
            os.remove(self.path + '/qtyXprice.yaml')

        if os.path.exists(self.path + '/qty.yaml'):
            os.remove(self.path + '/qty.yaml')

        if os.path.exists(self.path + '/labels.yaml'):
            os.remove(self.path + '/labels.yaml')

        if os.path.exists(self.path + '/ing.yaml'):
            os.remove(self.path + '/ing.yaml')

    def Login_System(self):

        self.initialize()
        #return tkMessageBox.showinfo("Restaurante Clan XIANG"," Bienvenido!")
            #self.username.set("")
        #self.password.set("")

    def initialize(self):
        """
        (re)load the the items from the yaml configuration and (re)init
        the whole menu system

        :return: None
        """
        with open(self.path + '/config_pi_menu.yaml', 'r') as f:
            doc = yaml.load(f)

        self.lastinit = os.path.getmtime(self.path + '/config_pi_menu.yaml')

        if len(self.framestack):
            self.destroy_all()
            self.destroy_top()
        self.show_items(doc)

    def has_config_changed(self):
        """
        Checks if the configuration has been changed since last loading

        :return: Boolean
        """
        return self.lastinit != os.path.getmtime(self.path + '/config_pi_menu.yaml')

    def show_items(self, items, upper=None):
        """
        Creates a new page on the stack, automatically adds a back button when there are
        pages on the stack already

        :param items: list the items to display
        :param upper: list previous levels' ids
        :return: None
        """

        if upper is None:
            upper = []
        num = 0

        # create a new frame
        # aqui cambio el color de frame que queda detras de los iconos y botones
        wrap = Frame(self, bg="black")

        if len(self.framestack):
            # when there were previous frames, hide the top one and add a back button for the new one
            self.hide_top()
            #--------- BACK ---------------------------
            back = FlatButton(
                wrap,
                text='',
                #Le cambio el tañaño a la letra del boton de atras
                font=('Helvetica', '50'),
                image=self.get_icon("arrow.left"),
                command=self.go_back,
            )
            back.set_color("#054d08")  # green
            back.grid(row=0, column=0, padx=1, pady=1, sticky=TkC.W + TkC.E + TkC.N + TkC.S)
            back.config(bd=8, relief=RAISED)
            back.config(bg='dark green', fg='white')

            # ------------- PUNTOS ---------------------------
            admin = FlatButton(
                wrap,
                text='Admin',
                #Le cambio el tañaño a la letra del boton de atras
                font=('Helvetica', '20'),
                #image=self.get_icon("arrow.left"),
                command=self.admin,
            )
            admin.set_color("#054d08")  # green
            admin.grid(row=4, column=1, padx=10, pady=10, sticky=TkC.W + TkC.E + TkC.N + TkC.S)
            admin.config(bd=8)
            admin.config(bg='dark green', fg='white')
            #-----------FACTURA -------------------------

            #En caso que no haya ningun producto en la cesta  muestra otro boton
            if os.path.exists(self.path + '/orderConfirmed.yaml'):

                bill = FlatButton(
                    wrap,
                    text='Mi factura',
                    #Le cambio el tañaño a la letra del boton de atras
                    font=('Helvetica', '30', 'bold'),
                    #image=self.get_icon("bill"),
                    command=self.show_bill,
                )
                bill.set_color("#054d08")  # green
                bill.grid(row=4, column=0, padx=10, pady=10, sticky=TkC.W + TkC.E + TkC.N + TkC.S)
                bill.config(bd=8, relief=RAISED)
                bill.config(bg='#6088d1', fg='white')
            else:
                help = FlatButton(
                    wrap,
                    text='Ayuda',
                    #Le cambio el tañaño a la letra del boton de atras
                    font=('Helvetica', '30','bold'),
                    #image=self.get_icon("bill"),
                    #command=self.show_bill,

                )
                help.set_color("#6b4f18")
                help.grid(row=4, column=0, padx=10, pady=10, sticky=TkC.W + TkC.E + TkC.N + TkC.S)
                help.config(bd=8, relief=RAISED, fg='white')
            num += 1

        # add the new frame to the stack and display it
        self.framestack.append(wrap)

        self.show_top()

        # calculate tile distribution
        allitems = len(items) + num
        rows = floor(sqrt(allitems))
        cols = ceil(allitems / rows)

        # make cells autoscale
        for x in range(int(cols)):
            wrap.columnconfigure(x, weight=1)
        for y in range(int(rows)):
            wrap.rowconfigure(y, weight=1)

        # display all given buttons
        for item in items:
            act = upper + [item['name']]
            # De esta forma tengo la variable de NAME del archivo de YAML de forma global
            self.name = item['name']
            # De esta forma tengo la variable de PRICE del archivo de YAML de forma global
            # Ahora puedo llamar la variable desde los metodos
            self.label= item['label']
            #Asigno el precio de cada articulo a una variable global
            self.price= item['price']
            #Asigno el precio de cada articulo a una variable global
            self.points= item['points']

            if 'icon' in item:
                image = self.get_icon(item['icon'])

            elif 'image' in item:
                image = self.get_image(item['image'])

            else:
                image = self.get_icon('scrabble.' + item['label'][0:1].lower())

            btn = FlatButton(
                wrap,
                text=item['label'],
                font=('Helvetica', '25','bold'),
                image=image,
            )

            labelTest = Label(
                wrap,
                text='Testing',
                font=('Helvetica', '25','bold')
            )
            labelTest.configure(fg='black')

            if 'items' in item:
                # this is a deeper level
                #btn.configure(command=lambda act=act, item=item: self.show_items(item['items'], act),
                              #text=item['label'] + '…')
                btn.configure(command=lambda act=act, item=item: self.show_items(item['items'], act),
                              text=item['label'],wraplength=200,font=('Arial', '20','bold'))
                btn.set_color("#2b5797")  # dark-blue
            else:
                #btn.configure(command=lambda act=act: self.go_action(act), )
                btn.configure(command=lambda act=act: self.order(),justify=LEFT,wraplength=550,font=('Arial', '20','bold'),fg ='red',
                                        text=item['description']+'\n'
                                        +'\n'+'Precio: € '+str(item['price'])
                                        +'   '+'   '+'Unidades: '+item['units']
                                        +'\n'+'Puntos: '+str(item['points']))

            if 'color' in item:
                btn.set_color(item['color'])

            # add buton to the grid
            btn.grid(
                row=int(floor(num / cols)),
                column=int(num % cols),
                padx=1,
                pady=1,
                sticky=TkC.W + TkC.E + TkC.N + TkC.S
            )
            num += 1

    def Rest(self):
        #self.username.set("")
        self.password.set("")
        self.txtPassword.focus()

    def iExit(self):
        self.iExit = tkMessageBox.askyesno("Restaurante Clan XIANG", "Seguro que desea cerrar el programa?")
        if self.iExit > 0:
            self.master.destroy()
        else:
            command = self.new_window
            return

    def get_icon(self, name):
        """
        Loads the given icon and keeps a reference

        :param name: string
        :return:
        """
        if name in self.icons:
            return self.icons[name]

        ico = self.path + '/ico/' + name + '.png'
        if not os.path.isfile(ico):
            ico = self.path + '/ico/' + name + '.gif'
            if not os.path.isfile(ico):
                ico = self.path + '/ico/adobe.acrobat.gif'

        self.icons[name] = PhotoImage(file=ico)
        return self.icons[name]

    #--------- PRODUCT IMAGE --------------------
    def get_image(self, name):

            #if 'icon' in item:
                #image = self.get_icon(item['icon'])
            #else:
                #image = self.get_icon(item['image'])
        if name in self.icons:
            return self.icons[name]
        #----------------------------------------------
        #           FOLDERS
        #----------------------------------------------
        #Aqui escribo la ruta del folder con las imagenes
        #De esta forma puedo clasificar imagenes por folders
        #NO tener todas en una carpeta porque so muchas
        ico = self.path + '/img/' + name + '.gif'
        if not os.path.isfile(ico):
            ico = self.path + '/img/' + name + '.png'
            if not os.path.isfile(ico):
                ico = self.path + '/img/entrante/' + name + '.png'
                if not os.path.isfile(ico):
                    ico = self.path + '/img/desert/' + name + '.png'
                    if not os.path.isfile(ico):
                        ico = self.path + '/img/dim-sum/' + name + '.png'
                        if not os.path.isfile(ico):
                            ico = self.path + '/img/coffe/' + name + '.png'
                            if not os.path.isfile(ico):
                                ico = self.path + '/img/drinks/' + name + '.png'
                                if not os.path.isfile(ico):
                                    ico = self.path + '/img/drinks/beer/' + name + '.png'
                                    if not os.path.isfile(ico):
                                        ico = self.path + '/img/drinks/licores/' + name + '.png'
                                        if not os.path.isfile(ico):
                                            ico = self.path + '/img/drinks/soda/' + name + '.png'
                                            if not os.path.isfile(ico):
                                                ico = self.path + '/img/drinks/wine/' + name + '.png'
                                                if not os.path.isfile(ico):
                                                    ico = self.path + '/img/drinks/licores/ginebra/' + name + '.png'
                                                    if not os.path.isfile(ico):
                                                        ico = self.path + '/img/drinks/licores/ron/' + name + '.png'
                                                        if not os.path.isfile(ico):
                                                            ico = self.path + '/img/drinks/licores/tequila/' + name + '.png'
                                                            if not os.path.isfile(ico):
                                                                ico = self.path + '/img/drinks/licores/wiskey/' + name + '.png'
                                                                if not os.path.isfile(ico):
                                                                    ico = self.path + '/img/meat/' + name + '.png'
                                                                    if not os.path.isfile(ico):
                                                                        ico = self.path + '/img/sushi/' + name + '.png'
                                                                        if not os.path.isfile(ico):
                                                                            ico = self.path + '/img/tallarines/' + name + '.png'
                                                                            if not os.path.isfile(ico):
                                                                                ico = self.path + '/img/soup/' + name + '.png'
                                                                                if not os.path.isfile(ico):
                                                                                    ico = self.path + '/img/rice/' + name + '.png'
                                                                                    if not os.path.isfile(ico):
                                                                                        ico = self.path + '/img/misellaneous/' + name + '.png'
                                                                                        if not os.path.isfile(ico):
                                                                                            ico = self.path + '/img/sushi/nigiri/' + name + '.png'
                                                                                            if not os.path.isfile(ico):
                                                                                                ico = self.path + '/img/sushi/maki/' + name + '.png'
                                                                                                if not os.path.isfile(ico):
                                                                                                    ico = self.path + '/img/sushi/tartar/' + name + '.png'
                                                                                                    if not os.path.isfile(ico):
                                                                                                        ico = self.path + '/img/sushi/sashimi/' + name + '.png'
                                                                                                        if not os.path.isfile(ico):
                                                                                                            ico = self.path + '/img/sushi/california/' + name + '.png'
                                                                                                            if not os.path.isfile(ico):
                                                                                                                ico = self.path + '/img/sushi/temaki/' + name + '.png'
                                                                                                                if not os.path.isfile(ico):
                                                                                                                    ico = self.path + '/img/sushi/urimaki/' + name + '.png'
                                                                                                                    if not os.path.isfile(ico):
                                                                                                                        ico = self.path + '/img/sushi/bandejas-sushi/' + name + '.png'
                                                                                                                        if not os.path.isfile(ico):
                                                                                                                            ico = self.path + '/img/drinks/wine/tinto/' + name + '.png'
                                                                                                                            if not os.path.isfile(ico):
                                                                                                                                ico = self.path + '/img/drinks/wine/blanco/' + name + '.png'
                                                                                                                                if not os.path.isfile(ico):
                                                                                                                                    ico = self.path + '/img/drinks/wine/Rosado/' + name + '.png'
                                                                                                                                    if not os.path.isfile(ico):
                                                                                                                                        ico = self.path + '/img/drinks/wine/copas/' + name + '.png'
                                                                                                                                        if not os.path.isfile(ico):
                                                                                                                                            ico = self.path + '/img/drinks/wine/tinto/Rioja/' + name + '.png'
                                                                                                                                            if not os.path.isfile(ico):
                                                                                                                                                ico = self.path + '/img/drinks/wine/tinto/rivera-duero/' + name + '.png'
                                                                                                                                                if not os.path.isfile(ico):
                                                                                                                                                    ico = self.path + '/img/vegetales/' + name + '.png'
                                                                                                                                                    if not os.path.isfile(ico):
                                                                                                                                                        ico = self.path + '/img/meat/cerdo/' + name + '.png'
                                                                                                                                                        if not os.path.isfile(ico):
                                                                                                                                                            ico = self.path + '/img/meat/ternera/' + name + '.png'
                                                                                                                                                            if not os.path.isfile(ico):
                                                                                                                                                                ico = self.path + '/img/meat/pollo/' + name + '.png'
                                                                                                                                                                if not os.path.isfile(ico):
                                                                                                                                                                    ico = self.path + '/img/meat/mariscos/' + name + '.png'
                                                                                                                                                                    if not os.path.isfile(ico):
                                                                                                                                                                        ico = self.path + '/img/meat/pato/' + name + '.png'
                                                                                                                                                                        if not os.path.isfile(ico):
                                                                                                                                                                            ico = self.path + '/img/points/' + name + '.png'




        self.icons[name] = PhotoImage(file=ico)
        return self.icons[name]

    # -------- ALLERGENICOS IMAGE ----------------
    def get_allergenios(self, name):

            #if 'icon' in item:
                #image = self.get_icon(item['icon'])
            #else:
                #image = self.get_icon(item['image'])
        if name in self.icons:
            return self.icons[name]
        #----------------------------------------------
        #           FOLDERS
        #----------------------------------------------
        #Aqui escribo la ruta del folder con las imagenes
        #De esta forma puedo clasificar imagenes por folders
        #NO tener todas en una carpeta porque so muchas
        ico = self.path + '/allergenicos/' + name + '.gif'
        if not os.path.isfile(ico):
            ico = self.path + '/allergenicos/' + name + '.png'

        self.icons[name] = PhotoImage(file=ico)
        return self.icons[name]
    # -------- ALLERGENICOS IMAGE ----------------

    def hide_top(self):
        """
        hide the top page
        :return:
        """
        self.framestack[len(self.framestack) - 1].pack_forget()

    def show_top(self):
        """
        show the top page
        :return:
        """
        self.framestack[len(self.framestack) - 1].pack(fill=TkC.BOTH, expand=1)

    def destroy_top(self):
        """
        destroy the top page
        :return:
        """
        self.framestack[len(self.framestack) - 1].destroy()
        self.framestack.pop()

    def destroy_all(self):
        """
        destroy all pages except the first aka. go back to start
        :return:
        """
        while len(self.framestack) > 1:
            self.destroy_top()

    def shut_down(self):

            self.quit()

    def go_action(self, actions):
        """
        execute the action script
        :param actions:
        :return:
        """
        # hide the menu and show a delay screen
        self.hide_top()
        delay = Frame(self, bg="#2d89ef")
        delay.pack(fill=TkC.BOTH, expand=1)
        label = Label(delay, text="Agregando producto a su mesa ..", fg="white", bg="#630603", font="Sans 30")
        label.pack(fill=TkC.BOTH, expand=1)
        self.parent.update()

        # excute shell script
        subprocess.call([self.path + '/pimenu.sh'] + actions)

        # remove delay screen and show menu again
        delay.destroy()
        #.destroy_all()
        self.show_top()

    def go_back(self):
        """
        destroy the current frame and reshow the one below, except when the config has changed
        then reinitialize everything
        :return:
        """
        if self.has_config_changed():
            self.initialize()
        else:
            self.destroy_top()
            self.show_top()
            #Pongo en cero el array que muestra los ingredientes para que no se acumulen.
            self.showIng = []

    def kellner(self):

        """
        execute the action script
        :param actions:
        :return:
        """
        # hide the menu and show a delay screen
        self.hide_top()
        delay1 = Frame(self, bg="#2d89ef")
        delay1.pack(fill=TkC.BOTH, expand=1)


        label1 = Label(delay1, fg="white", bg="#630603", font="Sans 30")
        label1.pack(fill=TkC.BOTH)

        back = FlatButton(
                        label1,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('Helvetica', '30'),
                        image=self.get_icon("arrow.left"),
                        command=self.go_back
                    )
        back.set_color("#054d08")  # green
        back.pack(fill=TkC.BOTH)

        image = Image.open("cover.gif")
        image = image.resize((500, 415), Image.ANTIALIAS)

        photo= ImageTk.PhotoImage(image)

        panel = Label(label1, image = photo)
        panel.image = photo
        panel.pack(pady = 5, padx = 5)

        self.framestack.append(delay1)
    #------- COUNTER --------------------
    def up(self):
        self.count += 1 #function to increase the count by one
        self.var.set(self.count)
    def down(self):
        self.count -= 1 #function to increase the count by one
        self.var.set(self.count)

    #-------- REMOVE INGREDIENT ----------
    def remove_ingredient(self):
        selected_ingredient = self.lb.curselection()

        for x in selected_ingredient[::-1]:
            self.lb.delete(selected_ingredient)

    #-------- PLACE ORDER -----------------
    def order(self):
        # hide the menu and show a delay screen
        self.hide_top()

        #Super importante traer el numero de plato que escojimos
        #Para ello le asignamos el valor de self.name a una variable local
        menuName = self.name

        delay1 = Frame(self, relief=RAISED, borderwidth=3)
        delay1.pack(fill=TkC.BOTH, expand=1)

        #-----------------------------
        #---------LABELS--------------
        #-----------------------------
        labelB = Label(delay1, fg="white", font="Sans 30")
        labelB.config(bg = "white")
        labelB.pack(fill=TkC.BOTH, side=BOTTOM, pady = 5, padx = 5)

        labelT = Label(delay1, fg="white", font="Sans 30")
        labelT.config(bg = "white")
        labelT.pack(fill=TkC.BOTH, side=TOP, pady = 5, padx = 5)

        labelL = Label(delay1, fg="white", font="Sans 30")
        labelL.pack(side=LEFT, pady = 5, padx = 5)

        labelL1 = Label(delay1, fg="white", font="Sans 30")
        labelL1.pack(side=LEFT, pady = 5, padx = 5)

        labelR = Label(delay1, fg="white", font="Sans 30")
        labelR.pack(side=RIGHT, pady = 5, padx = 5)

        labelRT = Label(labelR, fg="white", font="Sans 30")
        labelRT.pack(side=TOP, pady = 5, padx = 5)

        #------------------------------
        #---------NOMBRE del Producto---
        #------------------------------
        nombre= Label(labelT, text = self.label,font=('Helvetica', '25','bold'),bg = '#be1623', fg = 'white')
        nombre.pack(fill=TkC.X, side=TOP, pady = 1, padx = 1)
        #------------------------------
        #---------COUNTER--------------
        #------------------------------
        title = Label(labelRT, font=('Helvetica', '20', 'bold'), text= "Cuántos deseas?")
        title.pack(side=TOP, pady = 5, padx = 5)
        #self.var lo declaro en INIT para que sea global
        #Resultado de self.init esta dentro de las funciones de UP, DOWN
        counter = Entry(labelRT, width=4, font=('arial', 16, 'bold'), textvariable=self.var, bd=10, insertwidth=2, justify='center')
        #Hago el BIND a la funcion
        counter.bind("<Button-1>", self.down)
        counter.config(bg = "#fafafa", font=("Courier", 40), width = 4)
        counter.pack(side=LEFT, pady = 5, padx = 5)

        #-----------------------------------------
        #------------ BOTONES --------------------
        #----------------------------------------
        minus = FlatButton(
                        labelRT,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('Helvetica', '30'),
                        image=self.get_image("minus"),
                        command=self.down
                    )
        minus.set_color("#7b474b")
        minus.config(bd=8, relief=RAISED)
        minus.pack(side=LEFT)

        plus = FlatButton(
                        labelRT,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('Helvetica', '30'),
                        image=self.get_image("plus"),
                        command=self.up
                    )
        plus.set_color("#006634")
        plus.config(bd=8, relief=RAISED)
        plus.pack(side=LEFT)

        back = FlatButton(
                        labelR,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('Helvetica', '30'),
                        image=self.get_image("delete"),
                        command=self.go_back
                    )
        back.set_color("#be1623")
        back.config(bd=8, relief=RAISED)
        #back.config(bg='dark green', fg='white')
        back.pack(side=BOTTOM, fill=X)


        confirm = FlatButton(
                        labelR,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('Helvetica', '30'),
                        image=self.get_image("check"),
                        command=self.order_confirmed
                    )
        confirm.set_color("#006634")
        confirm.config(bd=8, relief=RAISED)
        #confirm.config(bg='dark green', fg='white')
        confirm.pack(side=BOTTOM, fill=X)

        #-----------------------------------------
        #---------IMAGE ALLERGENICOS--------------
        #-----------------------------------------
        with open(self.path + '/allergenicos.yaml', 'r') as f:
            doc1 = yaml.load(f)
        self.lastinit = os.path.getmtime(self.path + '/allergenicos.yaml')

        # display all given buttons
        for d in doc1:
            #Si el nombre en la lista coicide con el que nos llega...
            if d['name'] == self.name :
                for i in d['items']:
                    image = Image.open(self.path + '/allergenicos/' + i['image'] + '.png')
                    image = image.resize((100, 100), Image.ANTIALIAS)

                    photo= ImageTk.PhotoImage(image)

                    panel = Label(labelB, image = photo)
                    panel.image = photo
                    panel.pack(side=LEFT, pady = 5, padx = 5)

        #-----------------------------------------
        #-----------LIST -------------------------
        #-----------------------------------------
        ing= Label(labelL, text = "Elimine ingrediente",font=('Helvetica', '20','bold'))
        ing.pack(fill=TkC.X, side=TOP, pady = 1, padx = 1)
                    #-------- YAML DOC -----------
        # Abro el doc YAML con todos los ingredientes
        with open(self.path + '/ingredients.yaml', 'r') as f:
            doc = yaml.load(f)
        # Me aseguro de cargar todos los cambios al documento
        self.lastinit = os.path.getmtime(self.path + '/ingredients.yaml')

                    #---- Scroll Bar -------------
        scrollbar = Scrollbar(labelL)
        scrollbar.pack( side = RIGHT, fill = Y )

                    #------- List ---------------
        #El selectmode extended me deja seleccionar varios items al mismo tiempo
        self.lb = Listbox(labelL,font=('Helvetica', '20'), selectmode=EXTENDED, yscrollcommand = scrollbar.set)

        for e in doc:
            #Si NAME del elemento YAML es igual al que nos llega como self.name (Parametro llega desde show_items)
            if e['name'] == self.name :
                # Entonces agrego cada Item del YAML al array self.showIng (Inicialicé en el INIT)
                for i in e['items']:
                    self.showIng.append(i['name'])

        for w in self.showIng:
            self.lb.insert(0,w)

        self.lb.pack(fill=TkC.Y, side=LEFT, pady = 5, padx = 5)

                #----------- Buttons -------------
        remove = FlatButton(
                        labelL1,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('Helvetica', '30'),
                        image=self.get_image("minus"),
                        command=self.remove_ingredient
                    )
        remove.set_color("#7b474b")
        remove.config(bd=8, relief=RAISED)
        remove.pack(side=TOP)
        #---------APPEND FRAME to SATACK--------------
        self.framestack.append(delay1)

    def order_confirmed(self):
        # hide the menu and show a delay screen
        self.hide_top()

        #Super importante traer el numero de plato que escojimos
        #Para ello le asignamos el valor de self.name a una variable local
        menuName = self.name
        counter = self.count
        price = self.price
        label = self.label
        ingredients = self.deleteIng

        self.confirmedLabels.append(label)

        # Multiplico la cantidad por el precio y lo guardo en un nuuevo array
        self.confirmedPrice.append(price)
        self.confirmedQuantity.append(counter)
        #Multiplico la qty que me llega por el precio que me llega
        self.totalPrice.append(round((price*counter),2))


        self.confirmedItems.append(menuName)
        self.confirmedIngredients.append(ingredients)

        items = [{'name':self.confirmedItems},{'qty':self.confirmedQuantity},{'ing':self.confirmedIngredients},{'price':self.confirmedPrice}]

        var = self.confirmedAll.append(items)

        # Obtengo los valores de los arreglos en una variable para poder interactuar y exportar a YAML
        var1 = self.confirmedAll

        #-------------------------------------
        #---------- SAVE in YAML -------------
        #-------------------------------------
        for g in var1:
            with open(self.path + '/orderConfirmed.yaml', 'w') as f:
                yaml.dump(g,f)

        #Creo un archivo YAML aparte para los precio y poder trabajarlo por separado
        for b in [self.confirmedPrice]:
            with open(self.path + '/prices.yaml', 'w') as f:
                yaml.dump(b,f)

        #Creo un archivo YAML aparte para los precio y poder trabajarlo por separado
        for k in [self.totalPrice]:
            with open(self.path + '/qtyXprice.yaml', 'w') as f:
                yaml.dump(k,f)

        #Creo un archivo YAML aparte para las cantidades y poder trabajarlo por separado
        for c in [self.confirmedQuantity]:
            with open(self.path + '/qty.yaml', 'w') as f:
                yaml.dump(c,f)
        #Creo un archivo YAML aparte para los nombres y poder trabajarlo por separado
        for d in [self.confirmedLabels]:
            with open(self.path + '/labels.yaml', 'w') as f:
                yaml.dump(d,f)
        #Creo un archivo YAML aparte para los ingredientes y poder trabajarlo por separado
        for d in [self.confirmedIngredients]:
            with open(self.path + '/ing.yaml', 'w') as f:
                yaml.dump(d,f)

        delay1 = Frame(self, relief=RAISED, borderwidth=3)
        delay1.config(bg = "#C3DBE2")
        delay1.pack(fill=TkC.BOTH, expand=1)

        labelB = Message(delay1, text= "Producto agregado a su order!", fg="white", font="Sans 40")
        labelB.config(bg = "red")
        labelB.pack(fill=TkC.BOTH, side= TOP, pady = 5, padx = 5)

        delay1.after(3000, delay1.destroy)

        self.go_back()

    def show_bill(self):
        # hide the menu and show a delay screen
        self.hide_top()

        # Llamo a los archivos de YAML para leer las variables
        with open(self.path + '/orderConfirmed.yaml', 'r') as f:
            meat = yaml.load(f)

        with open(self.path + '/qtyXprice.yaml', 'r') as f:
            pasta = yaml.load(f)

        with open(self.path + '/qty.yaml', 'r') as f:
            qty = yaml.load(f)

        with open(self.path + '/labels.yaml', 'r') as f:
            plato = yaml.load(f)

        with open(self.path + '/ing.yaml', 'r') as f:
            ing = yaml.load(f)

        #----------DENIFIR FRAME ---------------
        main = Frame(self, relief=RAISED, borderwidth=3)
        main.config(bg = "#fafafa")
        main.pack(fill=TkC.BOTH, expand=1)
        # up/down
        up = Frame(main,relief="raise")
        up.pack(fill=TkC.BOTH, side=TOP)

        down = Frame(main,relief="raise")
        down.pack(fill=TkC.BOTH, side=BOTTOM)
        # left
        l = Frame(main, relief="raise")
        l.pack(fill=TkC.BOTH, side=LEFT)

        # right
        r = Frame(main, relief="raise")
        r.pack(fill=TkC.BOTH, side=RIGHT)
        self.framestack.append(main)

        # ------------------------------------------
        #-------- LISTA DE PRODUCTOS ----------------
        l1 = Listbox(l)
        for d in plato:
            l1.insert(0,d)
            #for g in ing:
                #l1.insert(1,g)
        l1.configure(font=('arial', 18))
        l1.pack(fill=TkC.BOTH,side=LEFT)

        l2 = Listbox(l)
        for d in qty:
            l2.insert(0,d)
        l2.configure(width =5, font=('arial', 18), justify=CENTER)
        l2.pack(fill=TkC.BOTH,side=LEFT)

        l3 = Listbox(l)
        for d in pasta:
            l3.insert(0,d)
        l3.configure(width =7, font=('arial', 18), justify=CENTER)
        l3.pack(fill=TkC.BOTH,side=LEFT)

        ref = Label(up, font=('arial', 16), fg="red", text="Número de factura", bd=16, justify='center')
        ref.grid(row=0, column=0)
        ref = Entry(up, font=('arial', 16, 'bold'), textvariable=self.PaymentRef, bd=10, insertwidth=2, justify='center')
        ref.grid(row=0, column=1)

        empty0= Label(up, font=('arial', 16, 'bold'), text=" ")
        empty0.grid(row=0, column=2)

        datel = Label(up, font=('arial'), text="Fecha  ")
        datel.grid(row=0, column=3)
        date = Label(up, font=('arial', 16), textvariable=self.dateRef)
        date.grid(row=0, column=4)

        # ===  Número de referencia ====

        pay = FlatButton(
                        down,
                        text= "Pagar",
                        width=12,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('arial', 35, 'bold'),
                        #image=self.get_icon("money"),
                        command=self.payment
                    )
        pay.config(bg = "#23397d", fg = "white", bd=8, relief=RAISED)
        pay.pack(fill=TkC.BOTH, side= RIGHT, pady = 5, padx = 5)

        back = FlatButton(
                        down,
                        text= "Atrás",
                        width=8,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('arial', 25, 'bold'),
                        #image=self.get_icon("arrow.left"),
                        command=self.go_back
                    )
        back.config(bg = "green", fg = "white")
        back.pack(fill=TkC.BOTH, side= LEFT, pady = 5, padx = 5)


        points = FlatButton(
                        down,
                        text= "Puntos",
                        width=8,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('arial', 25, 'bold'),
                        #image=self.get_icon("money"),
                        command=self.go_back
                    )
        points.config(bg = "blue", fg = "white")
        points.pack(fill=TkC.BOTH, side= LEFT, pady = 5, padx = 5)

        # ==========================Total Payment Info======

        subTotal = Label(r, font=('arial', 16, 'bold'), text="Sub total", bd=16, justify='left')
        subTotal.grid(row=2, column=0)
        subTotal = Entry(r, width=7, font=('arial', 16, 'bold'), textvariable=self.subTotal, bd=10, insertwidth=2, justify='center')
        subTotal.grid(row=2, column=1)
        # --------------
        vat = Label(r, font=('arial', 16, 'bold'), text="IVA 21% ", bd=16, justify='left')
        vat.grid(row=3, column=0)
        vat1 = Entry(r, width=7, font=('arial', 16, 'bold'), textvariable=self.totalIva, bd=10, insertwidth=2, justify='center')
        vat1.grid(row=3, column=1)

        empty = Label(r, font=('arial', 16, 'bold'), text="_____________", bd=16, justify='left')
        empty.grid(row=4, column=0)
        empty1 = Label(r, font=('arial', 16, 'bold'), text="", bd=16, justify='left')
        empty1.grid(row=5, column=0)

        total = Label(r, font=('arial', 30, 'bold'), text="Total   €", bd=16, justify='left')
        total.grid(row=7, column=0)
        total = Entry(r, width=7, font=('arial', 30, 'bold'), textvariable=self.totalP, bd=10, insertwidth=1, justify='center')
        total.grid(row=7, column=1)
        self.preis()

    def preis(self):

        num = 0
        for l in self.totalPrice:
            num += l
        #Solo quiero dos decimales. Utilizo ROUND
        subtotal = round(num,2)

        #Multiplico por el 21% del iva
        #Solo quiero dos decimales. Utilizo ROUND
        totalIva = round(((subtotal*21)/100),2)

        #Solo quiero dos decimales. Utilizo ROUND
        total = round((subtotal+totalIva),2)

        self.totalIva.set(totalIva)
        self.subTotal.set(subtotal)
        self.totalP.set(total)

    def reset(self):
        # hide the menu and show a delay screen
        self.hide_top()

        if os.path.exists(self.path + '/qtyXprice.yaml'):
            os.remove(self.path + '/qtyXprice.yaml')

        if os.path.exists(self.path + '/orderConfirmed.yaml'):
            os.remove(self.path + '/orderConfirmed.yaml')

        if os.path.exists(self.path + '/qtyXprice.yaml'):
            os.remove(self.path + '/qtyXprice.yaml')

        if os.path.exists(self.path + '/qtyXprice.yaml'):
            os.remove(self.path + '/qtyXprice.yaml')

        if os.path.exists(self.path + '/qty.yaml'):
            os.remove(self.path + '/qty.yaml')

        if os.path.exists(self.path + '/labels.yaml'):
            os.remove(self.path + '/labels.yaml')

        if os.path.exists(self.path + '/ing.yaml'):
            os.remove(self.path + '/ing.yaml')

        self.confirmedItems = []
        self.confirmedPrice = []
        self.confirmedQuantity = []
        self.confirmedIngredients = []
        self.confirmedLabels = []
        self.totalPrice = []
        self.showIng = []
        # ===========   Variables ORDEN  ===============
        #Inicializo el contador en 1 por defecto. Obvio que minimo es un producto
        self.count = 1
        #Esta es la variable que me guarda el resultado del contador
        # le pongo un valor por defecto de 1. Pero es un string , por eso el contador tiene que estar en 1
        # Reseteo la variable cada vez que se selecciona
        self.var = StringVar(value='1')

        # ===========   Variables PRUEBA PRODUCTOS  ===============
        #Me guarda el numero de factura que genero aleatoriamente
        self.PaymentRef = StringVar()
        # Número de referencia
        x =  random.randint(100000, 999999)
        randomRef= str(x)
        self.PaymentRef.set("XIANG"+randomRef)


        delay1 = Frame(self, relief=RAISED, borderwidth=3)
        delay1.config(bg = "#C3DBE2")
        delay1.pack(fill=TkC.BOTH, expand=1)

        labelB = Message(delay1, text= "Orden pagado!", fg="white", font="Sans 40")
        labelB.config(bg = "red")
        labelB.pack(fill=TkC.BOTH, side= TOP, pady = 5, padx = 5)

        delay1.after(3000, delay1.destroy)

        if len(self.framestack):
            self.destroy_all()
            self.destroy_top()

        self.initialize()

    def payment(self):
        # hide the menu and show a delay screen
        self.hide_top()

        delay1 = Frame(self, relief=RAISED, borderwidth=3)
        delay1.pack(fill=TkC.BOTH, expand=1)

        #---------LABELS--------------
        labelB = Label(delay1, fg="white", font="Sans 30")
        labelB.pack(fill=TkC.BOTH, side=BOTTOM, pady = 5, padx = 5)

        labelT = Label(delay1, fg="white", font="Sans 30")
        labelT.pack(fill=TkC.BOTH, side=TOP, pady = 5, padx = 5)

        labelL = Label(delay1, fg="white", font="Sans 30")
        labelL.pack(fill=TkC.BOTH,side=LEFT, pady = 5, padx = 5)

        labelR = Label(delay1, fg="white", font="Sans 30")
        labelR.pack(fill=TkC.BOTH,side=RIGHT, pady = 5, padx = 5)


        card = FlatButton(
                        labelR,
                        text= "Targeta",
                        width=12,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('arial', 45, 'bold'),
                        #image=self.get_icon("money"),
                        command=self.reset
                    )
        card.config(bg = "#23397d", fg = "white", bd=8, relief=RAISED)
        card.pack(fill=TkC.BOTH, expand=1, pady = 5, padx = 5)

        cash = FlatButton(
                        labelL,
                        text= "Efectivo",
                        width=8,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('arial', 45, 'bold'),
                        #image=self.get_icon("arrow.left"),
                        command=self.go_back
                    )
        cash.config(fg = "white",  bd=8, relief=RAISED)
        cash.pack(fill=TkC.BOTH, expand=1, pady = 5, padx = 5)

        back = FlatButton(
                        labelB,
                        text= "Atrás",
                        width=8,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('arial', 25, 'bold'),
                        #image=self.get_icon("arrow.left"),
                        command=self.go_back
                    )
        back.config(fg = "white",  bd=8, relief=RAISED)
        back.pack(fill=TkC.BOTH, expand=1, pady = 5, padx = 5)

        text = FlatButton(
                        labelT,
                        text= "Gana puntos realizando esta encuesta",
                        #width=8,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('arial', 30, 'bold'),
                        #image=self.get_icon("arrow.left"),
                        command=self.go_back
                    )
        text.config(bg = "green", fg = "white", bd=8, relief=RAISED)
        text.pack(fill=TkC.BOTH,expand=1, pady = 5, padx = 5)
        #---------APPEND FRAME to SATACK--------------
        self.framestack.append(delay1)

    def admin(self):
        # hide the menu and show a delay screen
        self.hide_top()

        # Llamo a los archivos de YAML para leer las variables
        #with open(self.path + '/orderConfirmed.yaml', 'r') as f:
            #meat = yaml.load(f)

        #----------DENIFIR FRAME ---------------
        main = Frame(self, relief=RAISED, borderwidth=3)
        main.config(bg = "#fafafa")
        main.pack(fill=TkC.BOTH, expand=1)

        left = Frame(main,relief="raise")
        left.pack(fill=TkC.BOTH, side=LEFT)

        right = Frame(main,relief="raise")
        right.pack(fill=TkC.BOTH, side=RIGHT)

        # ------------------------------------------
        #-------- Login/REGISTER ----------------

        login_button = FlatButton(right,
                                  text="Login",
                                  font=('arial', 25, 'bold'),
                                  width=30,
                                  command=self.login)
        login_button.config(bg = "blue", fg = "white")
        login_button.pack(fill=TkC.BOTH, side= TOP, pady = 5, padx = 5)

        register_button = FlatButton(right,
                                     text="Register",
                                     font=('arial', 25, 'bold'),
                                     width=30,
                                     command=self.register)
        register_button.config(bg = "blue", fg = "white")
        register_button.pack(fill=TkC.BOTH, side= TOP, pady = 5, padx = 5)


        start_button = Button(right, text="Return to start page",
                                 command=lambda: parent.switch_frame(StartPage))

        start_button.pack(fill=TkC.BOTH, side= TOP, pady = 5, padx = 5)

        # ------------------------------------------
        #-------- EXIT ----------------
        exit_button = FlatButton(right,
                                     text="",
                                     font=('arial', 25, 'bold'),
                                     width=30,
                                     image=self.get_image("shutdown"),
                                     #No hay necesidad de crear un funcion si lo unico que deseo es cerra la ventana
                                     #basta con cerrar la clase SELF directamente a travez de comando.
                                     command=self.quit)
        exit_button.config(bg = "white", fg = "gray")
        exit_button.pack(fill=TkC.BOTH, side= TOP, pady = 5, padx = 5)
        # ------------------------------------------
        #-------- SUPPORT ----------------
        support_button = FlatButton(right,
                                     text="",
                                     font=('arial', 25, 'bold'),
                                     width=30,
                                     image=self.get_image("support"),
                                     #No hay necesidad de crear un funcion si lo unico que deseo es cerra la ventana
                                     #basta con cerrar la clase SELF directamente a travez de comando.
                                     command=self.support)
        support_button.config(bg = "white", fg = "gray")
        support_button.pack(fill=TkC.BOTH, side= TOP, pady = 5, padx = 5)

        back = FlatButton(
            left,
            text='',
            width=150,
            image=self.get_icon("arrow.left"),
            command=self.go_back,
        )
        back.set_color("#054d08")  # green
        back.config(bd=8, relief=RAISED)
        back.config(bg='dark green', fg='white')
        back.pack(fill=TkC.BOTH, expand=1, pady = 5, padx = 5)


        self.framestack.append(main)

    def slicer(self):
        # hide the menu and show a delay screen
        self.hide_top()
        #---------------------------------------------------------#
        # --------- SET FRAME/LABELS -----------------------------#
        delay1 = Frame(self, relief=RAISED, borderwidth=3)
        delay1.pack(fill=TkC.BOTH, expand=1)

        labelL = Label(delay1, fg="white", font="Sans 30")
        labelL.pack(side=LEFT, pady = 5, padx = 5)

        labelR = Label(delay1, fg="white", font="Sans 30")
        labelR.pack(side=RIGHT, pady = 5, padx = 5)

        #---------------------------------------------------------#
        # --------- SCROLLBAR ------------------------------------#
        # Create the text widget
        load = self.path + '/points/points-1.png'
        my_image = PhotoImage(file=load)

        text_widget = Canvas(labelR,image=my_image)
        # Create a scrollbar
        # EL WIDTH me da la acchura del scroll bar
        scroll_bar = Scrollbar(labelR,orient='horizontal', width=40)
        # Pack the scroll bar
        # Place it to the right side, using tk.RIGHT
        scroll_bar.pack(side=BOTTOM,fill= BOTH)
        # Pack it into our tkinter application
        # Place the text widget to the left side
        text_widget.pack(fill=BOTH,expand=1)
        #---------------------------------------------------------#
        # --------- BACK-BOTTON ------------------------------------#
        back = FlatButton(
                        labelL,
                        text= "Atrás",
                        width=8,
                        #Le cambio el tañaño a la letra del boton de atras
                        font=('arial', 25, 'bold'),
                        #image=self.get_icon("arrow.left"),
                        command=self.go_back
                    )
        back.config(fg = "green",  bd=8, relief=RAISED)
        back.pack(side=RIGHT, expand=1, pady = 5, padx = 5)

        self.framestack.append(delay1)

    def support(self):
        # hide the menu and show a delay screen
        self.hide_top()

        # Llamo a los archivos de YAML para leer las variables
        #with open(self.path + '/orderConfirmed.yaml', 'r') as f:
            #meat = yaml.load(f)

        #----------DENIFIR FRAME ---------------
        main = Frame(self, relief=RAISED, borderwidth=3)
        main.config(bg = "#fafafa")
        main.pack(fill=TkC.BOTH, expand=1)

        top = Frame(main,relief="raise")
        top.pack(fill=TkC.BOTH, side=TOP)

        left = Frame(main,relief="raise")
        left.pack(fill=TkC.BOTH, side=LEFT)

        right = Frame(main,relief="raise")
        right.pack(fill=TkC.BOTH, side=RIGHT)

        # ------------------------------------------
        #-------- Login/REGISTER ----------------
        title = Label(top,
                                  text="Configuraciones",
                                  font=('arial', 25, 'bold'),
                                  #width=30,
                                  #command=self.login)
                                  )
        title.config(bg = "red", fg = "white")
        title.pack(fill=TkC.BOTH, side= TOP, pady = 5, padx = 5)

        config_button = FlatButton(right,
                                  text="config",
                                  font=('arial', 25, 'bold'),
                                  width=30,
                                  #command=self.login)
                                  )
        config_button.config(bg = "white", fg = "black")
        config_button.pack(fill=TkC.BOTH, side= BOTTOM, pady = 5, padx = 5)

        db_button = FlatButton(right,
                                     text="Data base",
                                     font=('arial', 25, 'bold'),
                                     width=30,
                                     #scommand=self.register)
                                     )
        db_button.config(bg = "white", fg = "black")
        db_button.pack(fill=TkC.BOTH, side= BOTTOM, pady = 5, padx = 5)
        # ------------------------------------------
        #-------- EXIT ----------------
        exit_button = FlatButton(right,
                                     text="",
                                     font=('arial', 25, 'bold'),
                                     #width=30,
                                     image=self.get_image("shutdown"),
                                     #No hay necesidad de crear un funcion si lo unico que deseo es cerra la ventana
                                     #basta con cerrar la clase SELF directamente a travez de comando.
                                     command=self.quit)
        exit_button.config(bg = "white", fg = "gray")
        exit_button.pack(fill=TkC.BOTH, side= RIGHT, pady = 5, padx = 5)
        # ------------------------------------------
        #-------- SUPPORT ----------------
        support_button = FlatButton(right,
                                     text="",
                                     font=('arial', 25, 'bold'),
                                     #width=30,
                                     image=self.get_image("support"),
                                     #No hay necesidad de crear un funcion si lo unico que deseo es cerra la ventana
                                     #basta con cerrar la clase SELF directamente a travez de comando.
                                     command=self.support)
        support_button.config(bg = "white", fg = "gray")
        support_button.pack(fill=TkC.BOTH, side= RIGHT, pady = 5, padx = 5)

        back = FlatButton(
            left,
            text='',
            width=150,
            image=self.get_icon("arrow.left"),
            command=self.go_back,
        )
        back.set_color("#054d08")  # green
        back.config(bd=8, relief=RAISED)
        back.config(bg='dark green', fg='white')
        back.pack(fill=TkC.BOTH, expand=1, pady = 5, padx = 5)


        self.framestack.append(main)
# -----------------------------------------------
#--------------- ATRIBUTES OF ROOT ------------
#
#
if len(sys.argv) > 1 and sys.argv[1] == 'fs':
    root.wm_attributes('-fullscreen', True)
root.geometry("320x240")
root.configure(bg='white')
#Esto es lo que me permite BIND el CARD a la pantalla principal de ROOT
#La targeta es leida con un ENTER key , cada vez que sea leida es como si
#si presionara la tecla de ENTER
root.bind('<Return>', checkRFidTag)
#root.bind('<key>', show)
# -----------------------------------------------
#--------------- RUN LOOP ---------------------
#
#
root.mainloop()
