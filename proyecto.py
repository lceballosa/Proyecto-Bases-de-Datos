from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont
import pymysql



class interfaz:
  
    def __init__(self, ventana):
        self.wind=ventana
        self.wind.title("Proyecto bases de datos")
        self.wind.geometry("400x300")
        self.ventana_ingreso()
        
 #Función que da la ventana para ingresar a la plataforma  
    def ventana_ingreso(self):
        self.wind.configure(background="cornflower blue")
        fontStyle = tkFont.Font(family="Lucida Grande", size=25)
        self.label= Label(ventana, text="BIENVENIDO", font= fontStyle) 
        self.label.configure(background="cornflower blue")
        self.label.grid(row= 0 , column=0, padx=50 , pady=5 )
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        frame= LabelFrame(ventana,text="Acceso base de datos", font= fontStyle)
        frame.configure(background="sky blue")
        frame.config(bd=10)
        frame.grid_propagate(False)
        frame.config(width="300", height="215")
        frame.grid(row=1, column=0, padx=50, pady=10)
        fontStyle = tkFont.Font(family="Lucida Grande", size=12)
        frame2= Label(frame,text="Usuario:", font=fontStyle)
        frame2.configure(background="sky blue")
        frame2.grid(row=4, column=4, padx=30 , pady=25)
        self.usuario=Entry(frame)
        self.usuario.focus()
        self.usuario.grid(row= 4, column=5)
        frame1= Label(frame,text="Contraseña:",font=fontStyle)
        frame1.grid(row=8, column=4)
        frame1.configure(background="sky blue")
        self.contr=Entry(frame, show="*")
        self.contr.grid(row= 8, column=5)           
        boton= ttk.Button(frame, text="Ingresar", command= self.mysqlconnect)
        boton.grid(row= 10, column=5, padx= 5, pady= 15) 
        self.frame_NoIngreso= Label(frame,text=" ", fg="red")
        self.frame_NoIngreso.grid(row= 9, column=5)
        self.frame_NoIngreso.configure(background="sky blue")            
 #Funcion que borra todo el contenido de la ventana
    def clean(self):
        list =self.wind.grid_slaves()
        for l in list:
            l.destroy()   
#Funcion que crea interfez de Ingeniero:
    def ingeniero(self):
        self.wind.configure(background="spring green")
        fontStyle = tkFont.Font(family="Lucida Grande", size=15)
        self.label= Label(self.wind, text="Seleccione la opción que desee", font=fontStyle)       
        self.label.configure(background="spring green")
        self.label.grid(row=1, column=2, padx=5, pady=15)
        self.boton1= ttk.Button(self.wind, text="Consultar Datos", command=self.consulta_datos)
        self.boton2= ttk.Button(self.wind, text="Actualizar Datos",command=self.clean)
        self.boton1.grid(row=4, column=2, padx=150, pady=45)
        self.boton2.grid(row=6, column=2,padx=150, pady=30)

#Funcion que crea interfaz de Genetista 
    def Genetista(self):
        self.wind.configure(background="coral")
        fontStyle = tkFont.Font(family="Lucida Grande", size=15)
        self.label= Label(self.wind, text="Seleccione la opción que desee", font=fontStyle)
        self.label.configure(background="coral")
        self.label.grid(row=1, column=2, padx=5, pady=15)
        self.boton1= ttk.Button(self.wind, text="Consultar Datos", command=self.consulta_datos)
        self.boton2= ttk.Button(self.wind, text="Ver Informes",command=self.clean)
        self.boton3= ttk.Button(self.wind, text="Correlacionar datos",command=self.clean)      
        self.boton1.grid(row=4, column=2, padx=150, pady=35)
        self.boton2.grid(row=6, column=2,padx=150, pady=20)
        self.boton3.grid(row=8, column=2,padx=150, pady=20)
