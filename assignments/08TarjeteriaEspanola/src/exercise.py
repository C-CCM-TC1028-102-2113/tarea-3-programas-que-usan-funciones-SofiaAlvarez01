def ntcpli (a):
    c= a*12
    return c

def ntcplu (b):
    d= b*35
    return d

def main():
    #escribe tu código abajo de esta línea
    pliegos= int(input("Dame la cantidad de pliegos de papel albanene: "))
    plumones= int(input("Dame la cantidad de plumones: "))
    z= ntcpli(pliegos)
    x= ntcplu (plumones)
    if z<x:
        print ("El número máximo de tarjetas que se pueden hacer es:",z)
    elif x<z:
        print ("El número máximo de tarjetas que se pueden hacer es:",x)
    pass

if __name__=='__main__':
    main()
