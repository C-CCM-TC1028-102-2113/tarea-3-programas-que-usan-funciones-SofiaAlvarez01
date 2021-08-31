def arearec (a,b):
    area= a*b
    return area
def main():
    #escribe tu código abajo de esta línea
    base= float(input("Dame la base: "))
    altura= float(input("Dame la altura: "))
    x= arearec(base,altura)
    print("El área del rectángulo es:",x)    
    pass

if __name__=='__main__':
    main()
