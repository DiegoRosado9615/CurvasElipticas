class Punto:
    """docstring forPunto."""
    def __init__(self,num1,num2):
        """Constructor"""
        self.x=num1
        self.y=num2

    def esIgual(self,punto2):
        """Metodo que nos dice si 2 puntos son iguales o no
           devuelve true si son iguales y false en otro caso """
        x1=self.x
        y1=self.y
        x2=punto2.x
        y2=punto2.y
        if(x1==x2 and y1==y2):
            return True
        else:
            return False


    def lambd(self,punto2,a,p):
        x1=self.x
        y1=self.y
        x2=punto2.x
        y2=punto2.y
        if(self.esIgual(punto2)):
            x1=x1*x1
            return (int(((3*x1) +a )/ (2*y1) ))%p
        else:
            if(x2==x1):
                return "Division entre 0"

            return (int((y2-y1)/(x2-x1)))%p


    def suma(self,punto2,a,p):
        """Metodo que permite sumar 2 puntos,recibe el punto con el que se va a
        sumar  y devuelve un nuevo punto o un mensaje de infinito"""
        x1=self.x
        y1=self.y
        x2=punto2.x
        y2=punto2.y
        if( x1==x2 and ((y1*-1)== y2 )):
            return "O"
        else:
            punto3=Punto(0,0)
            lambd=punto1.lambd(punto2,a,p)
            punto3.x=(lambd * lambd)-x1-x2
            punto3.y=lambd*(x1-punto3.x)-y1
            return punto3

    def __str__(self):
        """Imprimir la cadena"""
        return "x = " + str( self.x ) + ", y = " + str(self.y)

class Curva:
	def __init__ (self, A, B, campo):
		self.a = A
		self.b = B
		self.p = campo

	def calculaPuntosEncurva(self):
		if self.a == 1:
			print("Curva: y² = x³ + x +"+str(self.b))
		else:
			print("Curva: y² = x³ + "+str(self.a)+"x + "+str(self.b))

		for i in range(0,self.p):
			x = ((i**3) + (self.a*i) + self.b) % self.p
			for j in range(0,self.p):
				y = (j**2) % self.p
				if x==y:
					print("("+str(i)+","+str(j)+")")



punto1= Punto(15,-4)
punto2= Punto (331,-6000)

curva = Curva(10,6,11)
curva.calculaPuntosEncurva()

##print(punto1.suma(punto2,20,35))##Esto es q2, y estoy sacando q3
