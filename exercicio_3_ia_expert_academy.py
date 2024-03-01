# Exercício - 3: IA Expert Academy

# Cálculo de consórcio

valor_total = float(input("Qual é o valor total do consórcio? "))
qtd_parcelas = int(input("Em quantas parcelas?(em meses) "))
taxa_adm = float(input("Qual é a taxa de administração? "))

parcela = valor_total / qtd_parcelas
juros = (taxa_adm / 100) * parcela
total = parcela + juros
valor_total = (total * qtd_parcelas)

print(f'Parcela: R$ {parcela:.2f}')
print(f'Juros: R$ {juros:.2f}')
print(f'Total: R$ {total:.2f} ao mês')
print(f'O valor total R$ {valor_total:.2f}')

# Saldo devedor

parcelas_pagas = int(input("Quantas parcelas foram pagas? "))

saldo_devedor = valor_total - (parcelas_pagas * total)

print(f'Você pagou {parcelas_pagas} parcelas de {qtd_parcelas}')
print(f'Saldo devedor: R$ {saldo_devedor:.2f}')