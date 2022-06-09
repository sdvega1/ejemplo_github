from datetime import date

def calcular_edad(fecha_nacimiento):
    fecha_actual = date.today()
    resultado = fecha_actual.year - fecha_nacimiento.year

    return resultado

mi_fecha = date(1979, 1, 22)
edad = calcular_edad(mi_fecha)

print(edad)