##Funcion que crea interfaz de Administrador
    def Administrador(self):
        self.wind.configure(background="cyan")
        fontStyle = tkFont.Font(family="Lucida Grande", size=15)
        self.label= Label(self.wind, text="Seleccione la opción que desee", font=fontStyle)
        self.label.configure(background="cyan")
        self.label.grid(row=1, column=2, padx=5, pady=15)
        self.boton1= ttk.Button(self.wind, text="Consultar Datos", command=self.consulta_datos)
        self.boton2= ttk.Button(self.wind, text="Ver Informes",command=self.clean)
        self.boton3= ttk.Button(self.wind, text="Administrar Perfiles",command=self.clean)      
        self.boton1.grid(row=4, column=2, padx=150, pady=35)
        self.boton2.grid(row=6, column=2,padx=150, pady=20)
        self.boton3.grid(row=8, column=2,padx=150, pady=20)
        
#Funcion que conecta la base de datos con el IDE
    def mysqlconnect(self):
        try:
             self.base_datos= pymysql.connect(host="localhost", port=3306, user=self.usuario.get(),
             passwd=self.contr.get(), db="proyecto_bases_datos")
             user= self.usuario.get()
             self.clean()
             print("Connected")
             print(user)
             if(user=="Pacho_admin"):
                 self.Administrador()
             if(user=="Petra_genetista"):
                self.Genetista()
             if(user=="lmartinez_ingeniero"):
                self.ingeniero()         
        except:       
               print("no se pudo")
               #self.clean()
               self.frame_NoIngreso['text']='Ingrese de nuevo'
               self.usuario.delete(0,END)
               self.contr.delete(0,END)              
               return 1
   
#Funcion de consulta tablas principales y de importancia
    def consulta_datos(self):
        self.clean()
        self.clean1()
        self.wind.configure(background="sky blue")
        self.wind.geometry("400x300")
        #self.wind.geometry("600x600")
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.label= Label(ventana, text="CONSULTAR", font= fontStyle) 
        self.label.configure(background="SKY blue")
        self.label.place(x=110,y=10)

        frame= LabelFrame(ventana,text="", font= fontStyle)
        frame.configure(background="sky blue")
        frame.config(bd=5)
        frame.grid_propagate(False)
        frame.config(width="250", height="200")
        frame.place(x=70,y=60)
        self.boton1= ttk.Button(frame, text="Caballo" ,width=20,command= self.caballo)
        self.boton1.place( x=55, y = 40)
        self.boton2= ttk.Button(frame, text="Propietario",width=20)
        self.boton2.place( x=55, y = 80)
        self.boton3= ttk.Button(frame, text="Criadero",width=20) 
        self.boton3.place( x=55, y = 120)
#Funcion que borra todo el contenido de la ventana
    def clean1(self):
        list =self.wind.place_slaves()
        for l in list:
            l.destroy()  
