import json

with open('C:/Users/lucas/Downloads/Target/dados.json') as json_file:
    faturamento_dados = json.load(json_file)

faturamento_real = [dia['valor'] for dia in faturamento_dados if dia['valor'] > 0]

menor_faturamento = min(faturamento_real)
maior_faturamento = max(faturamento_real)

media_mensal = sum(faturamento_real) / len(faturamento_real)

dias_acima_da_media = sum(1 for valor in faturamento_real if valor > media_mensal)

print(menor_faturamento, maior_faturamento, dias_acima_da_media)

