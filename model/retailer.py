from dataclasses import dataclass

@dataclass
class Retailer:
    retailer_code: int
    retailer_name: str
    type: str
    country: str

    def __str__(self):
        return (f"{self.retailer_code}")