#Funcion consulta caballo:
    def caballo(self):
        self.clean1()
        #prueb git
        #Prueba Diego
        self.wind.geometry("600x600")
        fontStyle = tkFont.Font(family="Lucida Grande", size=10)
        self.wind.configure(background="blue")
        self.frame_caballo= LabelFrame(self.wind,text="", font= fontStyle)
        self.frame_caballo.configure(background="darkgrey")
        self.frame_caballo.config(bd=5)
        self.frame_caballo.grid_propagate(False)
        self.frame_caballo.config(width="540", height="540")
        self.frame_caballo.place(x=30,y=40)
        self.Cod_caballo= Label(self.frame_caballo,text="Código caballo:", font=fontStyle)
        self.Cod_caballo.configure(background="darkgrey")
        self.Cod_caballo.place(x=140,y=50)
        self.codigo_cab=Entry(self.frame_caballo)
        self.codigo_cab.focus()
        self.codigo_cab.place(x=260,y=50)
        self.fallo_busqueda=Label(self.frame_caballo, text="",
                                 font=fontStyle,fg="red" )
        self.fallo_busqueda.configure(background="darkgrey")
        self.fallo_busqueda.place(x=130, y=70)
        self.boton_buscar= ttk.Button(self.frame_caballo, text="Buscar" ,command=self.consulta_caballo ,width=15)
        self.boton_buscar.place( x=170, y = 100)
        self.boton_ingresar_caballo= ttk.Button(self.frame_caballo, text="Añadir",command=self.ingresar_caballo  ,width=15)
        self.boton_ingresar_caballo.place( x=290, y = 100)
        self.Nom_caballo= Label(self.frame_caballo,text="Nombre:", font=fontStyle)
        self.Nom_caballo.configure(background="darkgrey")
        self.Nom_caballo.place(x=100,y=150)
        self.Nom= Label(self.frame_caballo,text="                       ", font=fontStyle)
        self.Nom.place(x=250,y=150)
        self.Fecha_caballo= Label(self.frame_caballo,text="Fecha nacimiento:", font=fontStyle)
        self.Fecha_caballo.configure(background="darkgrey")
        self.Fecha_caballo.place(x=100,y=180)
        self.fech= Label(self.frame_caballo,text="                       ", font=fontStyle)
        self.fech.place(x=250,y=180)
        self.col_caballo= Label(self.frame_caballo,text="Color:", font=fontStyle)
        self.col_caballo.configure(background="darkgrey")
        self.col_caballo.place(x=100,y=210)
        self.col= Label(self.frame_caballo,text="                       ", font=fontStyle)
        self.col.place(x=250,y=210)
        self.sex_caballo= Label(self.frame_caballo,text="Sexo:", font=fontStyle)
        self.sex_caballo.configure(background="darkgrey")
        self.sex_caballo.place(x=100,y=240)
        self.sex= Label(self.frame_caballo,text="                       ", font=fontStyle)
        self.sex.place(x=250,y=240)
        self.gen_caballo= Label(self.frame_caballo,text="Genotipo:", font=fontStyle)
        self.gen_caballo.configure(background="darkgrey")
        self.gen_caballo.place(x=100,y=270)
        self.gen= Label(self.frame_caballo,text="                       ", font=fontStyle)
        self.gen.place(x=250,y=270)
        self.mod_caballo= Label(self.frame_caballo,text="Modalidad marcha:", font=fontStyle)
        self.mod_caballo.configure(background="darkgrey")
        self.mod_caballo.place(x=100,y=300)
        self.mod= Label(self.frame_caballo,text="                       ", font=fontStyle)
        self.mod.place(x=250,y=300)
        self.cri_caballo= Label(self.frame_caballo,text="Criadero:", font=fontStyle)
        self.cri_caballo.configure(background="darkgrey")
        self.cri_caballo.place(x=100,y=330)
        self.cri= Label(self.frame_caballo,text="                       ", font=fontStyle)
        self.cri.place(x=250,y=330)
        self.pro_caballo= Label(self.frame_caballo,text="Propietario Actual:", font=fontStyle)
        self.pro_caballo.configure(background="darkgrey")
        self.pro_caballo.place(x=100,y=360)
        self.pro= Label(self.frame_caballo,text="                       ", font=fontStyle)
        self.pro.place(x=250,y=360)
        self.microchip= Label(self.frame_caballo,text="Microchip:", font=fontStyle)
        self.microchip.configure(background="darkgrey")
        self.microchip.place(x=100,y=390)
        self.micr= Label(self.frame_caballo,text="                       ", font=fontStyle)
        self.micr.place(x=250,y=390)
        self.boton_historial_propietario= ttk.Button(self.frame_caballo, text="Ver historial propietarios" ,command=self.historial_propietarios ,width=22)
        self.boton_historial_propietario.place( x=100, y = 460)
        self.boton_actualizar_propietario= ttk.Button(self.frame_caballo, text="Actualizar propietario" ,command=self.actualizar_propietario ,width=20)
        self.boton_actualizar_propietario.place( x=300, y = 460)
        self.boton_volver1=ttk.Button(self.frame_caballo,text="Volver",command=self.consulta_datos,width=20)
        self.boton_volver1.place(x=200,y=500)

