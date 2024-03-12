x= int(input("digite el primer numero "))
y= int(input("digite el segundo numero "))

def suma (x,y):
    suma= y+x
    return suma

menu= input("""que opcion desea hacer
            1. suma 
            3. division 
            4. salir 
            """)
if menu == "1":
    print("entro a la funcion de suma")
    print (f"su resultado es {suma(x,y)}")