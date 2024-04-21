import datetime
from dataclasses import dataclass

@dataclass
class Vendite:
    data: datetime.date
    unit_sale_price: float
    quantity: int
    retailer_code: int
    product_number: int

    def __str__(self):
        return f"Date: {self.data}; Ricavo: {int(self.quantity)*float(self.unit_sale_price)}; Retailer: {self.retailer_code}; Product: {self.product_number}"

    def __lt__(self, other):
        return (self.quantity*self.unit_sale_price) < (other.quantity*self.unit_sale_price)

    # def __str2__(self):
    #     pass


