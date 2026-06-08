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