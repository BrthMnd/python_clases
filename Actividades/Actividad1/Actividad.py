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
el total sera de: {total} y si hay descuento: {totalConDescuento}
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


InstitucionEduc()
