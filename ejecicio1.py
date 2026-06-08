agenda={}
nombres=[]
telefonos=[] #se crearon lista para el diccionario
for x in range(3):
    nombre=input("Ingresar nombre: ")
    telefono=int(input("Ingresar teléfono: "))
    nombres.append(nombre) #esto es paara insertar los nombres a la lista 
    telefonos.append(telefono)
    

agenda["nombres"]=nombres #para guardar las listas al diccionario
agenda["telefonos"]=telefonos

for x in agenda:
    print (x,"->",agenda[x])


#ejercicio 1: forma 2: 
agenda=[]
for x in range(3):
    nombre=input("Ingresar nombre: ")
    telefono=int(input("Ingresar teléfono: "))
    contacto = {
        "nombre":nombre,
        "telefono":telefono,
    }
    agenda.append(contacto)

for x in agenda:
    print(x["nombre"],"->",x[telefono]) #x es un diccionario