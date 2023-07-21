def FruitManzana():
    kilos = float(input("Kilos de Manzana: "))
    kiloManzana = 2000

    def Calculo(kilos, kiloManzana, descuento):

        valorTotal = kiloManzana * kilos

        return valorTotal * descuento

    if (kilos <= 2 and kilos > 0):
        Valor = Calculo(kilos, kiloManzana, 1)

    elif (kilos > 2 and kilos <= 5):
        Valor = Calculo(kilos, kiloManzana, 0.9)
        print("Descuento del 10%")
    elif (kilos > 5 and kilos <= 10):
        Valor = Calculo(kilos, kiloManzana, 0.85)
        print("Descuento del 15%")
    elif (kilos > 10):
        Valor = Calculo(kilos, kiloManzana, 0.8)
        print("Descuento del 20%")

    print(
        f"Con el kilo de manzana costando:{kiloManzana} \nel valor a pagar es: {Valor}")


def Laboratorio():
    nivelH = int(input("Coloque la hemoglobina: "))
    sexo = input("Coloque el sexo M/masculino, F/Femenino: ")
    sexo = sexo.capitalize()

    print("Edad del Paciente la dara por meses? ")

    # CAlCULO
    def CalculoHemoglobina(nivelH, mes, primerRango, segundoRango):
        if (mes):
            if (nivelH > primerRango and nivelH < segundoRango):
                return True
            else:
                return False

        else:
            if (nivelH > primerRango and nivelH < segundoRango):
                return True
            else:
                return False

    # opciones
    res = input(" y/si - n/no -> ")
    res = res.capitalize()
    print(res)

    if (res == "Y"):
        edad = int(input("Coloque los meses de edad: "))
        mes = True
    else:
        edad = float(input("Coloque los años de edad: "))
        mes = False
    # logica

    if (mes):
        if (edad > 0 and edad <= 1):
            resultado = CalculoHemoglobina(nivelH, mes, 13, 26)
        elif (edad > 1 and edad <= 6):
            resultado = CalculoHemoglobina(nivelH, mes, 10, 18)
        elif (edad > 6 and edad <= 12):
            resultado: bool = CalculoHemoglobina(nivelH, mes, 11, 15)
        else:
            print("Meses invalidos...")
            return

    else:
        if (edad > 1 and edad <= 5):
            resultado: bool = CalculoHemoglobina(nivelH, mes, 11.5, 15)
        elif (edad > 5 and edad <= 10):
            resultado: bool = CalculoHemoglobina(nivelH, mes, 12.6, 15.5)
        elif (edad > 10 and edad <= 15):
            resultado: bool = CalculoHemoglobina(nivelH, mes, 13.6, 15.5)
        elif (edad > 15 and sexo == "M"):
            resultado: bool = CalculoHemoglobina(nivelH, mes, 14, 18)
        elif (edad > 15 and sexo == "F"):
            resultado: bool = CalculoHemoglobina(nivelH, mes, 12, 16)
        else:
            print("Error de edad...")

    verifMes = "Afirmativo" if mes else "Negativo"
    verifResult = "Positivo" if resultado else "Negativo"
    verifSexo = "Femenino" if sexo == "F" else "Masculino"

    if (resultado):
        print(F""" \n ***
Resultados del Paciente.
Anemia: {verifResult}.
Sexo: {sexo}
Edad:{edad} ¿se cuenta en Meses?: {verifMes}
***
""")
    else:
        print(F""" \n ***
Resultados del Paciente.
Anemia: {verifResult}.
Sexo: {sexo}
Edad:{edad} ¿se cuenta en Meses?: {verifMes}
***
""")


def InstitucionEduc():
    inProValue = float(input("Coloque el promedio del alumno: "))

    print("Coloque la opcion que corresponda al alumno.")
    print("Preparatoria-> 1 | Profesional-> 2")
    inPr = int(input("Opcion: "))
    if (inPr > 0 and inPr < 3):
        inPr = "Profesional"if inPr == 2 else "Preparatoria"
    else:
        print("Error al escoger la opcion")
        return

    # Valores predeterminados
    # "Profesional": 60,
    # "Preparatoria": 36
    # Funcion para calcular
    def CalcularUnidades(unidades, descuento, tipoAlumno, Reprobo, promedio):
        NotasReprobadas = 0
        if (Reprobo):
            NotasReprobadas = int(input("Coloque las notas que a reprobado: "))

        unidad = 60 if tipoAlumno == "Profesional" else 36

        total = (unidad * unidades)
        totalConDescuento = total * descuento

        descuento = 0 if descuento == 0 else (100 % descuento)*100

        return f"""
        ***
El alumno cursando su etapa {tipoAlumno} 
tiene un Promedio de {promedio} con {NotasReprobadas} notas reprovadas 
se le dara una oportunidad de {unidades} unidades 
que tienen en cuenta que la unidad del {tipoAlumno} sale en ${unidad}  
y con un descuento del {descuento}% 
el total sera de: {total}$ y si hay descuento: {totalConDescuento}$
        ***
"""

    if (inProValue < 0 and inProValue > 10.1):

        print("promedio no valido...")
        return

    # preparatiroa
    if (inProValue >= 9.5 and inPr == "Preparatoria"):
        response = CalcularUnidades(55, 0.75, inPr, False, inProValue)

    elif (inProValue >= 9 and inProValue < 9.5 and inPr == "Preparatoria"):
        response = CalcularUnidades(50, 0.9, inPr, False, inProValue)

    elif (inProValue >= 7 and inProValue < 9 and inPr == "Preparatoria"):
        response = CalcularUnidades(45, 0, inPr, False, inProValue)
    elif (inProValue < 7 and inPr == "Preparatoria"):
        response = CalcularUnidades(40, 0, inPr, True, inProValue)

    # profesional
    elif (inProValue >= 9.5 and inPr == "Profesional"):
        response = CalcularUnidades(55, 0.8, inPr, False, inProValue)
    elif (inProValue < 9.5 and inPr == "Profesional"):
        response = CalcularUnidades(55, 0, inPr, False, inProValue)

    # response

    print(response)


