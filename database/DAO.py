from database.DB_connect import DBConnect
from model.retailer import Retailer


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
