import Pyro4

@Pyro4.expose
class BasicCalculator(object):
  
  def add(self, x, y):
    return x + y

  def subtract(self, x, y):
    return x - y

  def multiply(self, x, y):
    return x * y

  def divide(self, x, y):
    return x / y



# @Pyro4.expose
# class GreetingMaker(object):
#     def get_fortune(self, name):
#         return "Hello, {0}. Here is your fortune message: \n"\
#                 "Behold the warranty -- the bold print giveth and the fine print taketh awai.".format(name)