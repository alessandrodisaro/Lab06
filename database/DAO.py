from database.DB_connect import DBConnect
from model.retailer import Retailer
from model.vendite import Vendite


class DAO():
    def __init__(self):
        pass

    def estrai_anno(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = ("SELECT DISTINCT YEAR(Date) AS anno FROM go_daily_sales")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row[
                              "anno"])  # nella query creo un dizzionario con chiave anno con valori gli anni, qui appendo i valori delle key con valore anno
        cursor.close()
        conn.close()
        if result is not None:
            return result
        else:
            return None

    def estrai_brand(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = ("SELECT DISTINCT Product_brand as p FROM go_products")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row["p"])
        cursor.fetchall()
        cursor.close()
        conn.close()
        if result is not None:
            return result
        else:
            return None

    def estrai_retailer(self):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)
        query = ("SELECT * FROM go_retailers")
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(Retailer(row["Retailer_code"], row["Retailer_name"], row["Type"], row[
                "Country"]))  # creo un oggetto retailer qui dentro ogni volta che ho un risultato di una query
        cursor.close()
        conn.close()
        if result is not None:
            return result
        else:
            return None

    def estrai_top_vendite(self, anno, brand, retailer):
        conn = DBConnect.get_connection()
        cursor = conn.cursor(dictionary=True)

        # query = """SELECT * FROM go_daily_sales
        #         WHERE year(Date)= %s and Retailer_code =%s and Product_number
        #          in (select Product_number from go_products where Product_brand=%s)"""
        # questa riga sopra per ualche ragione e' moolto piu lenta
        query = """SELECT * FROM go_daily_sales gds, go_products gp
                    WHERE year(Date)=coalesce( %s,year(Date)) and Retailer_code =coalesce(%s,Retailer_code)
                    and gds.Product_number = gp.Product_number
                    and gp.Product_brand=coalesce(%s,Product_brand)"""
        cursor.execute(query, (anno, retailer, brand))
        vendite = []
        for row in cursor:
            vendite.append(Vendite(row["Date"], row["Unit_sale_price"], row["Quantity"],
                                   row["Retailer_code"], row["Product_number"]))
        if vendite is not None:
            vendite.sort(reverse=True)
        else:
            print("Query vuota")
        if len(vendite) >= 5:
            result = vendite[0:5]
        else:
            result = vendite[0:len(vendite)]
        cursor.close()
        conn.close()
        return result

    def analizza_vendite(self, anno, brand, retailer):
        cnx = DBConnect.get_connection()
        cursor = cnx.cursor()
        # query = """SELECT *  FROM go_daily_sales gds,go_products gp
        #             WHERE year(Date)= coalesce(%s,year(Date)) and Retailer_code=(%s,Retailer_code)
        #             and Product_number in (select Product_number from go_products where Product_brand=(%s,Product_brand))"""
        query = """SELECT * FROM go_daily_sales gds, go_products gp
                    WHERE year(Date)=coalesce( %s,year(Date)) and Retailer_code =coalesce(%s,Retailer_code)
                    and gds.Product_number = gp.Product_number
                    and gp.Product_brand=coalesce(%s,Product_brand)"""
        cursor.execute(query, (anno, retailer, brand))
        result = []
        for row in cursor:
            result.append(Vendite(row[3], row[6], row[4], row[0],
                                  row[1]))
        if result is None:
            print("Query vuota")
        cursor.close()
        cnx.close()
        return result
