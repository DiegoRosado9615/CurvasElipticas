class Punto:
    """docstring forPunto."""
    def __init__(self,num1,num2):
        """Contsructor"""
        self.x=num1
        self.y=num2

    def esIgual(self,punto2):
        """Metodo que nos dice si 2 puntos son iguales o note
           devuelve true en caso que si y false en otro """
        x1=self.x
        y1=self.y
        x2=punto2.x
        y2=punto2.y
        if(x1==x2 and y1==y2):
            return True
        else:
            return False

    def alpha(self,punto2,a,p):
        x1=self.x
        y1=self.y
        x2=punto2.x
        y2=punto2.y
        if(self.esIgual(punto2)):
            x1=x1*x1
            return (int(((3*x1) +a )/ (2*y1) ))%p
        else:
            if(x2==x1):
                return "Divicion entre 0"

            return (int((y2-y1)/(x2-x1)))%p


    def suma(self,punto2,a,p):
        """Metodo que permite sumar 2 puntos,recibe el punto con el que se va a
        sumar  y devuelve un nuevo punto o un mensaje de infinito"""
        x1=self.x
        y1=self.y
        x2=punto2.x
        y2=punto2.y
        if( x1==x2 and ((y1*-1)== y2 )):
            return "infinito"
        else:
            punto3=Punto(0,0)
            alpha=punto1.alpha(punto2,a,p)
            alpha2=alpha*alpha
            punto3.x=alpha2-x1-x2
            punto3.y=alpha*(x1-punto3.x)-y1
            return punto3

    def __str__(self):
        """Imprimir la cadena"""
        return "x = " + str( self.x ) + ", y = " + str(self.y)


punto1= Punto(15,-4)
punto2= Punto (331,-6000)

print(punto1.suma(punto2,20,35))##Esto es q2, y estoy sacando q3
