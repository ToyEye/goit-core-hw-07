from decorators import input_error
from classes import Record
from datetime import datetime

@input_error
def add_contact(args, book):
    name, phone = args
    findName = book.find(name)
    
    if not findName :
        new_record = Record(name)
        new_record.add_phone(phone) 
        book.add_record(new_record)
        
        return f"Contact {name} added."
    else:
        findName.add_phone(phone)
        return f"Phone added to contact {name}."

@input_error
def change_contact(args, book):
    name, old_phone,new_phone = args
    contact = book.find(name)
   
    if contact:
        contact.edit_phone(old_phone,new_phone)
        return "Contact changed."
    else:
        return "Conctact not exist"
    
@input_error
def show_phone(args, book):
    name,phone = args

    contact = book.find(name)
    if contact:
        found_phone=contact.find_phone(phone)
        return found_phone

    else:
        return "Conctact not exist"
    
@input_error
def show_all(book):
    
    for name, record in book.data.items():
         
       yield record


@input_error
def add_birthday(args, book):
    name,date = args
    contact=book.find(name)
    
    if contact:  
        contact.add_birthday(date)
        return "B-day Added"
    
    else:
        return "Conctact not exist"


@input_error
def show_birthday(args, book):
    name = args[0]
    
    contact=book.find(name)
    
    if contact:
        b_day=contact.show_birthday(name)
        return b_day
    else:
        return "Conctact not exist"
    
@input_error
def birthdays(book):
    
    for name, record in book.data.items():
        contact = book.find(name)
        congrats = contact.birthdays(name)
        if not congrats:
            return 'No one to congratulate next week' 
        
        else:
            yield congrats
        
@input_error
def delete_contact(args,book):
    name=args[0]
    
    contact = book.find(name)
    if contact:
        book.delete(name)
        return f"Contact {name} deleted"
    else:
        return f"Contact {name} don't exist" 
        

# add Alex 1234569879
# add-birthday Alex 26.02.1990
# show-birthday Alex
# birthdays