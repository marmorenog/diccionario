# DICCIONARIOS: llave - valor (key-value)
persona = {
    "rut":16666,
    "nombre":"Elsa",
    "apellido":"Pato",
    "edad": 25,
    "altura": 1.65,
    "usa_lentes": True
}

print(persona) #no es buena práctica
print(persona["rut"])


#Vamos a ver como recorrer un diccionario:

for x in persona: #la x es la llave
    print(x,"-",persona[x]) 


#Comandos de utilidad de los diccionarios:

print (persona.keys()) #imprime las llaves
print(persona.values()) #imprime los nombres de los valores
print(persona.items()) #impreme ambos

#vamos a modificar el diccionario:

print (persona)
persona["mascota"] = "Cholito" # es para agregar el valor al diccionario , si la llave no existe la agrega!
persona["edad"] = 26 #si la llave existe modifica el valor 
persona["edad"] +=1

# edad = int(input("Ingrese la edad: "))
#persona["edad"]=edad

print(persona)