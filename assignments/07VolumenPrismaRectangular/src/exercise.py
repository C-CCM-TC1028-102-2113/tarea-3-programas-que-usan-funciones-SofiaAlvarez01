
def arearec (a,b):
    area= a*b
    return area

def volumenrec (c,d):
    volumen= c*d
    return volumen

base= float(input("Dame la base: "))
altura= float(input("Dame la altura: "))
profundidad= float(input("Dame la profundidad: "))
y= arearec (base,altura)
x= volumenrec (y, profundidad)
print("El volumen del prisma es: ",x)
    
    pass

if __name__=='__main__':
    main()
