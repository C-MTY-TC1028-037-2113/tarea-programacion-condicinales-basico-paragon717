
def main():
    X = int(input("Ingresa la medida del lado 1: "))
    Y = int(input("Ingresa la medida del lado 2: "))
    Z = int(input("Ingresa la medida del lado 3: "))

    if X+Y > Z and Y+Z > X and X+ Z > Y:
       if  (X==Y==Z):
            print("ES UN TRIANGULO EQUILATERO")
       elif (X == Y  or X == Z or Y == Z):
            print("ES UN TRIANGULO ISOSCELES")
       elif (X!=Z and Y!=Z and X!=Y):
            print("ES UN TRIANGULO ESCALENO")
    else:
           print("NO ES TRIANGULO")


if __name__=='__main__':
    main()