def numerosDiferentes():
    numeros = []
    print(" *** Numeros diferentes ***")
    while len(numeros) < 3:
        saltar = False
        numero = int(input("Coloque numero: "))

        if len(numeros) == 0:
            numeros.append(numero)
        else:
            for x in numeros:
                if x == numero:
                    print("coloque un numero distinto al que ya a puesto")
                    saltar = True
                    break
            if not saltar:
                numeros.append(numero)
            else:
                pass

    numerosCadena = [str(numero) for numero in numeros]
    print(numerosCadena)
    NumerosOrdenados = ", ".join(numerosCadena)

    print(f"""\n
Los numeros ingresados son { NumerosOrdenados }.
siendo el numero del medio {numeros[1]} 
"""
          )


def Reforestacion():
    print("\t Reforestar por Hectareas")

    def CalcularTerreno(supTerreno):

        hectarea = supTerreno / 10000

        if supTerreno > 1000000:
            pino = 0.7
            oyamel = 0.2
            cedro = 0.10
        else:
            pino = 0.5
            oyamel = 0.3
            cedro = 0.2

        sembrarPino = hectarea * pino
        sembrarOyamel = hectarea * oyamel
        sembrarCedro = hectarea * cedro

        return sembrarPino, sembrarOyamel, sembrarCedro, hectarea

    supTerreno = float(
        input("introduzca el tamaño del terreno por metros cuadrados: "))

    pino, oyamel, cedro, hectarea = CalcularTerreno(supTerreno)
    print(f"Arboles de pino:{pino}")
    print(f"Arboles de oyamel:{oyamel}")
    print(f"Arboles de cedro:{cedro}")
    print(f"De: {supTerreno:,} m^2 . Un total de: {hectarea:,} Hectareas")
    # no muy claro


def NumeroMenor():
    numeros = []
    cantidad = int(input("Ingrese la cantidad de numeros a ingresar"))

    for i in range(cantidad):
        numeros.append(int(input("Coloque Numero: ")))

    minimo = min(numeros)
    repetidos = numeros.count(minimo)

    numerosCadena = [str(numero) for numero in numeros]
    numerosCadena = ", ".join(numerosCadena)

    print(
        f"de la lista de numeros {numerosCadena} el menor es: {minimo} y se repite {repetidos} veces")


def SeñoraSupermercado():
    carrito = {}
    print("""
\t Compras en el super mercado
escoja la opcion "s" para si y "n" para no.
""")

    def CalculoArticulo(articulo, cantidad, valor):
        if articulo in carrito:
            carrito[articulo].extend([valor] * cantidad)
        else:
            carrito[articulo] = [valor] * cantidad

    while True:
        option = input("opcion -> ")
        option = option.capitalize()
        if option == "S":
            articulo = input("Escoja el articulo: ")
            cantidad = int(input("Cantidad del articulo que se llevará: "))
            valor = float(input("Valor del articulo: "))
            CalculoArticulo(articulo, cantidad, valor)
        elif option == "N":
            break
        else:
            print("Error al ingresar opcion, s/si - n/no")

        print(f"\n\t El carrito tiene: ")
        for art, can in carrito.items():
            print(
                f"{art} con una cantidad de {len(can)} y con un precio de {can[0]:,}$")
        print("\n")

    carrito
    print("\tTotal de Compras:")
    total = 0
    for art, can in carrito.items():
        total += sum(can)
        print(
            f"{art} con una cantidad de {len(can)} y con un precio de {sum(can):,}$")
    print(f"en total: {total:,}\n")


def CajeroSupermercado():
    clientes = {}
    list = []

    print("""
\t Caja registradora
Si ya acabo el dia diga "n" de lo contrario "y"
""")

    def CalculoArticulo(nombre, articulo, cantidad, valor):
        total = cantidad * valor
        if nombre in clientes:
            clientes[nombre].update({"Articulo": articulo, "Precio": valor})
        else:
            clientes[nombre] = {"Articulo": articulo, "Precio": valor}

    while True:
        option = input("opcion -> ")
        option = option.capitalize()
        if option == "S":
            nombre = input("Nombre del Cliente: ")
            articulo = input("Escoja el articulo: ")
            cantidad = int(input("Cantidad del articulo que se llevará: "))
            valor = float(input("Valor del articulo: "))

            CalculoArticulo(nombre, articulo, cantidad, valor)
            print("\n")
        elif option == "N":
            break
        else:
            print("Error al ingresar opcion, s/si - n/no recuerde: Si ya acabo el dia diga 'n' de lo contrario diga 's'")

        print("Clientes atendidos")
        if len(clientes) == 0:
            pass
        else:
            for client, obj in clientes.items():
                print(f"Cliente: {client}")
                for key, value in obj.items():
                    print(f"{key}:{value}")
            print("\n")

    for client, obj in clientes.items():
        print(f"{client}")
        for key, value in obj.items():
            print(f"{key}:{value}")
            if isinstance(value, (int, float)):
                list.append(value)

    print(list)


CajeroSupermercado()
