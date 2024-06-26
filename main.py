#Hecho por Gustavo Santana, Cristobal Valdebenito, Vicente Alarcón
import funciones as func

print("--- Bienvenido Docente ---");
print("--- Aqui usted podra agregar, eliminar, mostrar, modificar y\n ver la planilla de los estudiantes agregados ---")
while True:
    
    opcion = func.desplegar_Menu()
    
    if opcion == 1:
        func.agregar_Estudiante()
    elif opcion == 2:
        func.mostrar_Estudiantes()        
    elif opcion == 3:
        func.modificar_Estudiantes()
    elif opcion == 4:
        func.eliminar_Estudiantes()
    elif opcion == 5:
        func.plantilla()
    elif opcion == 6:
        func.animacion_salir()
        