def converter_minutos(horas):
    return horas * 60
horas = int(input("Digite a quandtidade de horas: "))
resultado = converter_minutos(horas)
print("Isso corresponde a", resultado, "minutos.")