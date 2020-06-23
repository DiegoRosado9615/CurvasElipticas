"""Clase que modela puntos"""
class Punto:
	"""Constructor de Puntos"""
	def __init__(self,num1,num2):
		self.x=num1
		self.y=num2
	"""Metodo que obtiene el inverso multiplicativo """
	def inversoMultiplicativo(self,a, n):
		a%=n;
		for i in range(1,n):
			if ((a * i) % n == 1) :
				return i;
		return -1
	"""Metodo que nos dice si 2 puntos son iguales o no
	devuelve true si son iguales y false en otro caso """
	def esIgual(self,punto2):
		x1=self.x
		y1=self.y
		x2=punto2.x
		y2=punto2.y

		if(x1==x2 and y1==y2):
			return True
		else:
			return False
	"""Metodo que obtiene el valor de la lambda
	Devuelve una lista en la posición cero se encuentran los valores que si tuvi
	eron un inverso y en la posicion uno un false, mientras los valores que no
	tuvieron inverso  tienen en la posicion uno un true
	"""
	def lambd(self,punto2,a,p):
		x1=self.x
		y1=self.y
		x2=punto2.x
		y2=punto2.y
		valorFinal=[]
		if( self.esIgual(punto2)):
			if(self.inversoMultiplicativo(2*y1,p)==-1):
				valorFinal.append(self.mcd((2*y1%p),p))
				valorFinal.append(True)
				return valorFinal
			x1=x1*x1
			valorFinal.append(((((3*x1) + a)*self.inversoMultiplicativo(2*y1,p))) % p)
			valorFinal.append(False)
			return valorFinal
		else:
			if((self.inversoMultiplicativo(x2-x1, p) ==-1)):
				valorFinal.append(self.mcd((x2-x1%p),p))
				valorFinal.append(True)
				return valorFinal
			valorFinal.append(((y2-y1)*self.inversoMultiplicativo(x2-x1, p))%p)
			valorFinal.append(False)
			return valorFinal
	"""Metodo que permite sumar 2 puntos,recibe el punto con el que se va a
	sumar  y devuelve un nuevo punto o un mensaje de infinito"""
	def suma(self,punto2,a,p):
		x1=self.x
		y1=self.y
		x2=punto2.x
		y2=punto2.y
		listaFinal=[]
		if( x1==x2 and ((y1*-1)== y2 )):
			punto3=Punto(-1,-1)
			return punto3
		else:
			punto3=Punto(0,0)
			lambd=self.lambd(punto2,a,p)
			lambd2=lambd[0]
			if lambd[1]==True:
				listaFinal.append(lambd2)
				listaFinal.append(True)
				return listaFinal
			punto3.x=((lambd2 * lambd2)-x1-x2)%p
			punto3.y=((lambd2*(x1-punto3.x))-y1)%p
			listaFinal.append(punto3)
			listaFinal.append(False)
			return listaFinal


	def suma2(self,punto2,a,p):
		x1=self.x
		y1=self.y
		x2=punto2.x
		y2=punto2.y
		listaFinal=[]
		if( x1==x2 and ((y1*-1)== y2 )):
			punto3=Punto(-1,-1)
			return punto3
		if(x1==x2 and y1!=y2 ):
			print("Hola")
			punto3=Punto (-1,-1)
			return punto3
		else:
			punto3=Punto(0,0)
			lambd=self.lambd(punto2,a,p)
			lambd2=lambd[0]
			punto3.x=((lambd2 * lambd2)-x1-x2)%p
			punto3.y=((lambd2*(x1-punto3.x))-y1)%p
			return punto3

	def creadorPuntos(self,x,y):
		puntoNuevo=Punto(x,y)
		return puntoNuevo

	def sumaRepetida(self,numVeces,a,p):
		contador=0
		puntoNuevo=self.creadorPuntos(self.x,self.y)
		informacion=[]
		while (contador<numVeces) :
			informacion=self.suma(puntoNuevo,a,p)
			if informacion[1]==True:
				print("Un Factor de este numero es")
				return informacion[0]
			puntoNuevo=informacion[0]
			contador=contador+1
			pass
		return puntoNuevo

	def factorial(self,puntoInical,a,p,contador):
		print(puntoInical)
		puntoInical=puntoInical.sumaRepetida(contador,a,p)
		contador=contador+1
		if( type(puntoInical) is int ) :
			return puntoInical
		return puntoInical.factorial(puntoInical,a,p,contador)
	"""Metodo que saca el orden de un punto"""
	def calculaOrden(self,punto,a,p):
		puntoNuevo=Punto(self.x,self.y)
		puntoInfinito=Punto(-1,-1)
		orden=1
		iteraciones=0
		while(p>iteraciones):
			if(puntoNuevo.esIgual(puntoInfinito) ):

				break
			orden=orden+1
			iteraciones=iteraciones+1
			puntoNuevo=puntoNuevo.suma2(self,a,p)
			print(puntoNuevo)
		return orden


	"""Metodo que imprime un punto"""
	def __str__(self):
		return "(" + str( self.x ) + " , " + str(self.y)+")"

	"""Metodo que saca el mcd"""
	def mcd(self,num1,num2):
		resta=0
		while (num2>0):
			resta=num2
			num2=num1%num2
			num1=resta
		return num1



""" Clase curva: modela una curva eliptica """
class Curva:
	"""Constructor de curvas: Recibe los coeficientes de la ecuación y el campo"""
	def __init__ (self, A, B, campo):
		self.a = A
		self.b = B
		self.p = campo

	""" Metodo que calcula los puntos dentro de la curva"""
	def calculaPuntosEncurva(self):
		print(self)
		print("Puntos")
		listaPuntos= []
		for i in range(0,self.p):
			x = ((i**3) + (self.a*i) + self.b) % self.p
			for j in range(0,self.p):
				y = (j**2) % self.p
				if x==y:
					punto="\t("+str(i)+","+str(j)+"),"
					print("\t("+str(i)+","+str(j)+"),")
					listaPuntos.append(punto)
		return listaPuntos
		print("\tO.")

	""" Metodo que verifica si un punto esta dentro de la curva"""
	def esta(self, punto):
		 y = (punto.y ** 2)
		 resto = (punto.x ** 3) + (self.a * punto.x) + (self.b)
		 if y == (resto % self.p) :
		 	return True
		 else:
		 	return False
	"""Metodo que imprime una Curva"""
	def __str__ (self):
		if (self.a==1):
			return "y² = x³ + x + "+str(self.b)+ " con Z: "+str(self.p)
		else :
			return "y² = x³ + "+str(self.a)+"x + "+str(self.b)+ " con Z: "+str(self.p)

#Pactica
##El metodo Factorial que factoriza los 2 numeros
#En su tercer parametro, es donde se le debe pasar un numero n
#Donde n es un numero compuesto por p y q donde p y q son diferentes y
#Ambos son primos
#Utilizamos abritatiame la curva y^2 = x^3+x+1
#Para empezar siempre Utilizamos el puton 0,1 albritario que esta
#En la curva x^3+x+1
#Como para que funcione el algorimo solo debemos pasar cuanto vale
#El coeficiente de X^1 solamente le pasamos el uno
punto1=Punto(0,1)
primo=input("Introduce un numero: ")
primo=int(primo)
x=punto1.factorial(punto1,1,primo,1)
print(x)
z=int (primo/x)
print ("Y el otro factor es ")
print(z)
