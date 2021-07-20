import math
import csv
print("Bienvenido al sistema de ubicación para zonas públicas WIFI")
nombreDeUsuario = int(input("Ingrese su usuario: "))

contrasena = 63615
menu = [" 1.Cambiar contraseña"," 2.Ingresar coordenadas actuales", " 3.Ubicar zona wifi más cercana", " 4.Guardar archivo con ubicación más cercana", " 5.Actualizar registros de zonas wifi desde archivo",
         " 6.Elegir opción de menú favorita", " 7.Cerrar sesión"]
zonasWifi = [[6.211, -72.482, 2], [6.212, -72.470, 25], [6.105, -72.342, 25], [6.210,-72.442,50]]
R = 6372.795477598 #Radio de la tierra

#Función la cual contiene el resto de opciones del menú y se hace el llamado a la función de favoritos
def menuAdaptativo():
  intentos = 0

  while(intentos <= 2):
    for i in range(0, len(menu)):
     print(menu[i])

    opcion = int(input("Elija una opción: "))
    aux = opcion
    opcion -=1
    if(opcion == 0):
      opcion += 1
      cambioContrasena()
    elif(opcion == 1):
      opcion += 1
      ingresarCoordenadas()
      break
    elif(opcion == 2):
      opcion += 1
      distanciaPuntosConexion()
      break
    elif(opcion == 3):
      opcion += 1
      guardarArchivo()
      break
    elif(opcion == 4):
      opcion += 1
      actualizarRegistros()
      break
    elif(opcion == 5):
      favoritos()
    elif(opcion == 6):
        print("Hasta pronto")
        break
    elif(aux > 7):
      intentos += 1
      if(intentos ==3):
        print("Error")

#Función para que se pueda elegir la opción favorita de la persona
def favoritos():
  favorita = int(input("Seleccione opción favorita: "))
  if(favorita <=4 and favorita != 6 and favorita != 7):
    respuesta = int(input("Para confirmar por favor responda:\n¿Cuánto son tres medias moscas y mosca y media?: "))
    if(respuesta == 3):
      respuesta2 =int(input("Para confirmar por favor responda:\n¿Qué cosa será aquella que mirada del derecho y mirada del revés siempre un número es?:"))
      if(respuesta2 == 6):
        aux = favorita - 1
        quitando = menu.pop(aux)
        menu.insert(0,quitando)
      else:
        print("Error")       
    else:
        print("Error")
  else:
    print("Error")
    exit()


#Función para el cambio de contraseña
def cambioContrasena():
    nueva = int(input("Ingrese la nueva contraseña: "))
    if(nueva != contrasena and nueva != 0):
        confirmacion = int(input("Para hacer el cambio, por favor ingrese la contraseña anterior: "))
        if(confirmacion == contrasena):
            menuAdaptativo()
        else:
          print("Error")
          exit()
    else:
        print("Error")
        exit()
 
#función para imprimir una matriz
def imprimirMatrix (X):
  for i in range(3):
    for j in range(1):
      print(f"coordenada [latitud,longitud] {i+1} :", X[i], end="")
    print()

#Ingresar las coordenadas
Matriz = []
latitudSup = 6.306
latitudInf = 5.888
longitudOr = -72.321
longitudOcc = -72.552
def ingresarCoordenadas():
 if(len(Matriz) == 0):
  for i in range(3): # Ciclo de las filas
   aux_fila = []
   for j in range(1): # Ciclo de latitud
    latitud = float(input(f"ingrese latitud #{i+1}: "))
    if(latitudInf < latitud and latitud < latitudSup and latitud != None ):
      aux_fila.append(latitud)
    else:
     print("Error coordenada")
     exit()

    for k in range(1):# Ciclo de longitud
     longitud = float(input(f"ingrese longitud #{i+1}: "))
     if(longitudOcc < longitud and longitud < longitudOr and longitud != None):
      aux_fila.append(longitud)
     else:
      print("Error coordenada")
      exit()
   Matriz.append(aux_fila)#inserta los valores a la matriz
  menuAdaptativo()

 elif(len(Matriz) != 0):
   imprimirMatrix(Matriz)
   coordenadaAlSur()
   coordenadaAlOccidente()
   cambiarCoordenada()

def coordenadaAlSur():
  menor = Matriz[0][0]
  i = 0
  while(i < len(Matriz)):
    if(Matriz[i][0] < menor):
      menor = Matriz[i][0]
    i+=1
  print(f"la coordenada {menor} es la que está más al sur")

def coordenadaAlOccidente():
  menor = Matriz[0][1]
  i = 0
  while(i < len(Matriz)):
    if(Matriz[i][1] < menor):
      menor = Matriz[i][1]
    i+=1
  print(f"la coordenada {menor} es la que está más al occidente")

