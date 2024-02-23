from collections import UserDict
from datetime import datetime
from  helpers import get_upcoming_birthdays

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
            validDate = datetime.strptime(value,"%d.%m.%Y").date()
            super().__init__(validDate)
        
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")	

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phone = ''
        self.birthday = None

    def add_phone(self,phone):
        self.phone = Phone(phone) # додавання  телефона за допомогою класа Phone
        
        
    def edit_phone(self, new_phone):
        
        Phone(new_phone)

        self.phone= new_phone
        
    
    def find_phone(self,phone):
        if self.name == phone.name:
            return self.phone
    
    def add_birthday(self,b_day):
        
        self.birthday= Birthday(b_day)   
        return self.birthday
    
    def show_birthday(self,name):
        if self.name.value == name:
            return self.birthday
        
    def birthdays(self,name):
        if self.name.value == name and self.birthday:
              user={"name":self.name.value,"birthday":self.birthday.value.strftime("%d.%m.%Y") }  
              b_day = get_upcoming_birthdays(user)
              return b_day
         
    
    def __str__(self):
        print(self.phone)
        return f"Contact name: {self.name.value}, phone: {self.phone}, birthday: {self.birthday}"
    

class AddressBook(UserDict):
    def add_record(self,record):
        self.data[record.name.value]=record  #додавання запису
        

    def find(self, name):
        return self.data.get(name)   #пошук запису
            
           