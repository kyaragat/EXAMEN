import funciones as fn

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martínez","Pedro Rodríguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez", "Francisco Diaz", "Helena Fernandez" ]

sueldos={trabajador: 0 for trabajador in trabajadores}

while True:
    try:
        print("---MENU---")
        print("1. Asignar sueldos aleatorios")
        print("2. Clasificar sueldos")
        print("3. Ver estadísticas")
        print("4. Reporte de sueldos")
        print("5. Salir del programa")

        opcion = int(input("Seleccione una opcion: "))

        if opcion == 1:
            sueldos = fn.asignar_sueldos(trabajadores)
            print("los sueldos son: ", sueldos)

        elif opcion ==2 :
            sueldos_menor_800, sueldos_entre_800_2m, sueldos_mayores_2m, total_sueldos= fn.clasificar_sueldos(sueldos)
            print("Sueldos menores a 800: $", sueldos_menor_800)
            print("Entre 800 y 2millones: $", sueldos_entre_800_2m)
            print("Mayores a 2millones: $", sueldos_mayores_2m)
            print("El total de los sueldos es: ", total_sueldos)

        elif opcion ==3:
            sueldo_mas_bajo, sueldo_mas_alto, promedio_sueldo=fn.ver_estadisticas(sueldos)
            print("El sueldo mas bajo es: $", sueldo_mas_bajo)
            print("El sueldo mas alto es: $", sueldo_mas_alto)
            print("El promedio de los sueldos es: $", promedio_sueldo)

        elif opcion == 4:
            fn.reporte_sueldos(sueldos)
            print("Reporte de sueldos")
            
        elif opcion ==5:
            print("Finalizando programa")
            print("Desarrollado por: Kiara Gatica")
            print("18759693-9")

            break

        else:
            print("ingrese opcion valida")

    except ValueError:
        print("ingrese valor valido")