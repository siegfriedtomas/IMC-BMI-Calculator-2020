print("""Bienvenido al programa "¿Estas gordito o no? versión 2020" """)

# Diccionario que recopila los datos del usuario
persona={"Nombre": "","Apellido": "","Edad": "","Peso (en Kg)": 0,"Altura (en Mts)": 0,"Dirección": "","Teléfono": ""}

# Función que, según el valor final del IMC, te devuelve la categoría en la que estás.
def cat_imc(imc):
    if imc < 18.5:
        print("""Usted está en la categoria "Bajo Peso" """)
    elif imc < 24.9:
        print("""Usted está en la categoria "Peso Normal" """)
    elif imc < 29.9:
        print("""Usted está en la categoria "Sobre Peso" """)
    elif imc < 34.9:
        print("""Usted está en la categoria "Obesidad Tipo 1" """)
    elif imc < 39.9:
        print("""Usted está en la categoria "Obesidad Tipo 2" """)
    elif imc > 40:
        print("""Usted está en la categoria "Obesidad Tipo 3" """)

# Función que imprime los datos del usuario al finalizar el programa.
def imprimir():
    for dato in persona:
        print (dato, ":", persona[dato])

for i in persona:
    persona[i]=input(f"Ingrese su {i} :")

imc=round(float(persona["Peso (en Kg)"]) / (float(persona["Altura (en Mts)"])**2),5)

persona["IMC"]=imc

print("---------------------------------------------------------")

imprimir()
cat_imc(imc)

print("---------------------------------------------------------")