#funcion que  conecta la bases de datos y ejecuta una cCONSULTA
    def mysqlconnect_query(self, query):
        try:
             cursor= self.base_datos.cursor()
             cursor.execute(query)
             self.resultado= cursor.fetchall()
             print(self.resultado)  
             return self.resultado
        except:       
               print("no se pudo , sad")
               self.fallo_busqueda['text']= "Usuario inexistente o fallo en la base de datos"
#Función que contacta con la base de datos y añade 
    def mysqlconnect_ingresar_actualizar(self,query):
        try:
            cursor= self.base_datos.cursor()
            cursor.execute(query)
            print ("La base se ha actualizado correctamente")
            return 0
        except:
            print("fallo en la actualización de datos")
#Función que contecta con la base y ejecuta un PROCEDIMIENTO ALMACENADO
    def mysqlconnect_PA(self, name, parameters=()):
        try:
            cursor=self.base_datos.cursor()
            cursor.callproc(self.base_datos,name, parameters)
            print("Éxito")
            return 0
        except:
            print("fallo")
                           
#Funcion que averigua determinado caballo con código:
    def consulta_caballo(self):
        query= "select * from caballo where Cab_CodRegistro="+self.codigo_cab.get()+";"
        print(query)
        fila= self.mysqlconnect_query(query)
        try:
            self.Nom['text']= self.resultado[0][1]
            self.fech['text']= self.resultado[0][2]
            self.col['text']= self.resultado[0][3]
            self.sex['text']= self.resultado[0][4]
            self.gen['text']= self.resultado[0][6]
            self.mod['text']= self.resultado[0][7]
            self.cri['text']= self.resultado[0][8]
            self.pro['text']= self.resultado[0][9]
            self.micr['text']= self.resultado[0][5] 
        except:
               self.fallo_busqueda['text']= "El caballo no se encuentra en la base de datos"
 
       
#Funcion que muestra crea la interfaz y muestra el historial_propietarios de un caballo
    def historial_propietarios(self):
        #hacer la consulta y mostrarla
        query= "select * from historial_propietarios where caballo_codigo="+self.codigo_cab.get()+";"
        fila= self.mysqlconnect_query(query)
        self.wind.geometry("800x300")
        self.clean1()
        fontStyle = tkFont.Font(family="Lucida Grande", size=30)
        self.wind.configure(background="blue")
        #cuadro para datos
        self.tree= ttk.Treeview(height= 8, columns= ("#1","#2","#3","#4"))
        self.tree['show'] = 'headings'
        self.tree.grid(row= 10, column= 3 , columnspan=2)
        self.tree.heading("#1", text= "Fecha cambio", anchor=CENTER)
        self.tree.heading("#2", text="Código Propietario", anchor=CENTER)
        self.tree.heading("#3", text="Nombre", anchor=CENTER)
        self.tree.heading("#4", text="Teléfono", anchor=CENTER)
        self.tree.place(x=0,y=60)
        # eliminamos si hay datos en la tabla
        records= self.tree.get_children()
        for element in records:
            self.tree.delete(element)
        self.historial=Label(self.wind, text="Historial", anchor=CENTER, font=fontStyle)
        self.historial.place(x=330,y=10)
        self.historial.configure(background="blue") 
        self.boton_volver= ttk.Button(self.wind, text="Volver" ,command=self.caballo  ,width=15)
        self.boton_volver.place(x=200,y=250 )
        for row in fila:
            self.tree.insert('', 0, text= "", values= (row[0], row[1], row[2], row[3]) )   