#Función para actualizar la coordenada que el usuario elija
def cambiarCoordenada():
  cambio = int(input("Presione 1,2 o 3 para actualizar la respectiva coordenadas\npresione 0 para regresar al menú "))
  if(cambio == 1 or cambio == 2 or cambio == 3):
    nueva_fila = []
    for i in range(len(Matriz[cambio - 1])):
      aux = float(input(f"Ingrese la nueva coordenada{i + 1}: ")) #se ingresan las nuevas coordenadas
      if(latitudInf < aux and aux < latitudSup and aux != None ):
        nueva_fila.append(aux)
      elif(longitudOcc < aux and aux < longitudOr and aux != None):
        nueva_fila.append(aux)
      else:
        print("Error")      
    Matriz[cambio - 1] = nueva_fila #acá se hace el cambio con los valores agregados en la matriz original
    menuAdaptativo()
  elif(cambio == 0):
    menuAdaptativo()
  else:
    print("Error actualización")
    exit()


distancias = []
auxub = []
def distanciaPuntosConexion():
  contador =0
  i = 0
  if(len(Matriz) != 0):
    imprimirMatrix(Matriz)
    ubicacion = int(input("Por favor elija su ubicación actual (1,2 ó 3) para calular la distancia a los puntos de conexión: "))
    if(ubicacion >= 1 and ubicacion <= 3):
      aux = ubicacion
      aux-=1
      auxub.append(aux) #guardo la opcion elegida para poder utilizarla con las distancias
      lat1 = Matriz[aux][0] #acá consigo la latitud según eligió la perosna
      long1 = Matriz[aux][1]
      while(contador < 4): #el ciclo es para poder hacer las 4 operaciones
        contador+=1        
        for j in range (1): #un for repitiendose una vez porque de una obtengo la lat2 y long2
          lat2= zonasWifi[i][j]
          long2= zonasWifi[i][j+1]
          i+=1
        deltaDeLat = lat2 - lat1
        deltaDeLong = long2 - long1
        seno = math.sin(deltaDeLat)/2
        seno2 = math.sin(deltaDeLong)/2
        distancia = 2 * R * math.asin((math.sqrt(math.pow(seno,2)) + math.cos(lat1) * math.cos(lat2)* math.pow(seno2,2)))  
        distancias.append(distancia)#creo un arreglo para poder almacenar todas las distancias
        if(len(distancias)== 4):
          mostrandoDistancias()
    else:
     print("Error ubicación")
     exit()  
  else:
    print("Error sin registro de coordenadas")
    exit()


#Una función para poder calular las distancias mas cercanas 
elementos = []
elementos2 = []
def mostrandoDistancias():
  menor = distancias[0]
  cont = 0

  for x in range(4):
    if(distancias[x]<menor):
        menor = distancias[x]
        cont = x
  distancias.pop(cont) #saco el elemento que está en la posicion del contador para así poder comparar el segundo menor

  if(len(distancias)==3):
    menor2 = distancias[0]
    for j in range(3):
      if(distancias[j]<menor2):
          menor2 = distancias[j]

  distancias.insert(cont,menor) 
  
  for y in range(4): #acá obtengo la zona wifi dependiendo de las distancias y también obtengo los usuarios
      if(menor == distancias[y]):
          usuarios = zonasWifi[y][2]
          posicion = y
      elif(menor2 == distancias[y]):
          usuarios2 = zonasWifi[y][2]
          posicion2 = y

  #acá muestro las distancias teniendo en cuenta que se muestra primero el usuario menor  
  if(usuarios < usuarios2):
    print("Zonas wifi cercanas con menos usuarios")
    print(f"La zona wifi 1: ubicada en {zonasWifi[posicion]} a {menor}, tiene promedio {zonasWifi[posicion][2]} usuarios")
    print(f"La zona wifi 2: ubicada en {zonasWifi[posicion2]} a {menor2}, tiene promedio {zonasWifi[posicion2][2]} usuarios")
    opc1 = int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
    elementos.append(opc1) #la opcion que eligió el usuario 0
    elementos.append(posicion)#la posición en el arreglo zonasWifi  1
    elementos.append(posicion2)#la posición en el arreglo zonasWifi 2
    elementos.append(menor)#El numero de usuarios 3
    elementos.append(menor2)#El numero de usuarios 4
    indicacionesLlegada()
  else:
    print("Zonas wifi cercanas con menos usuarios") 
    print(f"La zona wifi 1: ubicada en {zonasWifi[posicion2]} a {menor2}, tiene promedio {zonasWifi[posicion2][2]} usuarios")
    print(f"La zona wifi 2: ubicada en {zonasWifi[posicion]} a {menor}, tiene promedio {zonasWifi[posicion][2]} usuarios")
    opc2 = int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
    elementos2.append(opc2) #la opcion que eligió el usuario
    elementos2.append(posicion2)#la posición en el arreglo zonasWifi  
    elementos2.append(posicion)#la posición en el arreglo zonasWifi 
    elementos2.append(menor2)#El numero de usuarios 
    elementos2.append(menor)#El numero de usuarios 
    indicacionesLlegada2()

