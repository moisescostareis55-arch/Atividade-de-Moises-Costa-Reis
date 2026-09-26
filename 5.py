def calcular_desconto(preco, desconto):
    return preco - (preco * desconto / 100)


preco = float(input("Digite o preço: "))
desconto = float(input("Digite o desconto (%): "))

resultado = calcular_desconto(preco, desconto)

print("Preço final: R$", resultado)