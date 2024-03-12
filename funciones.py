# cuando llamamos yuna funcion esta se ejecuta 
# el parametro es lo que acompaña  la linea del titulo "def"
# y ese parametro va a hacer nuestra "x" en la operacion matematica

def maximo(x,y):
    if x>y:
        x+y
    else:
        print(f" {x} no es mayor")   
        
    
w= 5 + maximo(5,2)
print(w)