from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
ventana = Tk()
ventana.title("calculadora")
ventana.geometry("320x480")
ventana.configure(background= "purple")
########contar veces del programa####
archivo = open('contar.txt', 'r')   ##1. abrir el archivo para leer
linea=archivo.readline()
veces=int(linea)+1                  ##2. obtener el numero de veces que se ha guardado y sumarle 1.
archivo.close()
archivo = open('contar.txt', 'w')   ##3. abrir el archivo para escribir
archivo.write(str(veces))           ##4. guargar el numero de veces que se ha abierto
archivo.close()                     ##5. cerrar el archivo
###########################################



menu=Combobox(ventana)
menu['values']= ("seleccione la opcion","suma","resta","multiplicacion","division")
menu.current(0)
menu.grid(row=0,column=0,)
lb1=Label(ventana,text="numero 1",background= "blue")
lb1.grid(row=1,column=0)
lb2=Label(ventana,text="numero 2",background="red")
lb2.grid(row=2,column=0)
lb3=Label(ventana,text="numero 3",background="orange")
lb3.grid(row=3,column=0)
num1=Entry(ventana,width=10)
num1.grid(row=1,column=1)
num2=Entry(ventana,width=10)
num2.grid(row=2,column=1)
num3=Entry(ventana,width=10)
num3.grid(row=3,column=1)
def borrarDatos():
    num1.delete(0,END)
    num2.delete(0,END)
    num3.delete(0,END)
    menu.current(0)
def Cerrardatos():
    exit()

btnBorrar=Button(ventana,text="borrar",command=borrarDatos,cursor="pirate")
btnBorrar.grid(row=7,column=0)
btnCerrar=Button(ventana,text="cerrar",command=Cerrardatos,cursor="pirate")
btnCerrar.grid(row=9,column=0)

#######AGREGAR LA ETIQUETA DE VECES USADO  CON LA VARIABLE: veces  #############
lb4=Label(ventana,text="VECES USADO: "+ str(veces),background="orange")
lb4.grid(row=12,column=0)
################################################################################


def mostrarResultado():
    opcion=menu.get()
    if opcion== "seleccione la opcion":
        messagebox.showerror("error","debes seleccionar una opcion")
    elif num1.get()=="" or num2.get()=="" or num3.get()=="":
        messagebox.showerror("error","debes poner los 3 numeros") 
    else:
        res=0
        n1=int(num1.get())
        n2=int(num2.get())
        n3=int(num3.get())
        if n2==0 or n3==0:
            messagebox.showerror("error","no se puede dividir entre cero")
        else:
            historial=""                ####1. preparar la variable para el:     historial
            if opcion=="suma":
                res=n1+n2+n3
                historial=str(n1)+"+"+str(n2)+"+"+str(n3)+"="+str(res)  ##si es suma guardar la operacion en historial
            if opcion=="resta":
                res=n1-n2-n3
                historial = str(n1) + "-" + str(n2) + "-" + str(n3)+"="+str(res)  ##guardar la operacion de resta en historial
            if opcion=="multiplicacion":
                res=n1*n2*n3
                historial = str(n1) + "*" + str(n2) + "*" + str(n3)+"="+str(res)   ##guargar la operacion de multiplicacion
            if opcion=="division":
                res=n1/n2/n3
                historial = str(n1) + "/" + str(n2) + "/" + str(n3)+"="+str(res)    ### guardar la operacion de division en historial
            messagebox.showinfo("resultado",res)
            ###########   GUARDAR EL HISTORIAL DE LAS OPERACIONES    #######
            archivo=open("datos.txt","a+")    #1. abrir el archivo datos.txt
            archivo.write("\n"+historial)     #2. agregar los datos del nuevo historial
            archivo.close()                   #3. cerrar el archivo
            #########     HISTORIAL GUARDADO    #########
            borrarDatos()
btnRes=Button(ventana,text="resultado",command=mostrarResultado,cursor="heart")
btnRes.grid(row=7,column=2)      
ventana.mainloop()

