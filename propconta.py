class Conta:
  def __init__(self, numero, nome, valor):
    self.__numero = numero
    self.__titular = nome
    self.__saldo = valor
    
  @property
  def titular(self):
    return self.__titular
  
  @titular.setter
  def titular(self, novotitular):
    if novotitular =='':
      print('Nome do titular não pode ser em branco')
    else:
      self.__titular = novotitular
      
  @property
  def numero(self):
    return self.__numero
  
  @numero.setter
  def numero(self, novonumero):
    if type(novonumero) != int:
       print("Digite apenas numeros!")
    else:
      self.__numero = novonumero
  
  @property
  def saldo(self):
    return self.__saldo
  
  @saldo.setter
  def saldo(self, novosaldo):
    if (novosaldo < 0):
      print('Saldo inválido')
    else:
      self.__saldo = novosaldo
  
minhaconta = Conta('1234-2', 'Shirlei M Vendrami', 1232.90)    
print('Saldo da conta: ' + str(minhaconta.saldo))
print(f'Saldo da conta: {minhaconta.saldo}')
print(f'Saldo da conta: R$ %.2f' % minhaconta.saldo)
minhaconta.saldo = 600.77
print(f'Saldo da conta: {minhaconta.saldo}')
minhaconta.saldo = -500
print(f'Saldo da conta: {minhaconta.saldo}')
minhaconta.saldo = float(input('Informe o saldo desejado: '))
print(f'Saldo da conta: {minhaconta.saldo}')
print(f'Número da conta: {minhaconta.numero}')
minhaconta.numero = str(input('Informe o número da conta: '))
print(f'Número da conta: {minhaconta.numero}')
minhaconta.titular = str(input('Informe o nome do titular: '))
print(f'Nome do titular: {minhaconta.titular}')