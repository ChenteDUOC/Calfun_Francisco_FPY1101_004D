#Hecho por Vicente, Crsitobal, Gustavo
#Se importan las bibliotecas
import csv,time
#Se definen las listas
titulo=["Nombre","Edad","Curso","Promedio"]
lista_estudiante=[]
# Interfaz Menu
def desplegar_Menu():
    while True:
        try:
            opcion = int(input("¿Que desea realizar?\n1.- Agregar estudiante.\n2.- Ver todos los estudiantes.\n3.- Modificar Estudiantes\n4.- Eliminar Estudiantes\n5.- Guardar colecciión en un archivo\n6.- Salir del programa.\n> "));
            if opcion not in [1,2,3,4,5,6]:
                raise ValueError
        except ValueError:
            print("Ingrese una opción válida. (1 - 6)")
            continue
        break
    return opcion        

# Opcion 1
# Hecho por Cristobal
def agregar_Estudiante():
    while True:
        nombre=input("Ingrese el nombre del estudiante:")
        print("\n--Se ingreso de manera correcta el nombre del estudiante--")
        
        edad=input("Ingrese la edad el estudiante:")
        print("\n--Se ingreso de manera correcta la edad del estudiante--")
        
        curso=input("Ingrese el curso del estudiante:")
        print("\n--Se ingreso de manera correcta el curso del estudiante--")
        try:
            while promedio not in [1,7]:
                promedio=float(input("Ingrese el promedio del estudiante:"))
                if promedio<1 or promedio>7:
                    print("\n--Se ingreso de manera correcta el promedio del estudiante--")
        except:
            print("Ingrese un valor valido")
        else:
            lista_estudiante.append([nombre, edad, curso, promedio]);
        while True:
            try:
                repetir = int(input("¿Quiere agregar otro estudiante?\n1.- Si\n2.- No\n> "))
                if repetir not in [1,2]:
                    raise ValueError
            except ValueError:
                print("Ingrese una respuesta válida.");
                continue
            if repetir == 1:
                break
            elif repetir == 2:
                break
        if repetir == 2:
            print("\n")
            break
#Opcion 6 
#Hecho por Gustavo Santana 
def animacion_salir():
    print("Saliendo del programa",end="")
    for x in range(3):
        print(".",end="",flush=True)
        time.sleep(0.5)

# Opcion 5
#Hecho por Gustavo Santana
def plantilla():
    with open("Estudiantes.csv","w",newline="", encoding="UTF-8") as archivo_csv:
        escritor_csv=csv.writer(archivo_csv)
        escritor_csv.writerow(titulo)
        escritor_csv.writerows(lista_estudiante)

# Opcion 2
#Hecho por Gustavo Santana
def mostrar_Estudiantes():
    for x in lista_estudiante:
        print(x)
    print("Estos son todos los estudiantes registrados")


# Opcion 4
# Aqui trabajo Vicente Alarcón

def eliminar_Estudiante():
    l = 1
    if lista_estudiante:
        print("Estudiantes registrados:");
        for estudiante in lista_estudiante:
            print(f"{l}", estudiante);
            l += 1;
        while True:
            try:
                eliminar = int(input("> "))
                if eliminar not in range(1, l):
                    raise ValueError
            except ValueError:
                print("Ingrese un estudiante válido.")
                continue
            eliminar -= 1;
            lista_estudiante.pop(eliminar);
            while True:
                try:
                    repetir = int(input("¿Quiere eliminar a otro estudiante?\n1.- Si\n2.- No\n> "))
                    if repetir not in [1,2]:
                        raise ValueError
                except ValueError:
                    print("Ingrese una opcion válida.")
                    continue
                if repetir == 1:
                    break
                elif repetir ==2:
                    break
            if repetir == 2:
                break




