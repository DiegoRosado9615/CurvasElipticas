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
	    return -1;
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
    """Metodo que obtiene el valor de la lambda"""
    def lambd(self,punto2,a,p):
    	x1=self.x
    	y1=self.y
    	x2=punto2.x
    	y2=punto2.y
    	if(self.esIgual(punto2)):
    		x1=x1*x1
    		return ((((3*x1) + a)*self.inversoMultiplicativo(2*y1,p))) % p
    	else:
    		return ((y2-y1)*self.inversoMultiplicativo(x2-x1, p))%p
    """Metodo que permite sumar 2 puntos,recibe el punto con el que se va a
	sumar  y devuelve un nuevo punto o un mensaje de infinito"""
    def suma(self,punto2,a,p):
        x1=self.x
        y1=self.y
        x2=punto2.x
        y2=punto2.y
        if( x1==x2 and ((y1*-1)== y2 )):
            punto3=Punto(-1,-1)
            return punto3
        else:
            punto3=Punto(0,0)
            lambd=punto1.lambd(punto2,a,p)
            punto3.x=((lambd * lambd)-x1-x2)%p
            punto3.y=((lambd*(x1-punto3.x))-y1)%p
            return punto3
    """Metodo que genera la suma de puntos de manera extendida"""
    def sumaExtendida(self,punto,a,p):
    	##la idea es sumar el punto tantas veces hasta que ya no sea posible.
    	##es decir sacar la suma de forma lineal
        listaPuntos=[]
        contador=0
        puntoNuevo=punto
        while contador <p:
            puntoNuevo=punto.suma(puntoNuevo,a,p)
            print(puntoNuevo)
            listaPuntos.append(puntoNuevo)
            contador=contador+1
        return listaPuntos

    """Metodo que nos dice si es un resuido cuadratico o no"""
    def metodCuadratico(self,a,p):
        cuadrado=(p-1)/2
        formula= (a**cuadrado)%p
        if (formula==1):
            return True
        else:
            return False

    """Metodo que imprime un punto"""
    def __str__(self):
        return "(" + str( self.x ) + " , " + str(self.y)+")"


""" Clase curva: modela una curva eliptica
class Curva:

	def __init__ (self, A, B, campo):
		self.a = A
		self.b = B
		self.p = campo


	def calculaPuntosEncurva(self):
		print(self)
		print("Puntos")
		for i in range(0,self.p):
			x = ((i**3) + (self.a*i) + self.b) % self.p
			for j in range(0,self.p):
				y = (j**2) % self.p
				if x==y:
					print("\t("+str(i)+","+str(j)+"),")
		print("\tO.")
	def esta(self, punto):
		 y = (punto.y ** 2)
		 resto = (punto.x ** 3) + (self.a * punto.x) + (self.b)
		 if y == (resto % self.p) :
		 	return True
		 else:
		 	return False
	def __str__ (self):
		if (self.a==1):
			return "y² = x³ + x + "+str(self.b)+ " con Z: "+str(self.p)
		else :
			return "y² = x³ + "+str(self.a)+" x + "+str(self.b)+ " con Z: "+str(self.p)

"""
def ecuacion(limite):
    listaValor=[]
    valor=0
    for i in range(limite):
        valor=(i**3+i+6)%11
        listaValor.append(valor)
    return listaValor

punto1= Punto(2,7)
punto2= Punto(2,7)
punto3=punto1.suma(punto2,1,11)
print(punto1.sumaExtendida(punto1,1,11))
##print(punto1.inversoMultiplicativo(58,493))
