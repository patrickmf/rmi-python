import Pyro4

calculator = None

# server = Pyro4.Proxy(uri)         # get a Pyro proxy to the greeting object
basicUri = input("What is the Pyro uri of the basic calculator object? ").strip()
basic_calculator = Pyro4.Proxy(basicUri)

scientificUri = input("What is the Pyro uri of the scientific calculator object? ").strip()
scientific_calculator = Pyro4.Proxy(scientificUri)

print("Escolha qual o tipo de calculadora:")
print("1 - basica")
print("2 - cientifica")
type = int(input())



if type == 1:
  calculator = basic_calculator
  print(calculator.add(2, 2))

  print("Escolha qual operacao ira realizar:")
  print("1 - somar")
  print("2 - subtrair")
  print("3 - multiplicar")
  print("4 - dividir")

  operation = int(input())

  if operation == 1:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format(result = calculator.add(valor1, valor2)))

  elif operation == 2:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format( result = calculator.subtract(valor1, valor2)))

  elif operation == 3:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format( result = calculator.multiply(valor1, valor2)))
  
  elif operation == 4:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format( result = calculator.divide(valor1, valor2)))

  else:
    print("Operacao invalida")

elif type == 2:
  calculator = scientific_calculator

  print("Escolha qual operacao ira realizar:")
  print("1 - somar")
  print("2 - subtrair")
  print("3 - multiplicar")
  print("4 - dividir")
  print("5 - potenciacao")
  print("6 - radiciacao")

  operation = int(input())

  if operation == 1:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format( result = calculator.add(valor1, valor2)))

  elif operation == 2:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format( result = calculator.subtract(valor1, valor2)))

  elif operation == 3:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format( result = calculator.multiply(valor1, valor2)))
  
  elif operation == 4:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format( result = calculator.divide(valor1, valor2)))

  elif operation == 5:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format( result = calculator.potentiation(valor1, valor2)))

  elif operation == 6:
    valor1 = int(input("Digite o primeiro valor: "))
    valor2 = int(input("Digite o segundo valor: "))
    print("O resultado da soma: {result}".format( result = calculator.radication(valor1, valor2)))

  else:
    print("Operacao invalida")

else:
  print("Operacao invalida")


# print(greeting_maker.get_basic_calculator_uri())