taxa_dolar = 5.20
taxa_euro = 6.15

valor_reais = 100.00

valor_em_euro = round(valor_reais / taxa_euro, 2)
valor_em_dolar = round(valor_reais / taxa_dolar, 2)

print(valor_em_euro," ",valor_em_dolar)

