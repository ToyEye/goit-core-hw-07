from decorators import input_error
from classes import Record

@input_error
def add_contact(args, book):
    name, phone = args
    findName = book.find(name)
    
    if not findName :
        new_record = Record(name)
        new_record.add_phone(phone) 
        book.add_record(new_record)
        
        return "Contact added."
    else:
        return "Contact exist"

@input_error
def change_contact(args, book):
    name, phone = args
    contact = book.find(name)
   
    if contact:
        contact.edit_phone(phone)
        return "Contact changed."
    else:
        return "Conctact not exist"
    
@input_error
def show_phone(args, book):
    name = args[0]

    contact = book.find(name)
    if contact:
        found_phone=contact.find_phone(contact)
        return found_phone

    else:
        return "Conctact not exist"
    
@input_error
def show_all(book):
    all_contacts = []
    
    for name, record in book.data.items():
         
        all_contacts.append(str(record))
          
    return all_contacts


# @input_error
def add_birthday(args, book):
    name,date = args
    contact=book.find(name)
    if contact:  
        b_day=contact.add_birthday(date)
        return b_day


@input_error
def show_birthday(args, book):
    pass
    # реалізація

@input_error
def birthdays(args, book):
    pass
    # реалізація



# add Alex 1234569879