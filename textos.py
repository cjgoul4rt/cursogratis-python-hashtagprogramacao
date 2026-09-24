faturamento = 1000
custo = 600

lucro = faturamento - custo
# texto = 'O lucro foi de ' + str(lucro) + ' e o faturamento foi de ' + str(faturamento)
texto = f'O lucro foi de R${lucro} e o faturamento foi de R${faturamento}.'
print(texto)

email = ' EMAIL_FALSO@gmail.com'

email = email.lower() # ajusta para letras minusculas
email = email.strip() # remove espaços inuteis
print(email)

# tamanho
print(len(email))

# posicao
posicao = email.find('@')
print(posicao)

# pedacos do texto
servidores = email[posicao:]
print(servidores)

# trocar um pedaço do texto
novo_email = email.replace('gmail.com', 'proton.me')
print(novo_email)

nome = 'cj goulart'
nome = nome.capitalize()
print(nome)

nome = nome.title()
print(nome)

nome = nome.upper()
print(nome)

# formatação numérica
faturamento = 1000
custo = 600

lucro = faturamento - custo
margem = lucro / faturamento
# texto = 'O lucro foi de ' + str(lucro) + ' e o faturamento foi de ' + str(faturamento)
texto = f'O lucro foi de R${lucro:,.2f} e o faturamento foi de R${faturamento:,.2f} e a margem foi de {margem:.2%}'
print(texto)

# exercicio
nome = 'cj brabo goulart'
email = 'cj_o_brabo@proton.me'

# descubra o servidor do email
posicao = email.find('@')
servidor = email[posicao:]
print(servidor)


# descubra o 1o nome do usuário

# criar uma mensagem dizendo 'usuario tal cadastrado com sucesso no email tal'
