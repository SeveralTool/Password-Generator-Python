import random
from tkinter import *

ventana = Tk()
ventana.title("Pass Generator by ST")

input = Entry(ventana, font = ("Arial 11"), width= 40)
input.grid(row= 0, column = 0, columnspan = 40, padx = 50, pady = 5)

def passGenerator():
    input.delete(0, END)
    letrasMin = "abcdefghijklmnopqrstuvwxyz" # Definimos letras en minuscula
    letrasMay = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Definimos letras en mayuscula
    nums = "1234567890" # Definimos numeros
    symbols = "$%&/@#" # Definimos algunos simbolos
    length = 32 # Establecemos el tamaño de la pass

    combinacion = letrasMin + letrasMay + nums + symbols # Creamos la combinacion de la creacion

    password = "".join(random.sample(combinacion, length)) # Usamos random y conmbinamos aleatoriamente con el tamaño max
    print(password) # Imprimimos la password
    input.insert(0, password)

botonGen = Button(ventana,text = "Generar", width= 15, height= 2 , command = lambda: passGenerator())
botonGen.grid(row = 1, column = 0, padx = 150, pady = 5)
    
ventana.mainloop()