#Funcion para las indicaciones de llegada cuando usuario < usuarios2
def indicacionesLlegada():
   if(elementos[0] == 1 or elementos[0] == 2):
    c = auxub[0]
    lat1 = Matriz[c][0] #matriz de coordenadas mas frecuentadas
    long1 = Matriz[c][1]

    posicion = elementos[1]#cuando usuarios<usuarios2
    posicion2 = elementos[2]

    if(elementos[0] == 1 and lat1 < zonasWifi[posicion][0] and long1 < zonasWifi[posicion][1]):
      print("Para llegar a la zona wifi dirigirse primero al norte y luego hacia el oriente")
    elif(elementos[0] == 1 and lat1 > zonasWifi[posicion][0] and long1 > zonasWifi[posicion][1]):
      print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el occidente")
    elif(elementos[0] == 2 and lat1 < zonasWifi[posicion2][0] and long1 < zonasWifi[posicion2][1]):
      print("Para llegar a la zona wifi dirigirse primero al norte y luego hacia el oriente")
    elif(elementos[0] == 2 and lat1 > zonasWifi[posicion2][0] and long1 > zonasWifi[posicion2][1]):
      print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el occidente")
   else:
     exit(print("Error zona wifi"))
   tiempoDeLlegada()

#Funcion para las indicaciones de llegada cuando se pasa por el else
def indicacionesLlegada2():
   if(elementos2[0] == 1 or elementos2[0] == 2):
    c = auxub[0]
    lat1 = Matriz[c][0] #matriz de coordenadas mas frecuentadas
    long1 = Matriz[c][1]

    arrPosicion2 = elementos2[1]#cuando pasa por el else
    arrPosicion = elementos2[2]
    if(elementos2[0] == 1 and lat1 < zonasWifi[arrPosicion2][0] and long1 < zonasWifi[arrPosicion2][1]):
      print("Para llegar a la zona wifi dirigirse primero al norte y luego hacia el oriente")
    elif(elementos2[0] == 1 and lat1 > zonasWifi[arrPosicion2][0] and long1 > zonasWifi[arrPosicion2][1]):
      print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el occidente")
    elif(elementos2[0] == 2 and lat1 < zonasWifi[arrPosicion][0] and long1 < zonasWifi[arrPosicion][1]):
      print("Para llegar a la zona wifi dirigirse primero al norte y luego hacia el oriente")
    elif(elementos2[0] == 2 and lat1 > zonasWifi[arrPosicion][0] and long1 > zonasWifi[arrPosicion][1]):
      print("Para llegar a la zona wifi dirigirse primero al sur y luego hacia el occidente")
   else:
     exit(print("Error zona wifi"))
   tiempoDeLlegada2()

#Funcion para calcular los tiempos de llegada en moto y carro
t_llegada = []
def tiempoDeLlegada():
  if(elementos[0] == 1):
      t_Moto = elementos[3]/19.44
      t_Carro = elementos[3]/20.83
      print(f"Tiempo promedio en moto: {t_Moto}")
      print(f"Tiempo promedio en carro: {t_Carro}") 
      t_llegada.insert(0,t_Moto)
      t_llegada.insert(1,t_Carro)      
  elif(elementos[0] == 2):
      t_Moto = elementos[4]/19.44
      t_Carro = elementos[4]/20.83  
      print(f"Tiempo promedio en moto: {t_Moto}")
      print(f"Tiempo promedio en carro: {t_Carro}")   
      t_llegada.insert(0,t_Moto)
      t_llegada.insert(1,t_Carro)  
  input("Presione 0 para salir: ")
  menuAdaptativo()

t_llegada2 = []
def tiempoDeLlegada2():
  if(elementos2[0] == 2):
      t_Moto = elementos2[3]/19.44
      t_Carro = elementos2[3]/20.83
      print(f"Tiempo promedio en moto: {t_Moto}")
      print(f"Tiempo promedio en carro: {t_Carro}") 
      t_llegada2.insert(0,t_Moto)
      t_llegada2.insert(1,t_Carro)
  elif(elementos2[0] == 1):
      t_Moto = elementos2[4]/19.44
      t_Carro = elementos2[4]/20.83  
      print(f"Tiempo promedio en moto: {t_Moto}")
      print(f"Tiempo promedio en carro: {t_Carro}")
      t_llegada2.insert(0,t_Moto)
      t_llegada2.insert(1,t_Carro)     
  input("Presione 0 para salir: ")
  menuAdaptativo()

