from unittest import result

from database.DAO import DAO


class Model:
    def __init__(self):
        self._dao = DAO()

    def trova_anni(self):
        return self._dao.estrai_anno()

    def trova_brand(self):
        return self._dao.estrai_brand()

    def trova_retailer(self):
        return self._dao.estrai_retailer()

    def trova_top_vendite(self, anno, brand, retailer):
        return self._dao.estrai_top_vendite(anno, brand, retailer)

    def analizza_vendite(self,anno ,brand,retailer):
        vendite=self._dao.analizza_vendite(anno ,brand,retailer)
        results=[]
        girodaffari = 0
        numero_vendite = 0
        numero_retailers=[]
        num_prodotti=[]
        for v in vendite:
            girodaffari += (v.quantity * v.unit_sale_price)
            numero_vendite += v.quantity
            if len(numero_retailers)==0 and len(num_prodotti)==0:
                numero_retailers.append(v.retailer_code)
                num_prodotti.append(v.product_number)
            elif v.retailer_code not in numero_retailers:
                numero_retailers.append(v.retailer_code)
            elif v.product_number not in num_prodotti:
                num_prodotti.append(v.product_number)


        results.append(girodaffari)
        results.append(numero_vendite)
        results.append(len(numero_retailers))
        results.append(len(num_prodotti))
        return results


