#integrantes = ["Valeria", "Carlos", "Fernando", "Alejandro"]

integrantes = [] #se declara la lista vacía
for nombre in range(0, 4): #iteración en la que se ejecuta lo que sigue
    nombre = input("Ingrese el nombre de un integrante ") #solicita el ingreso del nombre del integrante
    integrantes.append(nombre) #va llenando la lista con los nombres ingresados

x=(", ".join(integrantes)) #transforma la lista en string y los separa con comas
y=(" ¡Felicidades!, Adalid les asegura trabajo una vez completado el BootCamp") #el string es asignado a la variable
w= (x.upper() + y.upper()) #vuelve mayúscula y luego suma dos cadenas
print(w) #imprime el mensaje más los input, todo en mayúscula
z = str.split(y) #Convierte string en lista
print(z + integrantes) #imprime la lista de integrantes más el mensaje (previamente convertido en lista)

for i in integrantes:
    print(i , "está en el índice", integrantes.index(i)) #iteración ára imprimir el índice o ubicación de los integrantes
    
print(len(w.split())) #lo que imprime el número de palabras del mensaje y los integrantes
q=tuple(z + integrantes) #suma dos listas, y las vuelve una tupla
print(q) #lo que imprime la tupla



#print(y + integrantes)
#print (x.upper() + y.upper())









#Prueba que no hemos podido resolver
#integrante=['valeria','carlos']
#print("Trabajo " ,*integrante, sep = ', ')