

def iden():
    iden = input("¿Tienes identificación oficial? (s/n): ")
    if iden =="n":
         print("No cumples requisitos")
    elif iden =="s":
         print("Trámite de licencia concedido")
    else:
         print("Respuesta incorrecta")

def main():

    edad = int(input("Ingresa tu edad: "))
    if edad >0 and  edad <18:
       print("No cumples requisitos")
    elif edad >=18:
        iden()    
    else:
         print("Respuesta incorrecta")
        
if __name__ == '__main__':
         main()


