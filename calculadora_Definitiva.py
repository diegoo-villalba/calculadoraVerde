from tkinter import *

raiz=Tk()

miFrame=Frame(raiz)

miFrame.pack()

#------- Operacion/Resultado-------------------------
operacion=""  #Variable global "operacion" que sea accesible desde todas las funciones/metodos de nuestro programa.
				#Esa variable "operacion" almacena en su interior la operacion que quiere realizar el usuario (+, -, *, /)

reset_pantalla=False

resultado=0   #Variable global "resultado" que va almacenando los valores númericos a medida que vamos sumando,restando, etc. Es =0 xq al comenzar el programa el resultado de las operaciones debe ser igual a cero.
#--------PANTALLA-----------------------------

numeroPantalla=StringVar() #Definimos una variable "numeroPantalla" y esta va a contener un string de caracteres "stringVar()"

pantalla=Entry(miFrame, textvariable=numeroPantalla) #Asociamos la variable "numeroPantalla" a nuestra Pantalla con "textvariable"
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4) #Instrucción "colspan": le decimos a la columna cuantas "columnas queremos que ocupe"
pantalla.config(bg="black", fg="green", justify="right")

#-----------PULSACIONES TECLADO---------------

def numeroPulsado(num): 
	global operacion

	global reset_pantalla

	if reset_pantalla!=False:  #Con el condicional "if" evaluamos si operacion es dif de "", de ser así entonces el usuario esta apretando el botón "+"
		
		numeroPantalla.set(num) #...entonces en pantalla unicamente ponga el valor "num" que le estoy pasando por parámetro a la función "suma". Es decir: si aprieto "+" y luego otro valor "num" que llame a la función "suma" entonces que no concatene con los valores previos sino que coloque el nuevo numero recientemente apretado en pantalla. 

		reset_pantalla=False #...debe de seguir concatenando para que siga la union numeros.
	
	else:
		numeroPantalla.set(numeroPantalla.get() + num) #Para cuando llamemos a la función, vea lo que hay en pantalla y lo agregue al n° anteriormente marcado. "set()" establece un valor en pantalla y "get()" obtiene la información en pantalla
#En conclusión lo que hace es: llamamos a la función pulsando el n°, lo agrega, luego mira la información en pantalla c/"get()" y luego agrega el otro n° marcado.

def suma(num): #Al apretar el botón suma cambiamos la variable operación = "" por operacion="+"
	
	global operacion  #global operacion: para que tenga en cuenta que esta función va a operar con la variable global "operacion"

	global resultado  #también este metodo "suma" debe de contar con la variable global "resultado"

	global reset_pantalla

	resultado+=int(num)  #Incremento += :  para que a la variable "resultado" le incremente el valor numerico anterior. La funcion "suma" se llama cuando apreto el valor "+", luego necesito que el numero en pantalla se almacene en algun sitio (resultado) y se sume a lo que hay anteriormente. Osea, resultado es lo que queda guardado y a eso se le incrementa (luego de apretar el "+") el nuevo valor "num" que ponemos para completar la suma.

	operacion="suma" #Al pulsar el botón "+" de la calculadora se llame a la función y almacene dentro de la variable global "operación" la palabra "suma"

	reset_pantalla=True

	numeroPantalla.set(resultado) #Esto es para que los valores numericos que voy agregando a la suma aparezcan en pantalla.

#-------------------FUNCION RESTA-----------------------------------
num1=0

contador_resta=0

def resta(num):

	global operacion

	global resultado

	global num1

	global contador_resta

	global reset_pantalla

	if contador_resta==0:

		num1=int(num)

		resultado=num1
	else:

		if contador_resta==1:

			resultado=num1-int(num)
		
		else:

			resultado=int(resultado)-int(num)
		
		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()

	contador_resta=contador_resta+1

	operacion="resta"

	reset_pantalla=True

#----------------FUNCION PRODUCTO----------------------
contador_multi=0

