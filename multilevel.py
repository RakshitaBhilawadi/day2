class Product:
  def __init__(self,product_name,price):
    self.product_name=product_name
    self.price=price
  def display_product(self):
    print("Product name:",self.product_name)
    print("Price of product is:",self.price)

class ElectronicProduct(Product):
  def __init__(self, product_name, price,brand,warranty):
    super().__init__(product_name, price)
    self.brand=brand
    self.warranty=warranty
  def display_electronic_product(self):
    print("Brand:", self.brand)
    print("Warranty:", self.warranty, "years")
class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
      super().__init__(product_name, price, brand, warranty)
      self.ram = ram
      self.storage = storage

    def display_mobile_details(self):
      self.display_product()
      self.display_electronic_product()
      print("RAM:", self.ram, "GB")
      print("Storage:", self.storage, "GB")

mobile = MobilePhone(
    product_name="Samsung Galaxy S23",
    price=74999,
    brand="Samsung",
    warranty=2,
    ram=8,
    storage=256
)
mobile.display_mobile_details()

