faturamento = 1100
custo = 600
lucro = faturamento - custo

print('Faturamento', faturamento)
novas_vendas = 1000

faturamento = faturamento + novas_vendas

imposto = 0.15 * faturamento # float
print(imposto)

lucro = faturamento - custo - imposto
print('Faturamento', faturamento)
print('Custo', custo)
print('Lucro', lucro)

margem_lucro = lucro / faturamento
print('Margem', margem_lucro)

# int = numeros inteiros
# float = numeros decimais
# str = textos
# bool = booleanos (true or false)

# operadores especiais

# mod -> %
# resto da divisão de um número pelo outro
# 10 % 3

anos = int(310 / 12)
print(anos, 'anos')

meses = 310 % 12
print(meses, 'meses')

# floor division -> //
print(310 // 12)

