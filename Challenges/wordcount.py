#!/usr/bin/env python3
import sys

# Definir la función print_words(filename) y la función print_top(filename).
def print_words(filename: str) -> None:
    f = open(filename,'r')
    #print(f.read())
    worddepot = {}
    #Separate the file in lines and read each line
    for line in f:
        #Count the times a word appears in every line
        wordcounter(line.strip().split(' '), worddepot)
    
    #Print the list of words and the times it appears on the text one word at a time.
    for item in worddepot.items():
        print (item)

#Count how many times the word appears in the text
#This function receives the list of words sliced (wordlist) and a dictionary (worddepot) where we will store
#the word (as the key) and the counter of appearances (as the value)
def wordcounter(wordlist, worddepot):
    for word in wordlist:
        if word != '':
            #Add one everytime the words repeats in the text.
            if word.lower() in worddepot:
                worddepot[word.lower()] += 1
            #Initialize 
            else:
                worddepot[word.lower()] = 1

def print_top(filename: str) -> None:
    
    f = open(filename,'r')
    worddepot = {}
    for line in f:
        wordcounter(line.strip().split(' '), worddepot)

    b = orderwords(worddepot)
    print('20 most repeated words: {}'.format(b[:20]))


def orderwords(listwords):
    words=[(word, count) for word, count in listwords.items()]
    return sorted(words, key=lambda x: x[1], reverse=True)

# Escribir unn programa que lea un archivo y cuente la frecuencia con la que cada palabra 
# aparece en el archivo. El programa debe aceptar uno de dos argumentos --count que muestra 
# todas las palabras y el número de veces que aparece en el archivo; o --topcount que muestra
# las 20 palabras más frecuentes ordenadas de mayor a menor según la frecuencia con la que aparecen 
# en el archivo.
#
# El código para manejar los argumentos de línea de comando ya está provisto
# junto con las llamadas a las funciones print_words() y print_top() que usted debe definir.
def main():
    if len(sys.argv) != 3:
        print('uso: ./wordcount.py {--count | --topcount | --countlines} file')
        sys.exit(1)

    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    elif option == '--countlines':
        print_lines(filename)
    else:
        print(f'Opcion desconocida: {option}')
        sys.exit(1)

if __name__ == '__main__':
    main()