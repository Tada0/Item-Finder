from datetime import date, datetime


class FileHandler:

    @staticmethod
    def read_to_list(filename):
        file = open(filename, 'r', encoding='utf-8')
        lines = []
        for line in file.readlines():
            lines.append(line.replace('\n', ''))
        file.close()
        return lines

    @staticmethod
    def add_new_products(filename, products):
        file = open(filename, 'a+', encoding='utf-8')
        for product in products:
            file.write('\n' + date.today().isoformat().replace('-', '') + ' ' + str(product))
        file.close()

    @staticmethod
    def check_with_existing_products(filename, products):
        new_products_str = [str(product) for product in products if product is not None]
        existing_products = [url[9:] for url in FileHandler.read_to_list(filename)]

        for existing_product in existing_products:
            if existing_product in new_products_str:
                new_products_str.remove(existing_product)

        return [product for product in products if str(product) in new_products_str]

    @staticmethod
    def delete_old_products(filename, limit):
        urls = [url for url in FileHandler.read_to_list(filename) if url]
        valid_urls = [url for url in urls if (date.today() - datetime.strptime(url[:8], "%Y%m%d").date()).days < limit]
        file = open(filename, 'w', encoding='utf-8')
        for url in valid_urls:
            file.write('\n' + url)
        file.close()