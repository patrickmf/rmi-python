import Pyro4

@Pyro4.expose
class ScientificCalculator(object):
  
  def add(self, x, y):
    return x + y

  def subtract(self, x, y):
    return x - y

  def multiply(self, x, y):
    return x * y

  def divide(self, x, y):
    return x / y

  def potentiation(self, x, y):
    return x ** y

  def radication(self, x, y):
    return x ** (1/y)