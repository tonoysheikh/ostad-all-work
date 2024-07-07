class car:
    def __init__(self , name , model , year):
        self.name = name
        self.model = model
        self.year = year
    def __str__(self):
        return f"The car is {self.name} {self.model} and year {self.year}"

c1 = car("Toyota" , "Camry" , 2023)
c2 = car("subaru" , "Forester" , 2020)

print(c1)
print(c2)