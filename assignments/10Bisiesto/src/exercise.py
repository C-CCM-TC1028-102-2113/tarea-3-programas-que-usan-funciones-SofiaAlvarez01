def bisiesto (a):
    if (a%4==0 and a%100!=0) or (a%400==0):
        añof= 1
    else:
        añof= 2
    return añof
def main():
    #escribe tu código abajo de esta línea
    año= int(input())
    x= bisiesto (año)
    if x==1:
        print ("True")
    elif x==2:
        print("False")    
    pass

if __name__=='__main__':
    main()
