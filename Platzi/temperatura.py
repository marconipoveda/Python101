import random

def filltemps(cant):
    temps=[]
    i=0
    while i < cant:
        temps.append(random.randint(-10,38))
        i+=1

    return temps

def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += temp

    return (sum_of_temps / len(temps))

if __name__ == "__main__":
    cant=int(input('Defina cantidad de temperaturas: '))
    temps = filltemps(cant)
    average = average_temps(temps)
    print(temps)
    print('La tempertura promerdio es: {0:.4f}'.format(average))