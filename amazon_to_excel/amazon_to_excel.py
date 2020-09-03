from model.amazon import Amazon
from model.excel import Excel

print("Buscando por produtos...")
products = Amazon().get_products("iphone")
if products != []:
    Excel().create_file(products)
    print("Concluido. Arquivo salvo na pasta do programa.")
else:
    print("Não foi possivel obter a informação, tente novamente.")
