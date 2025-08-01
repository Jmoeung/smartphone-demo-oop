class Smartphone:
    def __init__(self, brand, model, storage_gb):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb

    def display_info(self):
        return f"{self.brand} {self.model} with {self.storage_gb}GB storage"

phone1 = Smartphone("Apple", "iPhone 13", 128)
phone2 = Smartphone("Samsung", "Galaxy S21", 256)

print('Phone 1 Information:')
print(phone1.display_info())
print('Phone 2 Information:')
print(phone2.display_info())