#Funcion añadir caballo
    def ingresar_caballo(self):
        self.clean1()
        self.wind.geometry("600x600")
        fontStyle = tkFont.Font(family="Lucida Grande", size=30)
        self.wind.configure(background="blue")
        self.frame_caballo= LabelFrame(self.wind,text="", font= fontStyle)
        self.frame_caballo.configure(background="darkgrey")
        self.frame_caballo.config(bd=5)
        self.frame_caballo.grid_propagate(False)
        self.frame_caballo.config(width="540", height="540")
        self.frame_caballo.place(x=30,y=40)
        self.ingresar_caballo=Label(self.wind, text="Ingresar caballo", font=fontStyle)
        self.ingresar_caballo.place(x=160,y=50)
        self.ingresar_caballo.configure(background="darkgrey")
        fontStyle = tkFont.Font(family="Lucida Grande", size=10)
        self.Cod_caballo= Label(self.frame_caballo,text="Código caballo:", font=fontStyle)
        self.Cod_caballo.configure(background="darkgrey")
        self.Cod_caballo.place(x=140,y=70)
        self.codigo_cab=Entry(self.frame_caballo)
        self.codigo_cab.focus()
        self.codigo_cab.place(x=250,y=70)
        self.Nom_caballo= Label(self.frame_caballo,text="Nombre:", font=fontStyle)
        self.Nom_caballo.configure(background="darkgrey")
        self.Nom_caballo.place(x=140,y=100)
        self.Nom= Entry(self.frame_caballo)
        self.Nom.place(x=250,y=100)
        self.Fecha_caballo= Label(self.frame_caballo,text="Fecha nacimiento:", font=fontStyle)
        self.Fecha_caballo.configure(background="darkgrey")
        self.Fecha_caballo.place(x=140,y=130)
        self.fech= Entry(self.frame_caballo)
        self.fech.place(x=250,y=130)
        self.col_caballo= Label(self.frame_caballo,text="Color:", font=fontStyle)
        self.col_caballo.configure(background="darkgrey")
        self.col_caballo.place(x=140,y=160)
        self.col= Entry(self.frame_caballo)
        self.col.place(x=250,y=160)
        self.sex_caballo= Label(self.frame_caballo,text="Sexo:", font=fontStyle)
        self.sex_caballo.configure(background="darkgrey")
        self.sex_caballo.place(x=140,y=190)
        self.sex= Entry(self.frame_caballo)
        self.sex.place(x=250,y=190)
        self.gen_caballo= Label(self.frame_caballo,text="Genotipo:", font=fontStyle)
        self.gen_caballo.configure(background="darkgrey")
        self.gen_caballo.place(x=140,y=220)
        self.gen= Entry(self.frame_caballo)
        self.gen.place(x=250,y=220)
        self.mod_caballo= Label(self.frame_caballo,text="Modalidad marcha:", font=fontStyle)
        self.mod_caballo.configure(background="darkgrey")
        self.mod_caballo.place(x=140,y=250)
        self.mod= Entry(self.frame_caballo)
        self.mod.place(x=250,y=250)
        self.cri_caballo= Label(self.frame_caballo,text="Criadero:", font=fontStyle)
        self.cri_caballo.configure(background="darkgrey")
        self.cri_caballo.place(x=140,y=280)
        self.cri= Entry(self.frame_caballo)
        self.cri.place(x=250,y=280)
        self.pro_caballo= Label(self.frame_caballo,text="Propietario Actual:", font=fontStyle)
        self.pro_caballo.configure(background="darkgrey")
        self.pro_caballo.place(x=140,y=310)
        self.pro= Entry(self.frame_caballo)
        self.pro.place(x=250,y=310)
        self.microchip= Label(self.frame_caballo,text="Microchip:", font=fontStyle)
        self.microchip.configure(background="darkgrey")
        self.microchip.place(x=140,y=340)
        self.micr= Entry(self.frame_caballo)
        self.micr.place(x=250,y=340)
        self.cod_padre= Label(self.frame_caballo,text="Código padre:", font=fontStyle)
        self.cod_padre.configure(background="darkgrey")
        self.cod_padre.place(x=140,y=370)
        self.cod_p= Entry(self.frame_caballo)
        self.cod_p.place(x=250,y=370)
        self.cod_madre= Label(self.frame_caballo,text="Código madre:", font=fontStyle)
        self.cod_madre.configure(background="darkgrey")
        self.cod_madre.place(x=140,y=400)
        self.cod_m= Entry(self.frame_caballo)
        self.cod_m.place(x=250,y=400)
        self.boton_guardar=ttk.Button(self.frame_caballo,text="Guardar",command=self.instruccion_ingreso_caballo ,width=20)
        self.boton_guardar.place(x=280,y=450)
        self.boton_volver1=ttk.Button(self.frame_caballo,text="Volver",command=self.caballo,width=20)
        self.boton_volver1.place(x=110,y=450)
