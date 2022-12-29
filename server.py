import Pyro4
from models.BasicCalculator import BasicCalculator
from models.ScientificCalculator import ScientificCalculator

basicCalculator = BasicCalculator()
scientificCalculator = ScientificCalculator()

print(basicCalculator.add(2,2))

class server:
    def __init__(self) -> None:
        basic: basicCalculator
        scientific: scientificCalculator
        pass

Pyro4.Daemon.serveSimple({
    basicCalculator: "basic_calculator",
    ScientificCalculator: "scientific_calculator"
},
ns=False,
host="localhost",
port=8000,
)

# @Pyro4.expose
# class GreetingMaker(object):
#     def get_basic_calculator_uri(self):
#         return uri1

#     def get_scientific_calculator_uri(self):
#         return uri2



# print("Ready. Object uri =", uri)      # print the uri so we can use it in the client later
# print("")
# print(uri1)
# print(uri2)
# daemon.requestLoop()