#Función para guardar datos en un archivo
def guardarArchivo():
  if(len(Matriz) != 0 and len(auxub) != 0):
    if(len(elementos)!= 0):
     c = auxub[0]
     lat1 = Matriz[c][0] #matriz de la ubicación actual
     long1 = Matriz[c][1]         
     posicion = elementos[1]#zonaWifi que la persona eligió si opc1 = 1  -- zonaWifi[posicion] 
     posicion2 = elementos[2]#zonaWifi que la persona eligió si opc1 = 2 -- zonaWifi[posicion2] 
     distancia = elementos[3]#distancia cuando opc1 = 1  
     distancia2 = elementos[4]#distancia cuando opc1 = 2 
     file = open("datos.txt","w")
     if(elementos[0] == 1):
      file.write(f"actual {lat1},{long1}"+"\n"+ f" zonaWifi {zonasWifi[posicion]}"+"\n"+ f" recorrido: [{distancia}, moto, {t_llegada[0]}] , [{distancia}, carro,{t_llegada[1]} ]")
     elif(elementos[0] == 2):
      file.write(f"actual {lat1},{long1}"+"\n"+ f" zonaWifi {zonasWifi[posicion2]}"+"\n"+ f" recorrido: [{distancia2}, moto, {t_llegada[0]}] , [{distancia}, carro,{t_llegada[1]} ]")     
     file.close

    elif(len(elementos2)!= 0):
     c = auxub[0]
     lat1 = Matriz[c][0] #matriz de la ubicación actual
     long1 = Matriz[c][1]        
     posicion2 = elementos2[1]#zonaWifi que la persona eligió si opc1 = 1  -- zonaWifi[posicion] 
     posicion = elementos2[2]#zonaWifi que la persona eligió si opc1 = 2 -- zonaWifi[posicion2] 
     distancia2 = elementos2[3]#distancia cuando opc1 = 1  
     distancia = elementos2[4]#distancia cuando opc1 = 2 
     file = open("datos.txt","w")
     if(elementos2[0] == 1):
      file.write(f"actual {lat1},{long1}" + f" zonaWifi [{zonasWifi[posicion2]}]" + f" recorrido: [{distancia2}, moto, {t_llegada2[0]}] , [{distancia2}, carro,{t_llegada2[1]} ]")
     elif(elementos2[0] == 2):
      file.write(f"actual {lat1},{long1}" + f" zonaWifi [{zonasWifi[posicion]}]" + f" recorrido: [{distancia}, moto, {t_llegada2[0]}] , [{distancia}, carro,{t_llegada2[1]} ]")
    file.close      

    f = int(input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar, 0 para regresar al menú principa"))
    if(f == 1):
      exit(print("Exportando archivo"))
    elif(f == 0):
      menuAdaptativo()
  else:
    exit(print("Error de alistamiento"))

#Función para actualizar los registros de las zonas wifi
def actualizarRegistros():
  # aux = 0
  # j = 0
  # with open("archivo.csv","r", encoding="utf8") as file:
  #   csv_read = csv.reader(file, delimiter=",")
  #   chita = list(csv_read)
  # for i,x in enumerate(chita):
  #   if(x[6] == "CHITA" and aux<=3):
  #      aux +=1  
  #      latitud = x[10].replace(",",".")
  #      longitud = x[11].replace(",",".")
  #      usuarios = x[16]          
  #      for l in range(3):
  #        if(l == 0):
  #         zonasWifi[j].append(latitud)
  #         zonasWifi[j].append(longitud)
  #         zonasWifi[j].append(usuarios)
  #        zonasWifi[j].pop(0) 
  #      j+=1
  # print(zonasWifi)
  c = int(input("Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: "))
  if(c == 0):
    menuAdaptativo()
  else:
    exit()


#Funcion para iniciar sesión por parte del usuario 
def inicioDeSesion(): 
  if(nombreDeUsuario == 51636):
   contrasenaUsu = int(input("Ingrese su contraseña: "))
   if(contrasenaUsu == contrasena):
     numero1 = nombreDeUsuario % 1000
     numero2 = int(6/(6 % 5+1))
     suma = int(input("Ingrese la suma de " + str(numero1) + " + " + str(numero2) + " = "))   
     if(suma == 639):   
       menuAdaptativo()      
     else:
       print("Error")
   else:
      print("Error")
  else:
   print("Error")

#menuAdaptativo()
inicioDeSesion()





