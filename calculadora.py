primeiro_numero = int(input('Coloque o primeiro número aqui: '))
segundo_numero = int(input('Coloque o segundo número aqui: '))

print('Qual operação matemática você deseja fazer?')
print('1. Soma | 2. Subtração | 3. Multiplicação | 4. Divisão | 5. Potenciação')
escolha = input()

soma = primeiro_numero + segundo_numero
subtracao = primeiro_numero - segundo_numero
multiplicacao = primeiro_numero * segundo_numero
divisao = primeiro_numero / segundo_numero
potencia = primeiro_numero ** segundo_numero

if escolha.lower() == 'soma' or escolha == '1':
  print(f'A soma de {primeiro_numero} com {segundo_numero} é igual a {soma}!')
elif escolha.lower() == 'subtração' or escolha == '2':
  print(f'A subtração de {primeiro_numero} com {segundo_numero} é igual a {subtracao}!')
elif escolha.lower() == 'multiplicação' or escolha == '3':
  print(f'A multiplicação de {primeiro_numero} com {segundo_numero} é igual a {multiplicacao}!')
elif escolha.lower() == 'divisão' or escolha == '4':
  print(f'A divisão de {primeiro_numero} com {segundo_numero} é igual a {divisao}!')
elif escolha.lower() == 'potenciação' or escolha == '5':
  print(f'{primeiro_numero} elevado a {segundo_numero} é igual a {potencia}!')
else:
  print('Erro! Escolha uma operação listada acima')