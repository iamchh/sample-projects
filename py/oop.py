class laptop():
    def __init__(self,name,id,ram):
        self.name = name
        self.id = id
        self.ram = ram

    def get_details(self):
        return f'Name: {self.name}, Id: {self.id},Ram: {self.ram}'
    
user1 = laptop("Asus",3,8)

print(user1.get_details())