#Funcion que crea la instruccion para añadir un caballo y luego llama a la funcion que conecta e ingresa los datos        
    def instruccion_ingreso_caballo(self):
        query= "call insertar_caballo("+self.codigo_cab.get()+","+self.Nom.get()+","+self.fech.get()+","+self.col.get()+","+self.sex.get()+","+self.micr.get()+","+self.gen.get()+","+self.mod.get()+","+self.cri.get() +","+self.pro.get()+","+self.cod_m.get()+","+self.cod_p.get()+");"
        print(query)
        self.mysqlconnect_ingresar_actualizar(query)
#Función que permite actualizar el propietario del caballo que se consultó
    def actualizar_propietario(self):
        self.clean1()
        self.wind.geometry("500x270")
        fontStyle = tkFont.Font(family="Lucida Grande", size=20)
        self.actualizacion= Label(self.wind, text="Actualización propietario caballo", anchor=CENTER,font=fontStyle)
        self.actualizacion.place(x=55,y=10)
        self.actualizacion.configure(background="blue")
        fontStyle = tkFont.Font(family="Lucida Grande", size=11)
        self.codigo_cab= Label(self.wind, text="Ingrese el código del caballo:", anchor=CENTER,font=fontStyle)
        self.codigo_cab.configure(background="blue")
        self.codigo_cab.place(x=20,y=55)
        self.cod_cab=Entry(self.wind)
        self.cod_cab.place(x=190, y=85)
        self.codigo_pro= Label(self.wind, text="Ingrese el código del propietario (se debe encontrar en la base de datos):", anchor=CENTER,font=fontStyle)
        self.codigo_pro.configure(background="blue")
        self.codigo_pro.place(x=20,y=115)
        self.cod_pro=Entry(self.wind)
        self.cod_pro.place(x=190, y=150)
        self.fallo_actualizacion= Label(self.wind, text="", anchor=CENTER,font=fontStyle, fg="red")
        self.fallo_actualizacion.configure(background="blue")
        self.fallo_actualizacion.place(x=150,y=170)
        self.boton_actualizar=ttk.Button(self.wind,text="Actualizar",command=self.accion_boton_actualizar,width=12)
        self.boton_actualizar.place(x=130,y=195)
        self.boton_volver=ttk.Button(self.wind,text="Volver",command= self.caballo,width=12)
        self.boton_volver.place(x=280,y=195)
    def accion_boton_actualizar(self):
        name="cambio_propietario_caballo"
        parameters= (int(self.cod_cab.get()), self.cod_pro.get())
        print (parameters)
        update=self.mysqlconnect_PA(name, parameters)
        if(update==0):
            self.fallo_actualizacion['text']= "Actualización existosa"
        else:
            self.fallo_actualizacion['text']= "Error"
        

                 
if __name__=='__main__' :
    ventana= Tk()
    programa= interfaz(ventana)
    ventana.mainloop()

      


