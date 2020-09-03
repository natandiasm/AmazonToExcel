import xlsxwriter


class Excel:
    """ Cria um arquivo com o nome e preco dos produtos """

    def create_file(self, products):
        # cria o arquivo
        workbook = xlsxwriter.Workbook('products.xlsx')
        # adiciona uma nova pasta no arquivo
        worksheet = workbook.add_worksheet()
        # variavel para salvar o numero da columa e linha
        number = 1
        for product in products:
            worksheet.write('A{}'.format(number), product.name)
            worksheet.write('B{}'.format(number), product.price)
            number += 1
        workbook.close()
