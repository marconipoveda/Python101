def run():
    print('CALCULADORA DE DIVISAS')
    print('convierte de córdobas a dólares')
    print()

    ammount = float(input('Ingrese la cantidad de Córdobas: '))

    resultado=cambio_moneda(ammount)

    print('C${} córdobas equivalen a ${} dólares!'.format(ammount, resultado))

def cambio_moneda(ammount):
    cordxdolar = 34.5

    return ammount / cordxdolar


if __name__ == '__main__':
    run()
