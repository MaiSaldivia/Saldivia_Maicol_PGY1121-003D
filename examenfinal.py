from os import system
import random
from statistics import geometric_mean 
system("cls")


trabajadores=["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
sueldos=[]


while True:
    op=input("Ingrese una opción: ")
    match op:
        case "1":
            #Asignar sueldos aleatorios
            global sueldo
            sueldos=[random.randint(300000,2500000) for i in range (len(trabajadores))]
            print("Sueldos asignados de forma aleatoria entre 300.000 y 2.500.000")

        case "2":
            #Clasificar sueldos
            print("Función para mostrar la lista de empleados con su sueldo y clasificación")
            menores800k=[(trabajadores[i],sueldos[i]) for i in range(len(sueldos)) if sueldos[i]<800000]
            entre800ky2M=[(trabajadores[i],sueldos[i]) for i in range(len(sueldos))if 800000<=sueldos[i]>=2000000]
            mayores2M=[(trabajadores[i],sueldos[i]) for i in range(len(sueldos))if sueldos[i]>2000000]
            
            print(f"Sueldos menores a $800.000 TOTAL: {len(menores800k)}")
            for nombre,sueldo in menores800k:
                print(f"Nombre empleado:{nombre}    Sueldo: ${sueldo}")

            print(f"Sueldos entre $800.000 y $2.000.000 TOTAL:{len(entre800ky2M)}")
            for nombre,sueldo in entre800ky2M:
                print(f"Nombre empleado:{nombre}    Sueldo: ${sueldo}")

            print(f"Sueldos superiores a $2.000.000 TOTAL:{len(mayores2M)}")
            for nombre,sueldo in mayores2M:
                print(f"Nombre empleado:{nombre}    Sueldo: ${sueldo}")

            print(f"TOTAL SUELDOS: $ {sum(sueldos)}")


        case "3":
            #Ver estadísticas
            sueldomasalto=max(sueldos)
            sueldomasbajo=min(sueldos)
            promediosueldos=sum(sueldos)/len(sueldos)
            Mediageometrica=geometric_mean(sueldos)
            
            print(f"""Estadísticas:
                1.- Sueldo más alto: ${sueldomasalto}
                2.- Sueldo más bajo: ${sueldomasbajo}
                3.- Promedio de sueldos: ${promediosueldos}
                4.- Media geométrica: ${Mediageometrica}
                """)
            
        case "4":
            #Reporte de sueldos
            DescSalud=[sueldo*0.7 for i in sueldos]
            DescAFP=[sueldo*0.12 for i in sueldos]
            Sueldoliquido=[sueldo[i]-DescSalud[i]-DescAFP[i]]
            for i in range(len(trabajadores)):
                print(f"""Nombre empleado:{trabajadores[i]}    Sueldo Base:${sueldos[i]}     Descuento Salud:${DescSalud[i]}     Descuento AFP{DescAFP[i]}   Sueldo Líquido:${Sueldoliquido[i]}
                  """)
            archivo=open(f"examen.csv","w")
            archivo.write(f"""Nombre empleado:{trabajadores[i]}    Sueldo Base:${sueldos[i]}     Descuento Salud:${DescSalud[i]}     Descuento AFP{DescAFP[i]}   Sueldo Líquido:${Sueldoliquido[i]}""")
            archivo.close()
            #Estos datos se deben exportar a un archivo de texto (.csv)

        case "5":
            #Salir del programa
            print("Finalizando programa...\nDesarrollado por Maicol Saldivia\nRUT 20.515.077-3")
            break
        case other:
            print("Opción inválida. Ingrese la opción nuevamente")





