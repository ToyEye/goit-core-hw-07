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

class Birthday(Field):
    def __init__(self, value):
        try:
            pass
            # Додайте перевірку коректності даних
            # та перетворіть рядок на об'єкт datetime
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")	

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = Birthday(None)

    def add_phone(self,phone):
        self.phones.append(Phone(phone)) # додавання  телефона за допомогою класа Phone
        
        
    def remove_phone(self, phone):
        for el in self.phones:
            if el.value == phone:
                self.phones.remove(el) #видалення телефону
        
    def edit_phone(self, new_phone):
        
        Phone(new_phone)

        self.phones[0]= new_phone
        
    
    def find_phone(self,phone):
        
        if self.name == phone.name:
            return self.phones[0]
        
    
    def __str__(self):
        print(self.phones)
        return f"Contact name: {self.name.value}, phones: {self.phones[0]}"
    

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value]=record  #додавання запису
        

    def find(self, name):

        return self.data.get(name)   #пошук запису
            
    def delete(self, name):
        if name in self.data:
           del self.data[name]     #видалення запису
            
# Створення нової адресної книги
# book = AddressBook()

# # Створення запису для John
# john_record = Record("John")
# john_record.add_phone("1234567890")
# john_record.add_phone("5555555555")

# # Додавання запису John до адресної книги
# book.add_record(john_record)

# # Створення та додавання нового запису для Jane
# jane_record = Record("Jane")
# jane_record.add_phone("9876543210")
# book.add_record(jane_record)

#  # Виведення всіх записів у книзі
# for name, record in book.data.items():
#     print(record)

# # Знаходження та редагування телефону для John
# john = book.find("John")
# john.edit_phone("1234567890", "9223235555")

# print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

#  # Пошук конкретного телефону у записі John
# found_phone = john.find_phone("5555555555")

# print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

# john.edit_phone("9223235555", "1234567890")
# print(john)
# # for name, record in book.data.items():
# #     print(record)

# # Видалення запису Jane
# book.delete("Jane")