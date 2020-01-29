x = 9
y = 0

try:
    print(x/y)
except ZeroDivisionError as e:
    print('División por 0 no permitida')
else:
    print('alguna otra cosa salió mal')
finally:
    print('Clean up code')