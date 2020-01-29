def suma(num1, num2):
    return num1 + num2

def main():
    num1 = input('Ingrese el primer número! ')
    num2 = input('Ingrese el segundo número! ')
    
    
    print(suma(int(num1), int(num2)))

if __name__ == '__main__':
    main()