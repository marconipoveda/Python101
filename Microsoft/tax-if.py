pais = input("¿De qué país viene?: ")
tax = 0

if pais.lower() == 'canada':
    provincia = input("Provincia: ")
    if provincia in('Alberta','Ontario','Yukon'):
        tax = 0.05
    elif provincia == 'Quebec':
        tax = 0.13
    else:
        tax = 0.15
print(tax)