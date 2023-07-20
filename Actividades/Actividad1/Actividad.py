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


Laboratorio()
