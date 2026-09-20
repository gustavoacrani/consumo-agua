# Entrada de dados
tipo = input("Tipo de imóvel (comercial, casa ou apartamento): ").lower()

# Validação do tipo de imóvel
if tipo not in ["comercial", "casa", "apartamento"]:
    print("Tipo de imóvel inválido. Por favor, insira 'comercial', 'casa' ou 'apartamento'.")
else:
    # Entrada de consumo
    consumo = float(input("Consumo mensal de água (m³): "))

    # Classificação
    if tipo == "comercial":
        print("Tarifa comercial aplicada – consulte o plano corporativo.")

    elif tipo == "apartamento" and consumo < 10:
        print("Consumo econômico – excelente controle de água!")

    elif (tipo == "apartamento" or (tipo == "casa") and consumo <= 25:
        print("Consumo moderado – dentro do padrão residencial.")

    else:
        print("Consumo excessivo – adote medidas de economia e verifique vazamentos.")
