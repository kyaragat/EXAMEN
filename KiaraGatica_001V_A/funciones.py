import random
import csv

trabajadores = ["Juan Perez","Maria Garcia","Carlos Lopez","Ana Martínez","Pedro Rodríguez","Laura Hernandez","Miguel Sanchez","Isabel Gomez", "Francisco Diaz", "Helena Fernandez" ]

def asignar_sueldos(trabajadores):
    return {trabajador: random.randint(300000,2500000) for trabajador in trabajadores}

sueldos = asignar_sueldos(trabajadores)

def clasificar_sueldos(sueldos):
    sueldos_menor_800=[]
    sueldos_entre_800_2m=[]
    sueldos_mayores_2m=[]
    total_sueldos=[]

    for trabajador, sueldo in sueldos.items():
        if sueldo < 800:
            sueldos_menor_800.append((trabajador, sueldo))

        elif sueldo <= 800 <= 2500000:
            sueldos_entre_800_2m.append((trabajador, sueldo))

        elif sueldo > 2500000:
            sueldos_mayores_2m.append((trabajador, sueldo))

        total_sueldos=sueldos.items()

    return sueldos_menor_800, sueldos_entre_800_2m, sueldos_mayores_2m, total_sueldos

def ver_estadisticas(sueldos):
    sueldo_mas_bajo= min(sueldos.values())
    sueldo_mas_alto=max(sueldos.values())
    promedio_sueldo= sum(sueldos.values())/ len(sueldos.values())

    return sueldo_mas_bajo, sueldo_mas_alto, promedio_sueldo

def reporte_sueldos(sueldos):

    #descuento_salud= sueldos * 0.7
    #descuento_afp= sueldos * 0.12
    #sueldo_liquido= sueldos - descuento_afp - descuento_salud

    with open ('reportes_sueldos.csv','w',newline="") as archivo:
        escritor= csv.writer(archivo, delimiter=",")

        for trabajador, sueldo in sueldos.items():
            escritor.writerow([trabajador,sueldo])
    print("CSV creado")
    



    
