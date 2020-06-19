class Punto:
    """Constructor de Puntos"""
    def __init__(self,num1,num2):
        self.x=num1
        self.y=num2
    """Metodo que obtiene el inverso multiplicativo """
    def inversoMultiplicativo(self,a, n):
	    a%=n
	    for i in range(1,n):
	        if ((a * i) % n == 1) :
	            return i
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
    def lambd(self,punto2,a,p):
    	x1=self.x
    	y1=self.y
    	x2=punto2.x
    	y2=punto2.y
    	if(self.esIgual(punto2)):
			if(self.inversoMultiplicativo(2*y1,p)==-1):
				pass
    		x1=x1*x1    
    		return ((((3*x1) + a)*self.inversoMultiplicativo(2*y1,p))) % p
    	else:
            if(self.inversoMultiplicativo(x2-x1, p)==-1):
                return "No hay inverso"
    	return ((y2-y1)*self.inversoMultiplicativo(x2-x1, p))%p