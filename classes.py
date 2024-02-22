from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    
    def __init__(self, value):
        if len(value) !=0 :
            super().__init__(value)
        else:
            raise ValueError("Incorrect name")
		

class Phone(Field):
    
    def __init__(self, value):
        if len(value) == 10 and value.isdigit() :
            super().__init__(value)
        else:
            raise ValueError('Incorrect phone format')
		

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self,phone):
        self.phones.append(Phone(phone)) # додавання  телефона за допомогою класа Phone
        
    def remove_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                self.phones.remove(el) #видалення телефону
        
    def edit_phone(self, old_phone, new_phone):
        
        Phone(new_phone)
        
        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = new_phone  # зміна номера
                
                break  
        else:
            raise ValueError('Phone doesn\'t exist')   
    
    def find_phone(self,phone):
        for el in self.phones:
            if el.value == phone:
                return Phone(el.value)        #пошук номера
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"
    

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value]=record  #додавання запису

    def find(self, name):
        return self.data.get(name)   #пошук запису
            
    def delete(self, name):
        if name in self.data:
           del self.data[name]     #видалення запису
            
# Створення нової адресної книги
book = AddressBook()

# Створення запису для John
john_record = Record("John")
john_record.add_phone("1234567890")
john_record.add_phone("5555555555")

# Додавання запису John до адресної книги
book.add_record(john_record)

# Створення та додавання нового запису для Jane
jane_record = Record("Jane")
jane_record.add_phone("9876543210")
book.add_record(jane_record)

 # Виведення всіх записів у книзі
for name, record in book.data.items():
    print(record)

# Знаходження та редагування телефону для John
john = book.find("John")
john.edit_phone("1234567890", "9223235555")

print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

 # Пошук конкретного телефону у записі John
found_phone = john.find_phone("5555555555")
print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# for name, record in book.data.items():
#     print(record)

# Видалення запису Jane
book.delete("Jane")