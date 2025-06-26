entradas = {
    "Fortificados":[],
    "Iluminados":[]
}

stock_max = 500

def validar_codigo(codigo, nombre_concierto):
    if len(codigo) < 6:
        return False
    tiene_mayusculas = any(c.isupper() for c in codigo)
    tiene_numeros = any(c.isdigit() for c in codigo)
    sin_espacios = " " not in codigo
    contiene_nombre = nombre_concierto.lower() in codigo.lower()
    return tiene_mayusculas and tiene_numeros and sin_espacios and contiene_nombre

def comprar_entrada(nombre_concierto):
    if len(entradas[nombre_concierto])>= stock_max:
        print(f"Stock agotado para: '{nombre_concierto}'")
        return
    nombre = input("Ingrese Nombre del Comprador:")
    tipo = input("Tipo de entrada (CVG/PAL):")
    codigo = input("Ingrese codigo de confirmacion:")

    if validar_codigo(codigo, nombre_concierto):
        entradas[nombre_concierto].append({
        "nombre": nombre,
        "tipo": tipo,
        "codigo": codigo
        }) 
        print(f"Entrada registrada con exito para: {nombre_concierto}")
    else:
        print("Error codigo de confirmacion invalido")

def stock():
    vendidad_f = len(entradas["Fortificados"])
    vendidad_i = len(entradas["Iluminados"])
    disponible_f = stock_max - vendidad_f
    disponible_i = stock_max - vendidad_i
    print(f"Entradas disponibles para 'los Fortificados': {disponible_f}")
    print(f"Entradas disponibles para 'los Iluminados': {disponible_i}")
def menu():
    while True:
        print("----TOTEM AUTOSERVICIO CONCIERTOS ROCK AND CHILE---")
        print("1.-Comprar Entrada a Los Fortificados")
        print("2.-Comprar Entrada a Los Iluminados")
        print("3.-Stock De Entradas Para Ambos Conciertos")
        print("4.-Salir")
        try:
            opcion = int(input("Ingrese opcion:"))
        except ValueError:
            print("Ingrese un dato numerico")
        if opcion == 1:
            comprar_entrada("Fortificados")
        elif opcion == 2:
            comprar_entrada("Iluminados")
        elif opcion == 3:
            stock()
        elif opcion == 4:
            print("Programa terminado...")
            break
        else:
            print("Opcion invalida.")
menu()