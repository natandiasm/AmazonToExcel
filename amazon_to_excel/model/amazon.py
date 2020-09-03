import requests
from bs4 import BeautifulSoup

from .product import Product


class Amazon:
    """Converte o soup em uma lista de objetos do tipo Product """

    def __objectification_products(self, products):
        list_product = []
        for product in products:
            name = product.find("span", "a-size-base-plus a-color-base a-text-normal").text
            price = product.find("span", "a-offscreen")
            if price is None:
                price = "Sem preço"
            else:
                price = price.text
            item = Product(name=name, price=price)
            list_product.append(item)
        return list_product

    """Retorna uma lista com objetos Product """

    def get_products(self, name):
        req = requests.get('https://www.amazon.com.br/s?k={}&__mk_pt_BR=ÅMÅŽÕÑ&ref=nb_sb_noss'.format(name))
        if req.status_code == 200:  # Verifica se tudo ocorreu com sucesso
            page = req.content  # Volta com o conteúdo da página
            # obtem a pagina
            soup = BeautifulSoup(page, 'html.parser')
            # seleciona todos os produtos
            products = soup.find_all("div", {"class": "a-section a-spacing-medium"})
            # converte para objetos
            products = self.__objectification_products(products)
            # retorna a lista
            return products

        else:
            return []
