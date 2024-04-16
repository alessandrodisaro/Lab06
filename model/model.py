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