def multiplica(num):
	global operacion

	global resultado

	global num1

	global contador_multi

	global reset_pantalla

	if contador_multi==0:
	
		num1=int(num)
	
		resultado=num1

	else:

		if contador_multi==1:

			resultado=num1*int(num)

		else:

			resultado=int(resultado)*int(num)

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()

	contador_multi=contador_multi+1

	operacion="multiplicacion"

	reset_pantalla=True	

#--------------FUNCION DIVISION:----------------

contador_divi=0

def divide(num):
	global operacion

	global resultado

	global num1

	global contador_divi

	global reset_pantalla

	if contador_divi==0:

		num1=float(num)

		resultado=num1
	else:

		if contador_divi==1:

			resultado=num1/float(num)

		else:

			resultado=float(resultado)/float(num)

		numeroPantalla.set(resultado)

		resultado=numeroPantalla.get()

	contador_divi = contador_divi + 1
	
	operacion="division"

	reset_pantalla=True

#-----------Funcion el_resultado--------

def el_resultado(): #Funcion para que al apretar el botón "=" me aparezca el resultado de la operacion hasta el momento.

	global resultado  #Debe de operar esta función con la variable global "restulado"

	global operacion

	global contador_resta

	global contador_multi

	global contador_divi

	if operacion=="suma":
		
		numeroPantalla.set(resultado+int(numeroPantalla.get())) #La función debe reflejar en pantalla el resultado de la operacion hasta el momento + el ultimo n° (almacena el resultado de la 1er suma y muestra el n° siguiente que queremos sumar)

		resultado=0 #Para que despues de obtener un resultado, este sea reseteado y no arrastre el ultimo resultado al hacer la operacion por 3ra vez.

	elif operacion=="resta":

		numeroPantalla.set(int(resultado)-int(numeroPantalla.get()))

		resultado=0

		contador_resta=0

	elif operacion=="multiplicacion":

		numeroPantalla.set(int(resultado)*int(numeroPantalla.get()))

		resultado=0

		contador_multi=0

	elif operacion=="division":

		numeroPantalla.set(int(resultado)/int(numeroPantalla.get()))

		resultado=0

		contador_divi=0


#-------Fila 1--------------------
botonPotencia=Button(miFrame, text="^", width=3)
botonPotencia.grid(row=2, column=2)
botonCE=Button(miFrame, text="CE", width=3)
botonCE.grid(row=2, column=3)
botonC=Button(miFrame, text="C", width=3)
botonC.grid(row=2, column=4)

#-------Fila 2--------------------

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7")) #lambda o "funciones anonimas" son funciones que quedan de referencia y se llaman cuando el usuario pulse el botón.
boton7.grid(row=3, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"))
boton8.grid(row=3, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"))
boton9.grid(row=3, column=3)
botonDiv=Button(miFrame, text="/", width=3, command=lambda:divide(numeroPantalla.get()))
botonDiv.grid(row=3, column=4)

#-------Fila 3--------------------

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4")) #Para que escriba el numero cuando lo aprieto debo de agregar "command"=Función
boton4.grid(row=4, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"))
boton5.grid(row=4, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"))
boton6.grid(row=4, column=3)
botonMult=Button(miFrame, text="X", width=3, command=lambda:multiplica(numeroPantalla.get()))
botonMult.grid(row=4, column=4)

#-------Fila 3--------------------

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"))
boton1.grid(row=5, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"))
boton2.grid(row=5, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"))
boton3.grid(row=5, column=3)
botonRestar=Button(miFrame, text="-", width=3, command=lambda:resta(numeroPantalla.get()))
botonRestar.grid(row=5, column=4)

#-------Fila 3--------------------

boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"))
boton0.grid(row=6, column=1)
botonComa=Button(miFrame, text=",", width=3, command=lambda:numeroPulsado(","))
botonComa.grid(row=6, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:el_resultado())
botonIgual.grid(row=6, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get())) #Aquí con un command llamamos a la funcion "suma". El parametro que debemos pasarle a la función "suma" es lo que hay escrito en pantalla por eso "numeroPantalla.get()"
botonSuma.grid(row=6, column=4)

#--------Poner numeros en pantalla---------- (arranca arriba)










raiz.mainloop()