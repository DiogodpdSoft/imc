print('**************************************************') #Primeiras 3 linhas do código utilizado para estilizar e apresentar o programa
print('****************Calculadora ICM*******************')
print('*******************Diogo Dias*********************')

peso = float(input('Qual é o seu peso? (Kg) ' )) #Criado a variável peso seguido de float por representar numeros reais Kg. E o input para a pessoa digitar os seus kg.
altura = float(input('Qual é a sua altura? (m) ')) #Criado a variável altura seguido de float por representar numeros reais em metros. E o input para a pessoa digitar sua altura
imc = peso / (altura **2) #Criado a variável imc que se irá fazer o calculo do peso, divido pela altura ao quadrado
print('O IMC dessa pessoa é de {}'.format(imc)) #Print quer irá sair o resultado do calculo do valor do imc da pessoa
if imc< 18.5: #Valor do imc for abaixo de 18.5 sairá a mensagem que esta no print da próxima linha
  print('Você esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25: #Valor do imc for igual a 18.5 até 25 aparecerá a mensagem do print da próxima linha
  print('PARABÉNS, você está na faixa de PESO NORMAL')
elif 25<= imc< 30: #Valor do imc for igual a 25 até 30 aparecerá a mensagem do print da próxima linha
  print('Você está em SOBREPESO')
elif 30 <= imc < 40: #Valor do imc for igual a 30 até 40 aparecerá a mensagem do print da próxima linha
  print('Você está em Obesidade')
elif imc >= 40: #Valor do imc for maior que 40 aparecerá a mensagem do print da próxima linha
  print('Você esta em Obesidade Mórbida, cuidado!')
